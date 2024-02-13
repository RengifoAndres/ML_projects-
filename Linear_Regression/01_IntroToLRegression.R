###### This is a introduction to linear Regression with R



library(pacman)


p_load(tidyverse, 
      rio)


### load the data

## we are going to use a subsample for GEIH

## load data
db <- import("https://github.com/ignaciomsarmiento/datasets/blob/main/GEIH_sample1.Rds?raw=true")
db <- as_tibble(db) %>% rename(gender=sex) 



# 

db_of<- db %>% 
  group_by(oficio, gender)  %>% 
  summarise(ofic_ingLab= mean(y_ingLab_m, na.rm=T), .groups="drop") %>%
  mutate(ofic_ingLab= ofic_ingLab/1000000)

db_of  %>% dplyr:: select(oficio, gender, ofic_ingLab) %>% head(4)