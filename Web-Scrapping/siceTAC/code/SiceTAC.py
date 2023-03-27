# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 20:26:10 2022

@author: juanc
"""
import pandas as pd
import os
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import re

os.chdir(r"C:\Users\juanc\Google Drive\Andes\Web scraping")
driver = webdriver.Chrome(ChromeDriverManager().install())
enlaces = "https://plc.mintransporte.gov.co/Runtime/empresa/ctl/SiceTAC/mid/417"
driver.get(enlaces)
driver.maximize_window()
body = driver.execute_script("return document.body")
source = body.get_attribute('innerHTML')
time.sleep(1)
# #selectores
# config = driver.find_elements_by_xpath("//select[@name='dnn$ctr417$SiceTAC$CONFIGURACION']/option")
# config = [d.text for d in config]
# config.pop(0) 
# carga = driver.find_elements_by_xpath("//select[@name='dnn$ctr417$SiceTAC$TIPOCARGA']/option")
# carga = [d.text for d in carga]
# carga.pop(0) 
# tipo = driver.find_elements_by_xpath("//select[@name='dnn$ctr417$SiceTAC$UNIDADTRANSPORTE']/option")
# tipo = [d.text for d in tipo]
# tipo.pop(0)
# origen = driver.find_elements_by_xpath("//select[@name='dnn$ctr417$SiceTAC$ORIGEN']/option")
# origen = [d.text for d in origen]
# origen.pop(0) 
# destino = driver.find_elements_by_xpath("//select[@name='dnn$ctr417$SiceTAC$DESTINO']/option")
# destino = [d.text for d in destino]
# destino.pop(0)

 
# h_cargue = driver.find_element_by_xpath("//input[@name='dnn$ctr417$SiceTAC$HORASCARGUE']")
# h_cargue.clear()
# h_cargue.send_keys("1")
# h_descargue = driver.find_element_by_xpath("//input[@name='dnn$ctr417$SiceTAC$HORASDESCARGUE']") 
# h_descargue.clear()
# h_descargue.send_keys("1")
# h_e_cargue = driver.find_element_by_xpath("//input[@name = 'dnn$ctr417$SiceTAC$HORASESPERACARGUE']")
# h_e_cargue.clear()
# h_e_cargue.send_keys("1")
# h_e_descargue = driver.find_element_by_xpath("//input[@name='dnn$ctr417$SiceTAC$HORASESPERADESCARGUE']")
# h_e_descargue.clear()
# h_e_descargue.send_keys("1")
# calculo_text = driver.find_element_by_xpath("//span[@id='dnn_ctr417_SiceTAC_Cat']").text
# calculo_text=calculo_text.split()
# calculo_text= int(calculo_text[2])+int(calculo_text[4])
# calculo = driver.find_element_by_xpath("//input[@name='dnn$ctr417$SiceTAC$Resultado']")
# calculo.send_keys(calculo_text)
# calcular = driver.find_element_by_xpath("//a[@id='dnn_ctr417_SiceTAC_btCalcular']")
# calcular.click()
# alert = driver.switch_to.alert
# alert.text
# alert.accept()

# #Combinaciones posibles
# c_oper = driver.find_element_by_xpath("//td[@colspan='6']").text 
# c_oper == "No hay conceptos de costo para mostrar"

# config_v = []
# tipo_carga = []
# tipo_unidad = []
# for co in config:
#     for ca in carga:
#         for ti in tipo:
#             calculo = driver.find_element_by_xpath("//input[@name='dnn$ctr417$SiceTAC$Resultado']")
#             calculo.clear()
#             config_op = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$CONFIGURACION']"))
#             config_op.select_by_visible_text(co)
#             carga_op = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$TIPOCARGA']"))
#             carga_op.select_by_visible_text(ca)
#             tipo_op = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$UNIDADTRANSPORTE']"))
#             tipo_op.select_by_visible_text(ti)
#             time.sleep(2)
#             org = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$ORIGEN']"))
#             org.select_by_visible_text(origen[17])
#             org = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$DESTINO']"))
#             org.select_by_visible_text(destino[8])
#             calculo_text = driver.find_element_by_xpath("//span[@id='dnn_ctr417_SiceTAC_Cat']").text
#             calculo_text=calculo_text.split()
#             calculo_text= int(calculo_text[2])+int(calculo_text[4])
#             calculo = driver.find_element_by_xpath("//input[@name='dnn$ctr417$SiceTAC$Resultado']")
#             calculo.send_keys(calculo_text)
#             calcular = driver.find_element_by_xpath("//a[@id='dnn_ctr417_SiceTAC_btCalcular']")
#             time.sleep(2)
#             calcular.click()
#             time.sleep(2)
#             alert = driver.switch_to.alert
#             alert.accept()
#             time.sleep(2)
#             try:
#                 c_oper = driver.find_element_by_xpath("//td[@colspan='6']").text 
#             except:
#                 c_oper = ""
#             if c_oper != "No hay conceptos de costo para mostrar":
#                config_v.append(co) 
#                tipo_carga.append(ca)
#                tipo_unidad.append(ti)

# df = pd.DataFrame()
# df["config_v"] = config_v
# df["tipo_carga"] = tipo_carga
# df["tipo_unidad"] = tipo_unidad
# #guardar info
# df.to_excel("combinaciones.xlsx", index=False)

df = pd.read_excel("combinaciones.xlsx")


# COR = Costos Operativos - Resumen
# COD = Costos Operativos - Detalle
# PH  = Parámetros de la herramienta
# PDC = Parámetros distancias y combustible
# PP  = Parámetros de peajes
# PL  = Parámetros de llantas
# PLu = Parámetros de lubricantes
# PF  = Parámetros de filtros
# PMR = Parámetros de Mantenimiento y Reparación
# PLE = Parámetros de Lavado y Engrase

COR = pd.DataFrame(columns = ['Tonelada x KM Movilzación',
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
COD = pd.DataFrame()
PH = pd.DataFrame(columns = ['Horas Hábiles del mes',
 'Valor Combustible galón ACPM ',
 'Toneladas de la Configuración '])
PDC = pd.DataFrame(columns = ['Distancia (Km) - Total',
 'Distancia (Km) - Plano',
 'Distancia (Km) - Ondulado',
 'Distancia (Km) - Montaña',
 'Velocidad Promedio - Total',
 'Velocidad Promedio - Plano',
 'Velocidad Promedio - Ondulado',
 'Velocidad Promedio - Montaña',
 'Horas de viaje  - Total',
 'Horas de viaje  - Plano',
 'Horas de viaje  - Ondulado',
 'Horas de viaje  - Montaña',
 'Consumo de Combustible (Km/gln) - Total',
 'Consumo de Combustible (Km/gln) - Plano',
 'Consumo de Combustible (Km/gln) - Ondulado',
 'Consumo de Combustible (Km/gln) - Montaña',
 'Valores Combustible  - Total',
 'Valores Combustible  - Plano',
 'Valores Combustible  - Ondulado',
 'Valores Combustible  - Montaña',
 'Horas Recorrido (Viaje + Espera)',
 'Recorridos en el Mes'])
PP = pd.DataFrame()
PL = pd.DataFrame()
PLu = pd.DataFrame()
PF = pd.DataFrame()
PMR = pd.DataFrame()
PML = pd.DataFrame()

OD = pd.read_excel("OD.xlsx")
#df = df[11:].reset_index(drop=True)
for x in range(len(df)):
    for O in range(len(OD)): 
                try:                      
                    config_op = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$CONFIGURACION']"))
                    config_op.select_by_visible_text(df.loc[x,"config_v"])
                    carga_op = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$TIPOCARGA']"))
                    carga_op.select_by_visible_text(df.loc[x,"tipo_carga"])
                    tipo_op = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$UNIDADTRANSPORTE']"))
                    tipo_op.select_by_visible_text(df.loc[x,"tipo_unidad"])
                    time.sleep(1.5)
                    org = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$ORIGEN']"))
                    org.select_by_visible_text(OD.loc[O,"origen"])
                    time.sleep(1.5)
                    des = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$DESTINO']"))
                    des.select_by_visible_text(OD.loc[O,"destino"])
                    calculo_text = driver.find_element_by_xpath("//span[@id='dnn_ctr417_SiceTAC_Cat']").text
                    calculo_text=calculo_text.split()
                    calculo_text= int(calculo_text[2])+int(calculo_text[4])
                    calculo = driver.find_element_by_xpath("//input[@name='dnn$ctr417$SiceTAC$Resultado']")
                    calculo.send_keys(calculo_text)
                    calcular = driver.find_element_by_xpath("//a[@id='dnn_ctr417_SiceTAC_btCalcular']")
                    calcular.click()
                    time.sleep(1)
                    try:
                        time.sleep(1)
                        alert = driver.switch_to.alert
                        alert.accept()
                        time.sleep(1)
                    except:
                        time.sleep(1)
                        alert = driver.switch_to.alert
                        alert.accept()
                    time.sleep(1)
                    body = driver.execute_script("return document.body")
                    source = body.get_attribute('innerHTML')
                    sopa = bs(source, 'html.parser')
                    inputs = sopa.find_all("input", "aspNetDisabled form-control text-right")
                    inputs2 =[]
                    for i in inputs:
                        try:
                            inputs2.append(i["value"])
                        except:
                            inputs2.append("NA")
                    
                    labels = sopa.find_all("label", "col-md-2 control-label text-right")
                    labels2 = []
                    for i in labels:
                        try:
                            labels2.append(i.get_text())
                        except:
                            labels2.append("0")
                    
                    labels3 = sopa.find_all("label", "col-md-3 control-label")
                    labels4 = []
                    for i in labels3:
                        try:
                            labels4.append(i.get_text())
                        except:
                            labels4.append("0")
                    labels5 = sopa.find_all("label", "col-md-4 control-label")
                    labels6 = []
                    for i in labels5:
                        try:
                            labels6.append(i.get_text())
                        except:
                            labels6.append("0")
                    
                    inputs_l = []
                    inputs_l.append(labels2[0])
                    inputs_l.append(labels2[1])
                    inputs_l.append(labels2[2])
                    inputs_l.append(labels2[3])
                    inputs_l.append(labels2[4])
                    inputs_l.append(labels2[5])
                    inputs_l.append(labels2[6])
                    inputs_l.append(labels2[7])
                    inputs_l.append(labels2[8])
                    inputs_l.append(labels2[9])
                    inputs_l.append(labels2[10])
                    inputs_l.append(labels4[0])
                    inputs_l.append(labels4[1])
                    inputs_l.append(labels4[2])
                    inputs_l.append(labels4[3] +" - Total")
                    inputs_l.append(labels4[3] +" - "+labels2[-3])
                    inputs_l.append(labels4[3] +" - "+labels2[-2])
                    inputs_l.append(labels4[3] +" - "+labels2[-1])
                    inputs_l.append(labels4[4] +" - Total")
                    inputs_l.append(labels4[4] +" - "+labels2[-3])
                    inputs_l.append(labels4[4] +" - "+labels2[-2])
                    inputs_l.append(labels4[4] +" - "+labels2[-1])
                    inputs_l.append(labels4[5] +" - Total")
                    inputs_l.append(labels4[5] +" - "+labels2[-3])
                    inputs_l.append(labels4[5] +" - "+labels2[-2])
                    inputs_l.append(labels4[5] +" - "+labels2[-1])
                    inputs_l.append(labels4[6] +" - Total")
                    inputs_l.append(labels4[6] +" - "+labels2[-3])
                    inputs_l.append(labels4[6] +" - "+labels2[-2])
                    inputs_l.append(labels4[6] +" - "+labels2[-1])
                    inputs_l.append(labels4[7] +" - Total")
                    inputs_l.append(labels4[7] +" - "+labels2[-3])
                    inputs_l.append(labels4[7] +" - "+labels2[-2])
                    inputs_l.append(labels4[7] +" - "+labels2[-1])
                    inputs_l.append(labels4[8])
                    inputs_l.append(labels4[9])
                    inputs_l.append(labels6[0])
                    
                    copia = pd.DataFrame(columns = inputs_l[0:11])
                    t = 0
                    for i in copia:
                        copia.loc[0,i] = inputs2[t]
                        t=t+1
                        if t == 11:
                            break
                    copia["origen"] = OD.loc[O,"origen"]
                    copia["destino"] = OD.loc[O,"destino"]
                    copia["config_v"] = df.loc[x,"config_v"]
                    copia["tipo_carga"] = df.loc[x,"tipo_carga"]
                    copia["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    
                    copia2 = pd.DataFrame(columns = inputs_l[11:14])
                    t = 11
                    for i in copia2:
                        copia2.loc[0,i] = inputs2[t]
                        t=t+1
                        if t == 14:
                            break
                    copia2["origen"] = OD.loc[O,"origen"]
                    copia2["destino"] = OD.loc[O,"destino"]
                    copia2["config_v"] = df.loc[x,"config_v"]
                    copia2["tipo_carga"] = df.loc[x,"tipo_carga"]
                    copia2["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    
                    copia3 = pd.DataFrame(columns = inputs_l[14:])
                    t = 14
                    for i in copia3:
                        copia3.loc[0,i] = inputs2[t]
                        t=t+1
                    copia3["origen"] = OD.loc[O,"origen"]
                    copia3["destino"] = OD.loc[O,"destino"]
                    copia3["config_v"] = df.loc[x,"config_v"]
                    copia3["tipo_carga"] = df.loc[x,"tipo_carga"]
                    copia3["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    COR=COR.append(copia)
                    PH=PH.append(copia2)
                    PDC=PDC.append(copia3)
                    
                    
                    a = sopa.find_all("table")
                    table0=pd.read_html(str(a[0]))[0]
                    table0["origen"] = OD.loc[O,"origen"]
                    table0["destino"] = OD.loc[O,"destino"]
                    table0["config_v"] = df.loc[x,"config_v"]
                    table0["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table0["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    COD=COD.append(table0)
                    
                    table1=pd.read_html(str(a[1]))[0]
                    table1["origen"] = OD.loc[O,"origen"]
                    table1["destino"] = OD.loc[O,"destino"]
                    table1["config_v"] = df.loc[x,"config_v"]
                    table1["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table1["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PP = PP.append(table1)
                    
                    table2=pd.read_html(str(a[2]))[0]
                    table2["origen"] = OD.loc[O,"origen"]
                    table2["destino"] = OD.loc[O,"destino"]
                    table2["config_v"] = df.loc[x,"config_v"]
                    table2["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table2["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PL = PL.append(table2)
                    
                    
                    table3=pd.read_html(str(a[3]))[0]
                    table3["origen"] = OD.loc[O,"origen"]
                    table3["destino"] = OD.loc[O,"destino"]
                    table3["config_v"] = df.loc[x,"config_v"]
                    table3["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table3["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PLu = PLu.append(table3)
                    
                    table4=pd.read_html(str(a[4]))[0]
                    table4["origen"] = OD.loc[O,"origen"]
                    table4["destino"] = OD.loc[O,"destino"]
                    table4["config_v"] = df.loc[x,"config_v"]
                    table4["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table4["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PF=PF.append(table4)
                    
                    table5=pd.read_html(str(a[5]))[0]
                    table5["origen"] = OD.loc[O,"origen"]
                    table5["destino"] = OD.loc[O,"destino"]
                    table5["config_v"] = df.loc[x,"config_v"]
                    table5["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table5["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PMR = PMR.append(table5)
                    
                    table6=pd.read_html(str(a[6]))[0]
                    table6["origen"] = OD.loc[O,"origen"]
                    table6["destino"] = OD.loc[O,"destino"]
                    table6["config_v"] = df.loc[x,"config_v"]
                    table6["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table6["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PML=PML.append(table6)
                    
                    driver.get(enlaces)
                    time.sleep(1)
                except:
                    arreglar = input("refresque la página y escriba ok: ")
                    driver.get(enlaces)
                    body = driver.execute_script("return document.body")
                    source = body.get_attribute('innerHTML')
                    sopa = bs(source, 'html.parser')
                    inputs = sopa.find_all("label", {"class": "col-md-4 control-label text-right"})
                    while inputs == []:
                        driver.get(enlaces)
                        time.sleep(1)
                        body = driver.execute_script("return document.body")
                        source = body.get_attribute('innerHTML')
                        sopa = bs(source, 'html.parser')
                        inputs = sopa.find_all("label", {"class": "col-md-4 control-label text-right"})     
                    config_op = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$CONFIGURACION']"))
                    config_op.select_by_visible_text(df.loc[x,"config_v"])
                    carga_op = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$TIPOCARGA']"))
                    carga_op.select_by_visible_text(df.loc[x,"tipo_carga"])
                    tipo_op = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$UNIDADTRANSPORTE']"))
                    tipo_op.select_by_visible_text(df.loc[x,"tipo_unidad"])
                    time.sleep(1.5)
                    org = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$ORIGEN']"))
                    org.select_by_visible_text(OD.loc[O,"origen"])
                    time.sleep(1.5)
                    des = Select(driver.find_element_by_xpath("//select[@name='dnn$ctr417$SiceTAC$DESTINO']"))
                    des.select_by_visible_text(OD.loc[O,"destino"])
                    calculo_text = driver.find_element_by_xpath("//span[@id='dnn_ctr417_SiceTAC_Cat']").text
                    calculo_text=calculo_text.split()
                    calculo_text= int(calculo_text[2])+int(calculo_text[4])
                    calculo = driver.find_element_by_xpath("//input[@name='dnn$ctr417$SiceTAC$Resultado']")
                    calculo.send_keys(calculo_text)
                    calcular = driver.find_element_by_xpath("//a[@id='dnn_ctr417_SiceTAC_btCalcular']")
                    calcular.click()
                    time.sleep(1)
                    try:
                        time.sleep(1)
                        alert = driver.switch_to.alert
                        alert.accept()
                        time.sleep(1)
                    except:
                        time.sleep(1)
                        alert = driver.switch_to.alert
                        alert.accept()
                    time.sleep(1)
                    body = driver.execute_script("return document.body")
                    source = body.get_attribute('innerHTML')
                    sopa = bs(source, 'html.parser')
                    inputs = sopa.find_all("input", "aspNetDisabled form-control text-right")
                    inputs2 =[]
                    for i in inputs:
                        try:
                            inputs2.append(i["value"])
                        except:
                            inputs2.append("NA")
                    
                    labels = sopa.find_all("label", "col-md-2 control-label text-right")
                    labels2 = []
                    for i in labels:
                        try:
                            labels2.append(i.get_text())
                        except:
                            labels2.append("0")
                    
                    labels3 = sopa.find_all("label", "col-md-3 control-label")
                    labels4 = []
                    for i in labels3:
                        try:
                            labels4.append(i.get_text())
                        except:
                            labels4.append("0")
                    labels5 = sopa.find_all("label", "col-md-4 control-label")
                    labels6 = []
                    for i in labels5:
                        try:
                            labels6.append(i.get_text())
                        except:
                            labels6.append("0")
                    
                    inputs_l = []
                    inputs_l.append(labels2[0])
                    inputs_l.append(labels2[1])
                    inputs_l.append(labels2[2])
                    inputs_l.append(labels2[3])
                    inputs_l.append(labels2[4])
                    inputs_l.append(labels2[5])
                    inputs_l.append(labels2[6])
                    inputs_l.append(labels2[7])
                    inputs_l.append(labels2[8])
                    inputs_l.append(labels2[9])
                    inputs_l.append(labels2[10])
                    inputs_l.append(labels4[0])
                    inputs_l.append(labels4[1])
                    inputs_l.append(labels4[2])
                    inputs_l.append(labels4[3] +" - Total")
                    inputs_l.append(labels4[3] +" - "+labels2[-3])
                    inputs_l.append(labels4[3] +" - "+labels2[-2])
                    inputs_l.append(labels4[3] +" - "+labels2[-1])
                    inputs_l.append(labels4[4] +" - Total")
                    inputs_l.append(labels4[4] +" - "+labels2[-3])
                    inputs_l.append(labels4[4] +" - "+labels2[-2])
                    inputs_l.append(labels4[4] +" - "+labels2[-1])
                    inputs_l.append(labels4[5] +" - Total")
                    inputs_l.append(labels4[5] +" - "+labels2[-3])
                    inputs_l.append(labels4[5] +" - "+labels2[-2])
                    inputs_l.append(labels4[5] +" - "+labels2[-1])
                    inputs_l.append(labels4[6] +" - Total")
                    inputs_l.append(labels4[6] +" - "+labels2[-3])
                    inputs_l.append(labels4[6] +" - "+labels2[-2])
                    inputs_l.append(labels4[6] +" - "+labels2[-1])
                    inputs_l.append(labels4[7] +" - Total")
                    inputs_l.append(labels4[7] +" - "+labels2[-3])
                    inputs_l.append(labels4[7] +" - "+labels2[-2])
                    inputs_l.append(labels4[7] +" - "+labels2[-1])
                    inputs_l.append(labels4[8])
                    inputs_l.append(labels4[9])
                    inputs_l.append(labels6[0])
                    
                    copia = pd.DataFrame(columns = inputs_l[0:11])
                    t = 0
                    for i in copia:
                        copia.loc[0,i] = inputs2[t]
                        t=t+1
                        if t == 11:
                            break
                    copia["origen"] = OD.loc[O,"origen"]
                    copia["destino"] = OD.loc[O,"destino"]
                    copia["config_v"] = df.loc[x,"config_v"]
                    copia["tipo_carga"] = df.loc[x,"tipo_carga"]
                    copia["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    
                    copia2 = pd.DataFrame(columns = inputs_l[11:14])
                    t = 11
                    for i in copia2:
                        copia2.loc[0,i] = inputs2[t]
                        t=t+1
                        if t == 14:
                            break
                    copia2["origen"] = OD.loc[O,"origen"]
                    copia2["destino"] = OD.loc[O,"destino"]
                    copia2["config_v"] = df.loc[x,"config_v"]
                    copia2["tipo_carga"] = df.loc[x,"tipo_carga"]
                    copia2["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    
                    copia3 = pd.DataFrame(columns = inputs_l[14:])
                    t = 14
                    for i in copia3:
                        copia3.loc[0,i] = inputs2[t]
                        t=t+1
                    copia3["origen"] = OD.loc[O,"origen"]
                    copia3["destino"] = OD.loc[O,"destino"]
                    copia3["config_v"] = df.loc[x,"config_v"]
                    copia3["tipo_carga"] = df.loc[x,"tipo_carga"]
                    copia3["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    COR=COR.append(copia)
                    PH=PH.append(copia2)
                    PDC=PDC.append(copia3)
                    
                    
                    a = sopa.find_all("table")
                    table0=pd.read_html(str(a[0]))[0]
                    table0["origen"] = OD.loc[O,"origen"]
                    table0["destino"] = OD.loc[O,"destino"]
                    table0["config_v"] = df.loc[x,"config_v"]
                    table0["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table0["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    COD=COD.append(table0)
                    
                    table1=pd.read_html(str(a[1]))[0]
                    table1["origen"] = OD.loc[O,"origen"]
                    table1["destino"] = OD.loc[O,"destino"]
                    table1["config_v"] = df.loc[x,"config_v"]
                    table1["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table1["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PP = PP.append(table1)
                    
                    table2=pd.read_html(str(a[2]))[0]
                    table2["origen"] = OD.loc[O,"origen"]
                    table2["destino"] = OD.loc[O,"destino"]
                    table2["config_v"] = df.loc[x,"config_v"]
                    table2["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table2["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PL = PL.append(table2)
                    
                    
                    table3=pd.read_html(str(a[3]))[0]
                    table3["origen"] = OD.loc[O,"origen"]
                    table3["destino"] = OD.loc[O,"destino"]
                    table3["config_v"] = df.loc[x,"config_v"]
                    table3["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table3["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PLu = PLu.append(table3)
                    
                    table4=pd.read_html(str(a[4]))[0]
                    table4["origen"] = OD.loc[O,"origen"]
                    table4["destino"] = OD.loc[O,"destino"]
                    table4["config_v"] = df.loc[x,"config_v"]
                    table4["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table4["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PF=PF.append(table4)
                    
                    table5=pd.read_html(str(a[5]))[0]
                    table5["origen"] = OD.loc[O,"origen"]
                    table5["destino"] = OD.loc[O,"destino"]
                    table5["config_v"] = df.loc[x,"config_v"]
                    table5["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table5["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PMR = PMR.append(table5)
                    
                    table6=pd.read_html(str(a[6]))[0]
                    table6["origen"] = OD.loc[O,"origen"]
                    table6["destino"] = OD.loc[O,"destino"]
                    table6["config_v"] = df.loc[x,"config_v"]
                    table6["tipo_carga"] = df.loc[x,"tipo_carga"]
                    table6["tipo_unidad"] = df.loc[x,"tipo_unidad"]
                    PML=PML.append(table6)
                    
                    driver.get(enlaces)
                    time.sleep(1)

# COD = pd.read_excel("Costos Operativos - Detalle.xlsx")
# PF = pd.read_excel("Parámetros de filtros.xlsx")
# PML = pd.read_excel("Parámetros de Lavado y Engrase.xlsx")
# PL = pd.read_excel("Parámetros de llantas.xlsx")
# PLu = pd.read_excel("Parámetros de lubricantes.xlsx")
COD = COD.drop(columns=([0,1,2,3,4,5]))
COD = COD.dropna()
PF = PF.drop(columns=([0,1,2,3,4,5]))
PF = PF.dropna()
PML = PML.drop(columns=([0,1,2,3,4,5]))
PML = PML.dropna()
PL = PL.drop(columns=([0,1,2,3,4,5]))
PL = PL.dropna()
PLu = PLu.drop(columns=([0,1,2,3,4,5]))
PLu = PLu.dropna()

COR.to_excel("Costos Operativos - Resumen.xlsx",index=False)
COD.to_excel("Costos Operativos - Detalle.xlsx",index=False)
PH.to_excel("Parámetros de la herramienta.xlsx",index=False)
PDC.to_excel("Parámetros distancias y combustible.xlsx",index=False)
PP.to_excel("Parámetros de peajes.xlsx",index=False)
PL.to_excel("Parámetros de llantas.xlsx",index=False)
PLu.to_excel("Parámetros de lubricantes.xlsx",index=False)
PF.to_excel("Parámetros de filtros.xlsx",index=False)
PMR.to_excel("Parámetros de Mantenimiento y Reparación.xlsx",index=False)
PML.to_excel("Parámetros de Lavado y Engrase.xlsx",index=False)




# CO = ["Costos Operativos - Detalle1.xlsx", "Costos Operativos - Detalle2.xlsx"]

# COR = ["Costos Operativos - Resumen1.xlsx", "Costos Operativos - Resumen2.xlsx"]

# PF = ["Parámetros de filtros1.xlsx","Parámetros de filtros2.xlsx"]

# PH=["Parámetros de la herramienta1.xlsx", "Parámetros de la herramienta2.xlsx"]

# PE=["Parámetros de Lavado y Engrase1.xlsx","Parámetros de Lavado y Engrase2.xlsx"]

# PLL = ["Parámetros de llantas1.xlsx","Parámetros de llantas2.xlsx"]

# PLu = ["Parámetros de lubricantes1.xlsx","Parámetros de lubricantes2.xlsx"]

# PMR = ["Parámetros de Mantenimiento y Reparación1.xlsx","Parámetros de Mantenimiento y Reparación2.xlsx"]

# PP=["Parámetros de peajes1.xlsx","Parámetros de peajes2.xlsx"]

# PDC = ["Parámetros distancias y combustible1.xlsx","Parámetros distancias y combustible2.xlsx"]


# def CoBases(lista):
#     for d in lista:
#         if lista[0] == d:
#             base=pd.read_excel(d)
#         else:
#             df = pd.read_excel(d)
#             base = base.append(df)
#     base.to_excel(re.sub(r'[0-9]+', '', lista[0]),index=False)
#     return base


# df = CoBases(CO)
# df = CoBases(COR)
# df = CoBases(PF)
# df = CoBases(PH)
# df = CoBases(PE)
# df = CoBases(PLL)
# df = CoBases(PLu)
# df = CoBases(PMR)
# df = CoBases(PP)
# df = CoBases(PDC)
