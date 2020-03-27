# dataframe 데이터를 gis 데이터 형태로 변환 해주는 library
library(GISTools)
library(raster)
library(maptools)

# 각 브랜드별 매장 위치 데이터 load
olive <- read.csv('./store/서울시 올리브영 매장 위치.csv', header=T)
lobs <- read.csv('./store/서울시 롭스 매장 위치.csv', header=T)
lalavla <- read.csv('./store/서울시 랄라블라 매장 위치.csv', header=T)

# shpfile load
seoul_shp <- shapefile('서울시(행정동)경계_EPSG_5179.shp')
# shpfile epsg 변경
seoul_shp <- spTransform(seoul_shp, CRS("+init=epsg:4326"))

# 기존 shpfile의 형태 check
proj4string(seoul_shp)

# 좌표데이터 -> gis 형태로 변환
# 올리브영
olive_coord <- olive
coordinates(olive_coord) = ~Longitude+Latitude
proj4string(olive_coord) <- CRS("+init=epsg:5179 +proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0")
# Count polygon in points
cnt <- poly.counts(olive_coord, seoul_shp)
cnt2 <- as.data.frame(cnt)
str(cnt2)
cnt2$dong <- seoul_shp$ADM_NM

# 학교
school_coord <- school
coordinates(school_coord) = ~Longitude+Latitude
proj4string(school_coord) <- CRS("+init=epsg:4326 +proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0")
cnt3 <- poly.counts(school_coord, seoul_shp)
cnt4 <- as.data.frame(cnt3)
cnt4$dong <- seoul_shp$ADM_NM

# 올리브영 count 통합
cnt4$olive <- cnt2$cnt

# 랄라블라
lala_coord <- lalavla
coordinates(lala_coord) = ~Longitude+Latitude
proj4string(lala_coord) <- CRS("+init=epsg:4326 +proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0")
# Count polygon in points
cnt <- poly.counts(lala_coord, seoul_shp)
cnt2 <- as.data.frame(cnt)
cnt4$lalavla <- cnt2$cnt

# 롭스
lobs_coord <- lobs
coordinates(lobs_coord) = ~Longitude+Latitude
proj4string(lobs_coord) <- CRS("+init=epsg:4326 +proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0")
# Count polygon in points
cnt <- poly.counts(lobs_coord, seoul_shp)
cnt2 <- as.data.frame(cnt)
cnt4$lobs <- cnt2$cnt

# 파일 중간저장
write.csv(cnt4, 'analysis.csv')

library(dplyr)
# file load
df <- read.csv('analysis.csv', header=T)
df <- select(df, dong, olive, lalavla, lobs, school)



# 임대료 데이터 load
rent <- read.csv('rent.csv', header=T)
head(rent)

# 같은 행정동의 평균임대료 데이터 insert
for (i in 1:NROW(df)) {
  for (j in 1:NROW(rent)) {
    if(df[i,1] == rent[j,2]){
      df[i,6] <- rent[j,3]
    }
  }
}
# column 이름 변경
cols <- colnames(df)
cols[6] <- 'rent'
names(df) <- cols

# 지하철역 데이터 load
subway <- read.csv('subway.csv', header = T)
subway
head(subway)

# 행정동코드 데이터 load
dong_code <- read.csv('dong_code2.csv', header=T)
dong_code
str(dong_code)
names(dong_code) <- c('dong_codes', 'sido','na','sigungu','dong','days','na2')
codes <- dong_code[,1]
dong2 <- dong_code[,5]
dong_codes <- data.frame(codes, dong2)
dong_codes
head(dong_codes)
dong_codes$codes <- dong_codes$codes/100
names(dong_codes) <- c('행정동코드', '행정동명')

# 데이터 중간 저장
write.csv(dongpop2, 'floatpop.csv')