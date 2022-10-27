import pandas as pd
import plotly.express as px
covid_df = pd.read_csv('./sample_data/owid-covid-data.csv',index_col='date',parse_dates=True)
fig = px.choropleth(covid_df, 
                    locations="iso_code",
                    color='total_cases', 
                    animation_frame=covid_df.index.strftime('%Y/%m/%d'),
                    range_color=[0,1000000])
fig.show()