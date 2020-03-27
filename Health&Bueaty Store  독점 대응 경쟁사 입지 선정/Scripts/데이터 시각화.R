library(ggmap)

# google map api
api_key <- 'your_api'
register_google(key = api_key)

# 각 브랜드별 매장 위치 데이터 load
olive <- read.csv('./store/서울시 올리브영 매장 위치.csv', header=T)
lobs <- read.csv('./store/서울시 롭스 매장 위치.csv', header=T)
lalavla <- read.csv('./store/서울시 랄라블라 매장 위치.csv', header=T)

# 구글 맵 load
map <- get_map(location='seoul, korea', zoom=11, maptype = 'roadmap', source='google')
g <- ggmap(map)

# map 위 각 브랜드 매장 위치 point
g <- g + geom_point(data=olive, aes(x=Longitude, y=Latitude), size=2, colour='darkgreen')
g <- g + geom_point(data=lobs, aes(x=Longitude, y=Latitude), size=2, colour='orange')
g <- g + geom_point(data=lalavla, aes(x=Longitude, y=Latitude), size=2, colour='darkred')
print(g)


# 시각화
person <- dplyr::select(datasets, id, dong, `총생활인구`, `여성10.30대인구`)

library(raster)
library(ggplot2)
# shp file load : raster library
seoul <- shapefile('서울시(행정동)경계_EPSG_5179.shp')
# shp file에는 좌표계가 없기 때문에 좌표계 설정
seoul <- spTransform(seoul, CRS("+proj=longlat"))
# fortify : shp file을 데이터프레임으로 바꿔주는 함수
seoul_map <- fortify(seoul)
# merge 함수이용하여 데이터셋과 병합
merge_ds <- merge(seoul_map, person, by='id')

x11()
# 행정동별 생활인구
str(merge_ds)
person_map <- ggplot() + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group, fill=총생활인구), color='gray')+ labs(fill='총 생활인구')
person_map + scale_fill_gradient(low='yellow', high='darkblue')
# 여성10~30대 생활인구
woman_map <- ggplot() + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group, fill=`여성10.30대인구`), color='gray')+
  labs(fill='여성 10~30대 생활인구')
woman_map + scale_fill_gradient(low='yellow', high='darkblue')

# merge 함수이용하여 데이터셋과 병합
merge_ds <- merge(seoul_map, datasets, by='id')
# 올리브영 분포
olive_map <- ggplot() + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group, fill=olive), color='gray')+labs(fill='올리브영')
olive_map + scale_fill_gradient(low='white', high='darkgreen')

# 랄라블라 분포
lalavla_map <- ggplot() + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group, fill=lalavla), color='gray')+labs(fill='랄라블라')
lalavla_map + scale_fill_gradient(low='white', high='darkred')

# 롭스 분포
lobs_map <- ggplot() + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group, fill=lobs), color='gray')+labs(fill='롭스')
lobs_map + scale_fill_gradient(low='white', high='orange')

# 브랜드 전체 분포
tot_store_map <- ggplot() + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group, fill=tot_store), color='gray')+labs(fill='H&B스토어 전체수')
tot_store_map + scale_fill_gradient(low='white', high='purple')

# 지하철역 수 분포
subway_map <- ggplot() + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group, fill=subway), color='gray')+labs(fill='지하철역 수')
subway_map + scale_fill_gradient(low='white', high='brown')

# 학교 수 분포
school_map <- ggplot() + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group, fill=school), color='gray')+labs(fill='학교 수')
school_map + scale_fill_gradient(low='white', high='blue')

seoul_google_map <- get_map(location='seoul', zoom=11, maptype='roadmap', color='bw')

# 올리브영 포인트 분포
ggmap(seoul_google_map) + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group), color='gray', alpha=.2) +
  geom_point(data=olive, aes(x=Longitude, y=Latitude), size=2.2, colour='darkgreen')

# 랄라블라 포인트 분포
ggmap(seoul_google_map) + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group), color='gray', alpha=.2) +
  geom_point(data=lalavla, aes(x=Longitude, y=Latitude), size=2.2, colour='darkred')

# 롭스 포인트 분포
ggmap(seoul_google_map) + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group), color='gray', alpha=.2) +
  geom_point(data=lobs, aes(x=Longitude, y=Latitude), size=2.2, colour='darkorange')

# 결측값 제거
na.omit(datasets)
# rent 데이터 숫자 변환
datasets$rent <- as.numeric(datasets$rent)
# merge 함수이용하여 데이터셋과 병합
merge_ds <- merge(seoul_map, datasets, by='id')

# 브랜드 전체 분포
rent_map <- ggplot() + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group, fill=rent), color='gray')+labs(fill='임대료')
rent_map + scale_fill_gradient(low='white', high='brown')

# 총생활인구/총매장 분포
store_per_person_map <- ggplot() + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group, fill=총생활인구_총매장), color='gray')+labs(fill='총생활인구/총매장')
store_per_person_map + scale_fill_gradient(low='white', high='darkblue')

# 브랜드 전체 분포
fg_map <- ggplot() + geom_polygon(data=merge_ds, aes(
  x=long, y=lat, group=group, fill=best_group), color='gray')
fg_map + scale_fill_gradient(low='white', high='lightblue')
