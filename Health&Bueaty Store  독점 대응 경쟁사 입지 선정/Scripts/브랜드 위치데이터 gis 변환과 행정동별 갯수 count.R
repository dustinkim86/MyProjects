# dataframe 데이터를 gis 데이터 형태로 변환 해주는 library
library(GISTools)
library(raster)
library(maptools)

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