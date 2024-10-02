import streamlit as st
import pandas as pd
import plotly.express as plotly_express
import plotly.graph_objects as go
from sqlalchemy.util import ordered_column_set
from streamlit import title

# Configurar o layout da página
st.set_page_config(layout="wide")

st.title("Acompanhamento dos planos de ação")


###### Total de Planos de ação por indicador ######
dfIndicadorGeral = pd.read_csv("indicador_qt_plano_acao.csv", sep=";", decimal=",")

dfIndicadorGeral.set_index('index', inplace=True)

print(dfIndicadorGeral)


###### Total status por indicador ######

dfStatus = pd.read_csv("indicador_status_plano_acao.csv", sep=";", decimal=",")

dfStatus.set_index('index', inplace=True)


##### Área de Gráficos #####
st.markdown("Abaixo os gráficos de acompanhamento dos planos de ação aplicadas as estrategias dos indicadores da meta 15 do PNE.")

multi = '''**Planos de Ação** - total de planos de ação  associados aos inddicadores da meta 15 do PNE .
'''
st.markdown(multi)
grafico_geral = plotly_express.bar(dfIndicadorGeral, x='indicador', y='quantidade', color='indicador', title='Indicador Geral - Total de planos de ação ativos vinculados associados aos indicadores.')

st.plotly_chart(grafico_geral)



multi = '''**Status dos Planos de ação para o indicador 1.
'''
st.markdown(multi)


indicador1 = plotly_express.bar(dfStatus, x='status', y='quantidade', color='status', title='Status por indicador')

indicador1Pizza = plotly_express.pie(dfStatus, values = 'quantidade', names='status', color='status', title='Status por indicador')


#st.plotly_chart(fig)
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(indicador1)

with col2:
    st.plotly_chart(indicador1Pizza)
