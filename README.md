# Iris

## 【GeoIP】
For visualizing the frequency of occurrence of "Probe_dst_prefix" and "Reply_src_addr", I used "choropleth maps" in Python with Plotly.

Choropleth maps in Python  
https://plotly.com/python/choropleth-maps/

I converted the log file of Iris dataset to another excel file of frequency of occurrence per country.

Column 01 : Time / Collection time  
Column 02 : Country / Country name by ISO3 (Country name represented by 3 letters)  
Column 03 : Frequency of occurrence / Frequency of occurrence of Probe_dst_prefix or Reply_src_addr  

Country codes by alpha-2 & alpha-3  
https://www.iban.com/country-codes


## 【predict】

Name : (Variables)_(What to predict)  

pdp_ttl : predict probe_ttl based on probe_dst_prefix   
rsa_ttl : predict probe_dst_prefix based on reply_src_addr   
pdp_rsa : predict reply_src_addr based on probe_dst_prefix    
rsa_pdp : predict probe_dst_prefix based on reply_src_addr  


## 【result】

Result File of  
probe_dst_prefix  
reply_src_addr  
probe_ttl  

## 【data】
Iris dataset collected for 1 week.  
The collection interval is 100,000 data per hour.  

2022/10/25 11:00 ~ 2022/11/1 10:00 (JST)

Filename : log_Year_Month_Day_Hour.xlsx

Column 01 : probe_src_addr  
Column 02 : probe_dst_prefix  
Column 03 : probe_ttl  
Column 04 : reply_src_addr  


## 【output】
test program for accessing Iris dataset
