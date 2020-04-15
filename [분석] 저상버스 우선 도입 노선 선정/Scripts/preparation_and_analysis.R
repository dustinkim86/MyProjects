library(plyr)
library(dplyr)
library(readr)


#--------------------#
#  Data Preparation  #
#--------------------#

### 데이터 정제 ###

# 장애인 관광지 정보
dis_site_2<-read.csv("disabled_site_filtered.csv", stringsAsFactors = F)
str(dis_site_2)
table(is.na(dis_site_2))

#dis_site_2$X_VAL<-as.double(dis_site_2$X_VAL)
#dis_site_2$Y_VAL<-as.double(dis_site_2$Y_VAL)

dis_site_2_points<- dis_site_2 %>% group_by(ROAD_ADDR) %>% 
  summarise(X_VAL = mean(X_VAL), Y_VAL = mean(Y_VAL))

#write.csv(dis_site_2_points, "disabled_site_filtered_points.csv", row.names = F)


#-------빅데이터캠퍼스 내부 작업----------#

# 복지카드 데이터 반출 작업

# 거주지
dis_resid<-read.csv("원데이터/03. 장애인 복지카드 이용현황/2. 파일데이터/장애인복지카드이용현황/장애인_거주지_분석용.csv", stringsAsFactors=F)
str(dis_resid)

length(unique(dis_resid$residence)) # 11553

as.character(dis_resid$residence[which(dis_resid$disabled_cnt == max(dis_resid$disabled_cnt))])

dis_resid$disabled_cnt %>% head
dis_resid$disabled_cnt[60:65]


# 소비지
dis_spend<-read.csv("원데이터/03. 장애인 복지카드 이용현황/2. 파일데이터/장애인복지카드이용현황/장애인_거주지소비지_분석용.csv", stringsAsFactors=F)
str(dis_spend)

length(unique(dis_spend$spend)) # 10848

dis_spend_2<-dis_spend %>% group_by(spend) %>% 
  summarise(dis_spend_cnt=sum(disabled_cnt))
str(dis_spend_2)
dis_spend_2 <- as.data.frame(dis_spend_2)

#write.csv(dis_spend_2, "dis_spend_count.csv", row.names = F)

max(dis_spend_2$dis_spend_cnt) # 8795
as.character(dis_spend_2$spend[which(dis_spend_2$dis_spend_cnt == max(dis_spend_2$dis_spend_cnt))])

dis_spend_masked<-dis_spend_2 %>% 
  mutate( masked_spend_cnt = dis_spend_cnt/max(dis_spend_2$dis_spend_cnt))
str(dis_spend_masked)

dis_spend_masked<-dis_spend_masked[-2]

#write.csv(dis_spend_masked, "dis_spend_masked.csv", row.names = F)


# 생활인구

#getwd()
#setwd("E:/원데이터/43. 생활인구/2. 파일데이터/내국인")

spop_func<-function(dir_nm, df_nm){
  filelist = list.files(pattern=".txt")

  file_first <- read.csv(filelist[1], sep="|", quote="\`")
  file_first<-file_first[,c(1,3,4,6,22,18:21,34:37)]
  col_first <- colnames(file_first)

  first_sum <- file_first %>% 
    mutate(under9 = rowSums(.[4:5]), over65 = rowSums(.[6:13])) %>% 
    group_by(stdr_de_id, adstrd_code_se, oa_cd) %>% 
    summarise(under9 = sum(under9), over65 = sum(over65))

  df <- as.data.frame(first_sum)

  for (i in 2:length(filelist)){
    tmp <- read.csv(filelist[i], sep="|", quote="\`", header=F)
    tmp_s <- tmp[,c(1,3,4,6,22,18:21,34:37)]
  
    colnames(tmp_s) <- col_first
  
    tmp_g <- tmp_s %>% 
      mutate(under9 = rowSums(.[4:5]), over65 = rowSums(.[6:13])) %>% 
      group_by(stdr_de_id, adstrd_code_se, oa_cd) %>% 
      summarise(under9 = sum(under9), over65 = sum(over65))
  
    df<-rbind(df, as.data.frame(tmp_g))
  
  }

  df_tmp <- df %>% group_by(stdr_de_id, adstrd_code_se, oa_cd) %>%
    summarise(under9 = sum(under9), over65 = sum(over65))

  colnames(df_tmp)[c(1:3)] <- c("date","adong","jip_cd")

  file_nm <- paste("'", df_nm, ".csv'", sep="")
  write.csv(df_tmp, file_nm, row.names = F)
  names(df_tmp)<-df_nm
  return(df_nm)

}


spop_func("../201810/line_break", 'spop1810')
spop_func("../201812/line_break", 'spop1812')
spop_func("../201902/line_break", 'spop1902')
spop_func("../201904/line_break", 'spop1904')
spop_func("../201908/line_break", 'spop1908')


spop_func_2<-function(dir_nm, df_nm){
  filelist = list.files(pattern=".txt")

  file_first <- read.csv(filelist[1], sep="|", quote="\`", skip = 1, header=F)
  file_first<-file_first[,c(1,3,4,6,22,18:21,34:37)]
  colnames(file_first)[c(1:3)] <- c("stdr_de_id", "adstrd_code_se", "oa_cd")

  first_sum <- file_first %>% 
    mutate(under9 = rowSums(.[4:5]), over65 = rowSums(.[6:13])) %>% 
    group_by(stdr_de_id, adstrd_code_se, oa_cd) %>% 
    summarise(under9 = sum(under9), over65 = sum(over65))

  df <- as.data.frame(first_sum)

  for (i in 2:length(filelist)){
    tmp <- read.csv(filelist[i], sep="|", quote="\`", header=F)
    tmp_s <- tmp[,c(1,3,4,6,22,18:21,34:37)]
    
    tmp_g <- tmp_s %>% 
      mutate(under9 = rowSums(.[4:5]), over65 = rowSums(.[6:13])) %>% 
      group_by(stdr_de_id, adstrd_code_se, oa_cd) %>% 
      summarise(under9 = sum(under9), over65 = sum(over65))
  
    df<-rbind(df, as.data.frame(tmp_g))
  
  }

  df_tmp <- df %>% group_by(stdr_de_id, adstrd_code_se, oa_cd) %>%
    summarise(under9 = sum(under9), over65 = sum(over65))

  colnames(df_tmp)[c(1:3)] <- c("date","adong","jip_cd")

  file_nm <- paste("'", df_nm, ".csv'", sep="")
  write.csv(df_tmp, file_nm, row.names = F)
  names(df_tmp)<-df_nm

}


spop_func_2("../201906/line_break", 'spop1906')


sm1810 <-spop1810 %>% group_by(jip_cd) %>% summarise(under9=mean(under9), over65=mean(over65))
str(sm1810)

sm1812 <-spop1812 %>% group_by(jip_cd) %>% summarise(under9=mean(under9), over65=mean(over65))
str(sm1812)

sm1902 <-spop1902 %>% group_by(jip_cd) %>% summarise(under9=mean(under9), over65=mean(over65))
str(sm1902)

sm1904 <-spop1904 %>% group_by(jip_cd) %>% summarise(under9=mean(under9), over65=mean(over65))
str(sm1904)

sm1906 <-spop1906 %>% group_by(jip_cd) %>% summarise(under9=mean(under9), over65=mean(over65))
str(sm1906)

sm1908 <-spop1908 %>% group_by(jip_cd) %>% summarise(under9=mean(under9), over65=mean(over65))
str(sm1908)


sm1810$st1810<-sm1810$under9+sm1810$over65
sm1812$st1812<-sm1812$under9+sm1812$over65
sm1902$st1902<-sm1902$under9+sm1902$over65
sm1904$st1904<-sm1904$under9+sm1904$over65
sm1906$st1906<-sm1906$under9+sm1906$over65
sm1908$st1908<-sm1908$under9+sm1908$over65

# 전체
tmp1<-merge(sm1810[,c(1,4)], sm1812[,c(1,4)], by='jip_cd')
tmp2<-merge(tmp1, sm1902[,c(1,4)], by='jip_cd')
tmp3<-merge(tmp2, sm1904[,c(1,4)], by='jip_cd')
tmp4<-merge(tmp3, sm1906[,c(1,4)], by='jip_cd')
tmp5<-merge(tmp4, sm1908[,c(1,4)], by='jip_cd')
str(tmp5)

spopmean<-rowMeans(tmp5[,c(2:7)])

df<-data.frame(tmp5$jip_cd, spopmean)
colnames(df)<-c('jip_cd', '19year_mean_young_old')
str(df)

#write.csv(df, 'spop19mean.csv', row.names = F)

# 아동
tmp1<-merge(sm1810[,c(1,2)], sm1812[,c(1,2)], by='jip_cd')
tmp2<-merge(tmp1, sm1902[,c(1,2)], by='jip_cd')
tmp3<-merge(tmp2, sm1904[,c(1,2)], by='jip_cd')
tmp4<-merge(tmp3, sm1906[,c(1,2)], by='jip_cd')
tmp5<-merge(tmp4, sm1908[,c(1,2)], by='jip_cd')
str(tmp5)

und9<-rowMeans(tmp5[,c(2:7)])
length(und9)

und9 %>% head()

und_pop<-data.frame(tmp5$jip_cd, und9)
colnames(und_pop)[1]<-"jip_cd"

# 노인
tmp1<-merge(sm1810[,c(1,3)], sm1812[,c(1,3)], by='jip_cd')
tmp2<-merge(tmp1, sm1902[,c(1,3)], by='jip_cd')
tmp3<-merge(tmp2, sm1904[,c(1,3)], by='jip_cd')
tmp4<-merge(tmp3, sm1906[,c(1,3)], by='jip_cd')
tmp5<-merge(tmp4, sm1908[,c(1,3)], by='jip_cd')
str(tmp5)

ov65<-rowMeans(tmp5[,c(2:7)])
length(ov65)
ov65 %>% head()

ov_pop<-data.frame(tmp5$jip_cd, ov65)
colnames(ov_pop)[1]<-"jip_cd"
str(ov_pop)

df<-read.csv("spop19mean.csv", stringsAsFactors = F)
str(df)

tmp_df <- merge(df, und_pop, by='jip_cd')
tmp_df_2<- merge(tmp_df, ov_pop, by='jip_cd')
str(tmp_df_2)


colnames(tmp_df_2)[1] <- "TOT_REG_CD"
str(tmp_df_2)

s_tmp<-merge(total_set, tmp_df_2, by="TOT_REG_CD", all.x=T)
str(s_tmp) # 24195

#write.csv(s_tmp, "popmergedata.csv", row.names = F)
str(s_tmp)

# 합계
s_tmp_rs<-rowSums(s_tmp[,c(13:19,21)])
length(s_tmp_rs)

length(unique(s_tmp[,]))

str(total_set_id)
str(tmp_df)

total_pop_id<-merge(total_set_id, tmp_df[,c(1,3)], by="TOT_REG_CD", all.x=T)
str(total_pop_id)

length(unique(total_pop_id$rec_id))

tot_id_rs<-rowSums(total_pop_id[,c(13:19,21)])

res_df<-data.frame(rec_id=total_pop_id$rec_id, score=tot_id_rs)

str(res_df)
#write.csv(res_df, "res_df_2.csv", row.names = F)



#------------------------------------------#


total_tmp <- read.csv("total_dataset/total_dataset_7.csv", stringsAsFactors = F)
str(total_tmp)

total_tmp_id <- total_tmp %>% mutate(rec_id=row_number())
str(total_tmp_id)
#write.csv(total_tmp_id, "total_7_id.csv", row.names = F)


# 복지카드 거주지 데이터 복구

dis_resid<-read.csv("복지카드 거주지 데이터/reg_cd_dp_person.csv", stringsAsFactors=F)
str(dis_resid)

re_tmp<-dis_resid$disabled_cnt * 92
re_tmp %>% head()
recovered_dr<-data.frame(residence = dis_resid$residence, disabled_cnt = re_tmp)
str(recovered_dr)
#write.csv(recovered_dr, "recovered_dis_card_resid.csv", row.names = F)


# 복지카드 소비지 데이터 복원

dis_card_spnd<-read.csv("dis_spend_masked.csv", stringsAsFactors = F, encoding = "utf-8")
str(dis_card_spnd)

recovered_sp<-dis_card_spnd$masked_spend_cnt*8795
as.character(dis_card_spnd$spend[which(dis_card_spnd$masked_spend_cnt==1)])

rec_d_s<-data.frame(TOT_REG_CD=dis_card_spnd$spend, dis_spend_cnt=recovered_sp)
#write.csv(rec_d_s, "disabled_card_spend.csv", row.names = F)


# 생활인구 복구 1 

res_df<-read.csv("res_df.csv", stringsAsFactors = F, encoding='utf-8')
str(res_df)
str(total_tmp_id)

tot_spop<-merge(total_tmp_id, res_df, by='rec_id')
str(tot_spop)

#tot_spop$score %>%head(50)
#res_df$score %>% head(30) 
#res_df$score[res_df$rec_id==10]

minus<-rowSums(tot_spop[14:20]) # 생활인구 제외 7열 카운트 수치
spop<-tot_spop$score-minus # 순수 생활인구 수
tot_spop$spop <-spop

str(tot_spop)

colnames(tot_spop)[22] <- "생활인구_노인_아동"
tot_spop<-tot_spop[-21]

#write.csv(tot_spop, "total_with_spop.csv", row.names = F)

# 생활인구 복원 2 ; 아동+노인 수치에서 아동 빼서 노인 수치 도출

res_df_2 <- read.csv("res_df_2.csv", stringsAsFactors = F)
str(res_df_2)
str(tot_spop)

red_df_tmp<-merge(tot_spop, res_df_2, by="rec_id")
str(red_df_tmp)

red_df_tmp_2 <- red_df_tmp %>% 
  mutate( spop_under9 = score - rowSums(red_df_tmp[,c(14:20)]))
str(red_df_tmp_2)

red_df_tmp_3<-red_df_tmp_2 %>% 
  mutate(spop_over65 = 생활인구_노인_아동-spop_under9)
str(red_df_tmp_3)

#write.csv(red_df_tmp_3[,c(2:13,23,24)], "bus_spop.csv", row.names = F)


## Final Data Set ##

tot_5<-read.csv("total_dataset/tot_dataset_ver005_2.csv", stringsAsFactors = F, encoding="utf-8")
str(tot_5)
colnames(tot_5)[13]<-"직업재활시설_cnt"
tot_tmp<-tot_5

for(i in 13:18){
  tot_tmp[is.na(tot_tmp[i]),i]<-as.integer(0)
}

str(tot_tmp)



# 복지카드 데이터 추가

# 거주지
str(recovered_dr)
colnames(recovered_dr)[1] <- "TOT_REG_CD"

join_tmp<-join(tot_tmp, recovered_dr)
join_tmp$disabled_cnt[is.na(join_tmp$disabled_cnt)]<-as.numeric(0)

colnames(join_tmp)[21] <- "장애인인구"
str(join_tmp)


# 소비지
str(rec_d_s)

join_tmp_2<-join(join_tmp, rec_d_s)
str(join_tmp_2)

join_tmp_2$dis_spend_cnt[is.na(join_tmp_2$dis_spend_cnt)]<-as.numeric(0)
str(join_tmp_2)

colnames(join_tmp_2)[22]<-"복지카드소비지_cnt"
str(join_tmp_2)

tot_fin<-join_tmp_2[c(1:12,22,17,13,15,18,14,16,21,20,19)]
str(tot_fin)

#write.csv(tot_fin, "total_set_final.csv", row.names = F)







#---------------#
#  Calc & rank  #
#---------------#



tot_seoul<-tot_fin[!is.na(tot_fin$TOT_REG_CD),]
str(tot_seoul)

#write.csv(tot_seoul, "total_final_seoul.csv", row.names = F)

tot_seoul$dis_fac_score<-rowSums(tot_seoul[c(13:15)])
tot_seoul$fac_score<-rowSums(tot_seoul[c(16:19)])
bus_line_tmp<-tot_seoul[c(1,2,23,24,20:22)]
str(bus_line_tmp)
colnames(bus_line_tmp)<-c("LINE_ID","LINE_NM","dis_fac","fac","dis_pop","old_pop","kid_pop")
bus_line_tmp<-bus_line_tmp[c(1:5,7,6)]
str(bus_line_tmp)

#write.csv(bus_line_tmp, "bus_line_score_1.csv", row.names = F)



bus_scaled<-bus_line_tmp %>% mutate( dis_pop = scale(dis_pop),
                                     dis_fac = scale(dis_fac),
                                     kid_pop = scale(kid_pop),
                                     old_pop = scale(old_pop),
                                     fac = scale(fac))


bus_score <- bus_scaled %>% 
  mutate(score = (dis_pop*2) + (dis_fac*1.75) + (kid_pop*1.5) + (old_pop*1.25) + fac)

bus_score <- as.data.frame(bus_score)
str(bus_score)

#write.csv(bus_score, "bus_score.csv", row.names = F)


bs_g <- bus_score %>% group_by(LINE_ID, LINE_NM) %>% 
  summarise(score_mean=mean(score))
bs_g <- as.data.frame(bs_g)
bs_rank<-bs_g[order(bs_g$score, decreasing = T),]

#write.csv(bs_rank, "bus_line_score_rank.csv", row.names=F)




# further results

# 상위 5개 노선 정보
bus_sc <- bus_score
bus_sc$rec_id <- rownames(bus_sc)
str(bus_sc)

bus_201<-bus_sc[which(bus_sc$LINE_NM=="201"),]
bus_162<-bus_sc[which(bus_sc$LINE_NM=="162"),]
bus_4419<-bus_sc[which(bus_sc$LINE_NM=="4419"),]
bus_501<-bus_sc[which(bus_sc$LINE_NM=="501"),]
bus_333<-bus_sc[which(bus_sc$LINE_NM=="333"),]

stop_201<-as.data.frame(bus_201[order(bus_201$score),] %>% tail(10))$rec_id
stop_162<-as.data.frame(bus_162[order(bus_162$score),] %>% tail(10))$rec_id
stop_4419<-as.data.frame(bus_4419[order(bus_4419$score),] %>% tail(10))$rec_id
stop_501<-as.data.frame(bus_501[order(bus_501$score),] %>% tail(10))$rec_id
stop_333<-as.data.frame(bus_333[order(bus_333$score),] %>% tail(10))$rec_id

tot_b<-tot_fin
tot_b$rec_id <- rownames(tot_b)

tot_201<-tot_b[tot_b$rec_id %in% stop_201,]
tot_162<-tot_b[tot_b$rec_id %in% stop_162,]
tot_4419<-tot_b[tot_b$rec_id %in% stop_4419,]
tot_501<-tot_b[tot_b$rec_id %in% stop_501,]
tot_333<-tot_b[tot_b$rec_id %in% stop_333,]



# 장애인 인구수 상위 행정동
tot_fin <- read.csv("total_set_final.csv", stringsAsFactors = F)
str(tot_fin)

dis_resid_dong<-as.data.frame(tot_fin %>% group_by(ADM_CD, ADM_NM) %>% 
                                summarise(resid = sum(복지카드소비지_cnt)))
str(dis_resid_dong)
#write.csv(dis_resid_dong, "dis_resid_dong.csv", row.names = F)

dis_resid_dong<-read.csv("dis_resid_dong.csv", stringsAsFactors = F)
str(dis_resid_dong)

dis_resid_dong[order(dis_resid_dong$resid),] %>% tail()


# 생활인구 행정동별 순위 -- 정류장 기준으로 반출하여 데이터 불충분 -- 외부데이터활용

spop<-read_csv("LOCAL_PEOPLE_DONG_201909_2.csv")

spop %>% head()

livi<-read_csv("living_person.csv")
str(livi)

spop_dong<-as.data.frame(spop %>% group_by(행정동코드) %>% 
  summarise(under9 = mean(under9), over65 = mean(over65)))

colnames(spop_dong)[1]<-'ADMI_CD'
str(spop_dong)

spop_dong_name <- join(spop_dong, livi[c(2,3)], by='ADMI_CD', match='first')

# 아동 생활인구 행정동별 순위
as.data.frame(spop_dong_name[order(spop_dong_name$under9, decreasing = T),] %>% head(5))[c(2,4)]
#       under9 ADMI_NM
# 375 6199.452  세곡동
# 192 6194.447  진관동
# 274 5940.756 오류2동
# 403 5219.485 잠실3동
# 400 5062.801  위례동

# 노인 생활인구 행정동별 순위
as.data.frame(spop_dong_name[order(spop_dong_name$over65, decreasing = T),] %>% head(5))[c(3,4)]
#        over65         ADMI_NM
# 288 11115.676          여의동
# 9   10673.422 종로1.2.3.4가동
# 192 10610.408          진관동
# 422  9298.694            길동
# 82   9036.378          제기동


