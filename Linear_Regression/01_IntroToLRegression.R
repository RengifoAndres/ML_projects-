###### This is a introduction to linear Regression with R



library(pacman)


p_load(tidyverse, 
      skim)


### load the data

## we are going to use a subsample for GEIH

## load data
db <- import("https://github.com/ignaciomsarmiento/datasets/blob/main/GEIH_sample1.Rds?raw=true")
db <- as_tibble(db) %>% rename(gender=sex) 



