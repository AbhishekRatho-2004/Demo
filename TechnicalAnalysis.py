import streamlit as st
import yfinance as yf
import pandas_ta as ta
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
th_props = [
  ('font-size', '14px'),
  ('text-align', 'center'),
  ('font-weight', 'bold'),
  ('color', 'White')
  ]
                               
td_props = [
  ('font-size', '12px')
  ]
                                 
styles = [
  dict(selector="th", props=th_props),
  dict(selector="td", props=td_props)
  ]
st.subheader(':blue[Technical Indicators Analysis]')
st.markdown('<h3>Technical Indicator</h3>',unsafe_allow_html=True)
st.markdown('<p>A technical indicator is a mathematical calculation or pattern derived from price, volume, or open interest of a security (such as stocks, currencies, commodities, etc.) in financial markets. These indicators are used by traders and analysts to gain insights into the markets trend, momentum, volatility, and potential reversal points. Technical indicators are applied to charts to help traders make more informed decisions about when to buy, sell, or hold a particular security.</p>',unsafe_allow_html=True)
symbol=st.text_input('')
per=st.selectbox('Period',options=['1d','2d','1w','1mo','3mo','6mo','1y'])
inter=st.selectbox('Interval',options=['1d','5d','1wk'])
tech=yf.download(symbol,period=per,interval=inter)

df=pd.DataFrame()
ind_list=df.ta.indicators(as_list=True)
technical_indicator=st.selectbox('Tech Indicators',options=ind_list)
method=technical_indicator
indicator=pd.DataFrame(getattr(ta,method)(low=tech['Low'],close=tech['Close'],high=tech['High'],open=tech['Open'],volume=tech['Volume']))
indcl,indop=st.columns(2)
with indcl:
    st.metric(':blue[Closing Price]',value=tech.Close.mean().round(2),delta='1%')
with indop:
    st.metric(':blue[Opening Price]',value=tech.Open.mean().round(2),delta='-3%')
indh,indl=st.columns(2)
with indh:
    st.metric(':blue[High Price]',value=tech.High.mean().round(2),delta='-1%')
with indl:
    st.metric(':blue[Lowest Price]',value=tech.Low.mean().round(2),delta='-1.4%')
indicator['Close']=tech['Close']
fig_ind_new=px.line(indicator)
st.plotly_chart(fig_ind_new)
st.table(indicator.head(10).style.set_table_styles(styles))