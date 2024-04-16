#통계생성
import pandas as pd
import gc
gc.collect()
pd.set_option('float_format', ':.2f'. format)

####### SKT rst_hang_form_people_cust_info_0905_total_trmn_idx_f_live_1 START ########

df_skt1 = pd.read_csv(/data/combine/2023/hangan/output/kt/rst_hang_form_people_cust_info_0905_total_trmn_idx_f_live_1.csv') # LGU
df cross1 = pd.crosstab(index = [df_skt1.], columns = 'count', margins=True, margins_name= '') df_cross2 = pd.crosstab(index = [df_skt1.8], columns = 'count', margins=True, margins_name= '')
df cross3 = pd.crosstab(index = [df_skt1.47), columns = 'count', margins=True, margins_name= '') df cross4 = pd.crosstab(index = [df_skt1.25], columns = 'count', margins=True, margins_name='') df cross5= pd.crosstab(index = [df_skt1.9], columns = 'count', margins=True, margins_name= '') df cross6 = pd.crosstab(index = [df_skt1.01), columns = 'count', margins=True, margins_name= '') df cross7= pd.crosstab(index = [df_skt1.FORN_DIV], columns = 'count', margins=True, margins_name = '') df cross8= pd.crosstab(index = [df_skt1.ETL_YMD], columns = 'count', margins=True, margins_name = '') df cross9 = pd.crosstab(index = [df_skt1.REGION_DIV], columns = 'count', margins=True, margins_name = '')
df cross10= pd.crosstab(index = [df_skt1.ADMDONG_CD], columns = 'count', margins=True, margins_name= df cross11 pd.crosstab(index = [df_skt1.2], columns = 'count', margins=True, margins_name= '') df cross12 = pd.crosstab(index = [df_skt1.], columns = 'count', margins=True, margins_name = '')
=
df cross1.sort_values(by=['']).to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats1.csv") df cross2.sort_values(by=['']).to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats2.csv") df cross3.sort_values(by=['']).to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats3.csv") df cross4.sort_values(by=['']).to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats4.csv") df cross5.sort_values(by=['']).to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats5.csv") df cross6.sort_values(by=['']).to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats6.csv") df cross7.sort_values(by=[]).to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats7.csv") df cross8.sort_values(by=['']).to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats8.csv") df cross9.sort_values(by=['']).to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats9.csv") df cross10.sort_values(by=['']).to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats10.csv") df cross11.sort_values(by=['']).to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats11.csv") df cross12.sort_values(by=[').to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats12.csv") #연속형 변수
df_skt1.describe().to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats_desc.csv") # desc

#4분위수
## 1. TOTAL_TIME
q3= df_skt1['TOTAL_TIME'].quantile (0.75)
q1= df_skt1['TOTAL_TIME'].quantile (0.25)
iqr=q3-q1
df_upper = df_skt1 [df_skt1 ['TOTAL_TIME']> (q3+ 1.5* iqr)]
df_under = df_skt1 [df_skt1 ['TOTAL_TIME'] < (q1 - 1.5 * iqr)]
df_upper.to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats_TOTAL_TIME_upper.csv") #upper df_under.to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats_TOTAL_TIME_under.csv") #under
del [[q1, q3, iqr, df_upper, df_under]] gc.collect()

## 2. YM_STD_TIME

q3= df_skt1['YM_STD_TIME'].quantile (0.75)
q1= df_skt1['YM_STD_TIME'].quantile(0.25)
iqr=q3-q1
df_upper = df_skt1 [df_skt1['YM_STD_TIME] > (q3+ 1.5* iqr)]
df_under = df_skt1[df_skt1['YM_STD_TIME] < (q1 1.5* iqr)]
df_upper.to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats_YM_STD_TIME_upper.csv") #upper df_under.to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats_YM_STD_TIME_under.csv") #under
del [[q1, q3, iqr, df_upper, df_under]] gc.collect0

## 3. D_STD_TIME

q3= df_skt1['D_STD_TIME'].quantile(0.75)
q1= df_skt1['D_STD_TIME'].quantile(0.25)
iqr=q3-q1
df_upper = df_skt1 [df_skt1 ['D_STD_TIME'] > (q3 + 1.5 * iqr)] df_under = df_skt1 [df_skt1['D_STD_TIME] < (q1 - 1.5* iqr)]
df_upper.to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats_D_STD_TIME_upper.csv") #upper df_under.to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats_D_STD_TIME_under.csv") #under
del [[q1, q3, iqr, df_upper, df_under]] 
gc.collect()

## 4. N_STD_TIME

q3= df_skt1['N_STD_TIME'].quantile (0.75)
q1= df_skt1['N_STD_TIME'].quantile (0.25)
iqr = q3-q1
df_upper = df_skt1 [df_skt1['N_STD_TIME] > (q3+ 1.5 * iqr)]
df_under = df_skt1 [df_skt1['N_STD_TIME] < (q1 - 1.5* iqr)]

df_upper.to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats_N_STD_TIME_upper.csv") #upper df_under.to_csv("/data/combine/2023/hangan/output/kt/stats/rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1_stats_N_STD_TIME_under.csv") #under

del [[q1, q3, iqr, df_upper, df_under]]
gc.collect()
#메모리해제
del [[df_cross1,df_cross2,df_cross3,df_cross4,df_cross5,df_cross6,df_cross7,df_cross8, df_cross9,df_cross 10, df_skt1]] 
gc.collect()
##### rst_hang_forn_people_cust_info_0905_total_trmn_idx_f_live_1 END