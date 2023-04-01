# this code download cost data from every origin-destination pair and for every truck configuration. 
# 31/03/2023
# Author: Andrés Rengifo

#### importing packages

import pandas as pd
import os
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By   
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup as bs

from selenium.webdriver.chrome.service import Service   
from selenium.webdriver.support.ui import WebDriverWait    
from selenium.common.exceptions import TimeoutException    
from selenium.webdriver.support import expected_conditions as EC 
import re

os.chdir("..\\output")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome(ChromeDriverManager().install())  ## depreciated
enlaces = "https://plc.mintransporte.gov.co/Runtime/empresa/ctl/SiceTAC/mid/417"
driver.get(enlaces)
driver.maximize_window()



periodos= pd.read_excel("periodos.xlsx")
OD = pd.read_excel("OD.xlsx")
combinaciones= pd.read_excel('combinaciones.xlsx')
df_origen= driver.find_elements(By.XPATH,"//select[@name='dnn$ctr417$SiceTAC$ORIGEN']/option")
df_origen=  [d.text for d in df_origen]
df_origen.pop(0)
df_origen

##preparing the datasets before the scraping

### Panel costos operativos resumen
df_cost_resumen = pd.DataFrame(columns = ['origen', 
'destino',
'config_v',
'tipo_carga',
'tipo_unidad',
'Tonelada x KM Movilzación',
 'Costo Tonelada Movilización',
 'Costo Movilización Carga',
 'Costo Hora Adicional',
 'Horas de Espera',
 'Costo Tiempos de Espera',
 'Tonelada x KM del Viaje',
 'Costo Tonelada del Viaje',
 'Costo Total del Viaje',
 'Costo x KM Movilización',
 'Costo x KM del Viaje'])

#### Colnames has to mach with the colnames in the detailed cost table. 

df_cost_detalle = pd.DataFrame(columns = ['origen', 
'destino',
'config_v',
'tipo_carga',
'tipo_unidad',
'Tipo de costo',
 'Concepto',
 'Valor Mes',
 'Valor por viaje',
 'Valor por tonelada',
 'Participación'])
#### 


#### current month scraping 

#### setting the hours
horas=int(1) 

hour_item= driver.find_element(By.XPATH,"//input[@name='dnn$ctr417$SiceTAC$HORASCARGUE']")
hour_item.clear()
hour_item.send_keys(horas)  
hour_item=driver.find_element(By.XPATH,"//input[@name='dnn$ctr417$SiceTAC$HORASDESCARGUE']")
hour_item.clear()
hour_item.send_keys(horas)  
hour_item=driver.find_element(By.XPATH,"//input[@name='dnn$ctr417$SiceTAC$HORASESPERACARGUE']")
hour_item.clear()
hour_item.send_keys(horas)  
hour_item= driver.find_element(By.XPATH,"//input[@name='dnn$ctr417$SiceTAC$HORASESPERADESCARGUE']")
hour_item.clear()
hour_item.send_keys(horas)

it=0

for x in range(len(combinaciones)):
    config_op = Select(driver.find_element(By.XPATH,"//select[@name='dnn$ctr417$SiceTAC$CONFIGURACION']"))
    config_op.select_by_visible_text(combinaciones.loc[x,"config_v"])
    carga_op = Select(driver.find_element(By.XPATH,"//select[@name='dnn$ctr417$SiceTAC$TIPOCARGA']"))
    carga_op.select_by_visible_text(combinaciones.loc[x,"tipo_carga"])
    tipo_op = Select(driver.find_element(By.XPATH,"//select[@name='dnn$ctr417$SiceTAC$UNIDADTRANSPORTE']"))
    tipo_op.select_by_visible_text(combinaciones.loc[x,"tipo_unidad"])
    time.sleep(1.5)
    for o in df_origen:
         org = Select(driver.find_element(By.XPATH,"//select[@name='dnn$ctr417$SiceTAC$ORIGEN']"))
         org.select_by_visible_text(o)
         time.sleep(1.5)
         df_destino= OD[(OD['origen']== o)]['destino'].tolist()
         for d in df_destino:
            des = Select(driver.find_element(By.XPATH,"//select[@name='dnn$ctr417$SiceTAC$DESTINO']"))
            des.select_by_visible_text(d)
            time.sleep(1.5)
            
            #### calculo 
            calculo_text = driver.find_element(By.XPATH,"//span[@id='dnn_ctr417_SiceTAC_Cat']").text
            calculo_text=calculo_text.split()
            calculo_text= int(calculo_text[2])+int(calculo_text[4])
            calculo = driver.find_element(By.XPATH,"//input[@name='dnn$ctr417$SiceTAC$Resultado']")
            calculo.clear()
            time.sleep(1)
            calculo.send_keys(calculo_text)       
            calcular = driver.find_element(By.XPATH,"//a[@id='dnn_ctr417_SiceTAC_btCalcular']")
            calcular.click()
            time.sleep(1)
            try: 
                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
                time.sleep(1)
            except:
                time.sleep(1)
            ### using BS
            bs_obj = bs(driver.page_source, 'html.parser')

            #### extrac data 1: cost resumen
            cost_resume= bs_obj.find_all('input', class_='aspNetDisabled form-control text-right')
            for i in range(11):
                col= i+5   
                df_cost_resumen.loc[it, df_cost_resumen.columns[col]]= cost_resume[i]['value']
            for col in combinaciones.columns:
                df_cost_resumen.loc[it, col]= combinaciones.loc[x,col]  

            df_cost_resumen.loc[it, 'origen' ]=  o
            df_cost_resumen.loc[it, 'destino' ]=  d

            #### extrac data 2: cost delailed
            det_cost= bs_obj.find('table', id='dnn_ctr417_SiceTAC_tvDatos')
            columns = [i.get_text(strip=True) for i in det_cost.find_all("th")]

            files=det_cost.find('tbody').find_all("tr")   ### tbody distinge el cuerpo de la tabla. tr distingue las filas:
            data_det_cost= []
            for tr in files: 
                data_det_cost.append([td.get_text(strip=True) for td in tr.find_all("td")])  #### td identifica las columnas. Cada lista en esta iteración es una fila

            data_det_cost.pop(0)
            df= pd.DataFrame(data_det_cost, columns=columns) 
            df["origen"]= o 
            df["destino"]= d
            df["config_v"]= combinaciones.loc[x,'config_v']  ### 1 reemplazar por x
            df["tipo_carga"]= combinaciones.loc[x,'tipo_carga']
            df["tipo_unidad"]= combinaciones.loc[x,'tipo_unidad']
            df_cost_detalle=pd.concat([df_cost_detalle, df ])


            it= it+1
            #driver.execute_script("window.history.go(-1)")
            #driver.get(enlaces)
            time.sleep(1)

df_cost_detalle.to_excel('cost_detalle.xlsx', index=False)
df_cost_resumen.to_excel('cost_resumen.xlsx', index=False)




