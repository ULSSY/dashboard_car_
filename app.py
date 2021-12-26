from eda_app import run_eda_app
from ml_app import run_ml_app
import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import plotly.express as px
from eda_app import run_eda_app
from ml_app import run_ml_app
import matplotlib.pyplot as plt

def main():
    st.title('자동차 가격 예측 앱')

    # 사이드바 메뉴
    menu = ['메인 화면', '고객 정보', '데이터 검색']
    choice = st.sidebar.selectbox('메뉴', menu)
    
    
    
    if choice == '메인 화면' :
        df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')
        st.sidebar.header('<목록>')
        st.sidebar.subheader('1)Age and Annual Salary graph')
        st.sidebar.subheader('2)Credit Card Debt/Net Worth/Car Purchase Amount/graph')  
        st.sidebar.subheader( '')  
                                                        

     
        st.subheader('Age and Annual Salary')
        st.bar_chart(df[['Age','Annual Salary']]  )
       
       
        st.subheader('Credit Card Debt,Net Worth and Car Purchase Amount')
        st.bar_chart(df[['Credit Card Debt','Net Worth','Car Purchase Amount']]  )
    elif choice == '고객 정보' :
       

        run_eda_app()
        
    elif choice == '데이터 검색' :
        run_ml_app()
        


if __name__ == '__main__' :
        main()