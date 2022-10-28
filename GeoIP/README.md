# 【GeoIP】
For visualizing the frequency of occurrence of "Probe_dst_prefix" and "Reply_src_addr", I used "choropleth maps" in Python with Plotly.

Choropleth maps in Python
https://plotly.com/python/choropleth-maps/

I converted the log file of Iris dataset to another excel file of frequency of occurrence per country.

Column 01 : Time / Collection time
Column 02 : Country / Country name by ISO3 (Country name represented by 3 letters)
Column 03 : Frequency of occurrence / Frequency of occurrence of Probe_dst_prefix or Reply_src_addr

Country codes by alpha-2 & alpha-3
https://www.iban.com/country-codes
