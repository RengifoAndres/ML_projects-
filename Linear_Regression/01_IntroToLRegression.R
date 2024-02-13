###### This is a introduction to linear Regression with R



library(pacman)


p_load(tidyverse, 
       skimr,
      rio)

### load the data

## we are going to use a subsample for GEIH

## load data
db <- import("https://github.com/ignaciomsarmiento/datasets/blob/main/GEIH_sample1.Rds?raw=true")

db <- as_tibble(db) %>% rename(gender=sex) %>%
                        rename(ocupation= oficio)



db_of<- db %>% 
  group_by(oficio, gender)  %>% 
  summarise(ofic_ingLab= mean(y_ingLab_m, na.rm=T), .groups="drop") %>%
  mutate(ofic_ingLab= ofic_ingLab/1000)

db_of  %>% dplyr:: select(ocupation, gender, ofic_ingLab) %>% head(4)

## merge with the original data set

db_int <- db %>% inner_join(db_of, by=c("oficio", "gender"))

# child indicator
db_int <- db_int %>%
  mutate(flag = ifelse(age <= 18, 1, 0))

#  total number of children per household

db_int <- db_int %>%
  group_by(directorio, secuencia_p) %>%
  mutate(nmenores = sum(flag)) %>%
  dplyr::select(-flag) %>% 
  ungroup()


db_int %>% dplyr:: select(directorio, secuencia_p, age , nmenores ) %>% tail()

db_int <- db_int %>%
  mutate(H_Head = ifelse( p6050== 1, 1, 0))

table(db_int$H_Head)




features<- c("ofic_ingLab", "nmenores",  "H_Head",  "age",  "gender" )

db_int<- db_int %>% drop_na(any_of(features))


## Regression
linear_model<- lm(totalHoursWorked ~ ofic_ingLab + nmenores  +  nmenores*gender + H_Head + age + gender + I(age^2) , data=db_int  )
summary(linear_model)





