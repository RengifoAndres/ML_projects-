##### 
# Intro to web scraping in R using 
#  rvest
####


require(pacman) 

p_load(tidyverse, # contiene las librer?as ggplot, dplyr...
       rvest) # web-scraping


# First Steps with rvest

# rvest has several functions that can help us to .

# read_read_html 

my_url = "https://quotes.toscrape.com/"

# request el HTML de la p?gina a R. 
my_html = read_html(my_url) ## leer el html de la p?gina

##open the page
browseURL(my_url)

## obtengamos el titulo de la p?gina usando funciones simples de 
## rvest. 


div<- my_html %>% html_elements("div") %>%
  html_elements("a") %>%
  html_text2()

div[1]



quote<- my_html %>%
  html_elements(".quote")

quote[1]

tags <- my_html %>%
  html_elements(".tag")%>%
  html_text2()

tags[1]


tags <- my_html %>%
  html_elements(".tag")%>%
  html_text2()


### obtengamos los linnks de cada autor 

links<- my_html %>% 
  html_elements("a")%>%
  html_attr("href")

links[2]        

## pero obtenemos otros links que no deseamos

links<- my_html %>% 
  html_elements(".quote") %>%
  html_element("a")%>%  #note element no elements
  html_attr("href") 


links[1]



#####################
# GET TABLES FROM PAGES. 
#####################


## Example 1 ranking of the top 5% authors

my_url = "https://ideas.repec.org/top/top.person.nbcites.html"

### request the html 
browseURL(my_url)

my_html = read_html(my_url) ## leer el html de la p?gina

table<- my_html %>% 
  html_table()

table[[2]]


table<- as.data.frame(table[[2]])

ggplot(table, aes(x=Score))+
  geom_histogram()+ 
  theme_minimal()


## Example 2 Partidos de futbol  


my_url = "https://es.wikipedia.org/wiki/Anexo:Torneo_Apertura_2017_(Colombia)_-_Fase_todos_contra_todos"
browseURL(my_url)

### request the html 

my_html = read_html(my_url) ## leer el html de la p?gina

table<- my_html %>% 
  html_table()

### Recomendation: look at the end of the table list
##  



df<- as.data.frame(table[[1]] )


sf<- df %>%  filter(X1== "" ) %>%
  select(X5) 

str<- sf[1,1]

arbitro<- str_extract( str,  '?rbitro: .*'  ) %>%
  str_remove("?rbitro:")

df<- df %>% rename( "Fecha"= "X1", 
                    "Local"= "X2", 
                    "Marcador" = "X3",
                    "Visitante" ="X4", 
                    "Estadio"=  "X5") %>%
  filter(Fecha!= "" ) %>%
  select(-X6) %>%
  mutate(Arbtro= arbitro )


## ESTO NOS PIDE UN LOOP!!!!

## tenere cuidado con el item 66
df<- as.data.frame(table[[61]] )


df<- data.frame()

for (i in seq(1,length(table)-2 )) {
  
  df_temp<- as.data.frame(table[[i]] )
  
  df_temp <- slice(df_temp, 1:2)
  
  
  if (length(df_temp)== 7 ){
    
    df_temp <-df_temp %>%  select(-X7)
    
  }
  
  
  sf<- df_temp %>%  filter(X1== "" ) %>%
    select(X5) 
  
  str<- sf[1,1]
  
  arbitro<- str_extract( str,  '?rbitro: .*'  ) %>%
    str_remove("?rbitro:")
  
  df_temp<- df_temp %>%
    rename( "Fecha"= "X1", 
            "Local"= "X2", 
            "Marcador" = "X3",
            "Visitante" ="X4", 
            "Estadio"=  "X5") %>%
    filter(Fecha!= "" ) %>%
    select(-X6) %>%
    mutate(Arbtro= arbitro )
  
  
  df<- rbind(df, df_temp)
  print(i)
  
}


#### Ilustrando el uso de XPATH. 

### Primera p?gina

my_url = "https://quotes.toscrape.com/"

### request the html 

my_html = read_html(my_url) ## leer el html de la p?gina



quotes<-  my_html %>% 
  html_elements(xpath="//span[@class= 'text']") %>%
  html_text2()

author <-  my_html %>% 
  html_elements(xpath="//small[@class= 'author']") %>%
  html_text()



quotesdata<- data.frame(author= author,
                        quotes= quotes)




#######################################################
### scrapping pages that call info from another places
#######################################################

### ignacio Page
my_url = "https://ignaciomsarmiento.github.io/GEIH2018_sample/page1.html"


my_html = read_html(my_url) ## leer el html de la p?gina

table<- my_html %>% 
  html_table()


table
## does not work. Why?



win <- read_html("https://www.winsports.co/")
win %>%
  html_table()



p_load(jsonlite)
posiciones <- fromJSON("https://files-optafeeds-produccion-1.s3.amazonaws.com/positions/371/2023/all.json")
as.data.frame(posiciones) %>%
  View()

names(posiciones)

names(posiciones[["phases"]])
posiciones[["phases"]][["1041"]]

posiciones[["phases"]][["1093"]][["phase"]]

equipos <- posiciones[["phases"]][["1041"]][["teams"]]
length(equipos)

tabla_posiciones <- data.frame()
for (i in 1:length(equipos)) {
  nombre <- equipos[[i]]$name
  pos <- equipos[[i]]$pos
  pj <- equipos[[i]]$pj
  pg <- equipos[[i]]$pg
  pe <- equipos[[i]]$pe
  pp <- equipos[[i]]$pp
  pt <- equipos[[i]]$pt
  fila <- data.frame("Nombre" = nombre, "PJ" = pj, "PG" = pg, "PE" = pe, "PP" = pp, 
                     "Pts" = pt)
  tabla_posiciones <- bind_rows(tabla_posiciones, fila)
}







