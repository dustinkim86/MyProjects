###########################################################
### malaria weather RM
###########################################################
library(randomForest)

mal_weather<-read.csv('weather_malaria_rate.csv')
str(mal_weather)

y_data01 <- mal_weather[,15]
str(y_data01)
range(y_data01) 
mal_weather_sub <- mal_weather[,-c(1,3,4,7,9,10,12,13,14,15)]

str(mal_weather_sub)

normalize <- function(x){
  return ((x-min(x))/(max(x)-min(x)))
}

mal_weather_nor <- as.data.frame(lapply(mal_weather_sub,normalize))
str(mal_weather_nor)

mal_weather2 <- cbind(mal_weather_nor,y_data01)
str(mal_weather2)

malaria_날씨_상관분석 <- randomForest(y_data01 ~., data=mal_weather2,mtree=500,mtry=2,importance = T)

varImpPlot(malaria_날씨_상관분석)



###########################################################
### sfts weather RM
###########################################################

sfts_weather<-read.csv('weather_sfts_rate.csv')
head(sfts_weather)
str(sfts_weather)

y_data03 <- sfts_weather[,15]
str(y_data03)
range(y_data03) # 0.00 0.39
sfts_weather_sub <- sfts_weather[,-c(1,3,4,7,9,10,12,13,14,15)]

str(sfts_weather_sub)

sfts_weather_nor <- as.data.frame(lapply(sfts_weather_sub,normalize))
str(sfts_weather_nor)

sfts_weather2 <- cbind(sfts_weather_nor,y_data03)
str(sfts_weather2)

sfts_날씨_상관분석 <- randomForest(y_data03 ~., data=sfts_weather2,mtree=500,mtry=2,importance = T)

varImpPlot(sfts_날씨_상관분석)



###########################################################
### tsursu weather RM
###########################################################

tsutsu_weather<-read.csv('weather_tsutsu_rate.csv')
head(tsutsu_weather)
str(tsutsu_weather)

y_data04 <- tsutsu_weather[,15]
str(y_data04)
range(y_data04) # 0.00 20.76
tsutsu_weather_sub <- tsutsu_weather[,-c(1,3,4,7,9,10,12,13,14,15)]

str(tsutsu_weather_sub)

tsutsu_weather_nor <- as.data.frame(lapply(tsutsu_weather_sub,normalize))
str(tsutsu_weather_nor)

tsutsu_weather02 <- cbind(tsutsu_weather_nor,y_data04)
str(tsutsu_weather02)

tsutsu_날씨_상관분석 <- randomForest(y_data04 ~., data=tsutsu_weather02,mtree=500,mtry=2,importance = T)

varImpPlot(tsutsu_날씨_상관분석)
