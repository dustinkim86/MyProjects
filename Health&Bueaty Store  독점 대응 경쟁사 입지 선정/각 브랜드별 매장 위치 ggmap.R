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