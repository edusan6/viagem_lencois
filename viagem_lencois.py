import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# Configuração da Página
st.set_page_config(
    page_title="Roteiro Lençóis 2026",
    page_icon="🚐",
    layout="centered"
)

# --- DADOS DA VIAGEM ---
# Estruturando seus dados em uma lista de dicionários para ficar dinâmico
roteiro = [
    # IDA
    {
        "fase": "IDA",
        "data_saida": "02/04/2026",
        "dia_semana": "Quinta-feira",
        "hora_saida": "19:00",
        "origem": "Imperatriz",
        "destino": "Açailândia",
        "chegada_prevista": "20:15",
        "obs": "Carro/Van Própria",
        "link": "https://maps.app.goo.gl/Wu31JuQEbBnM87JF9"
    },
    {
        "fase": "IDA",
        "data_saida": "02/04/2026",
        "dia_semana": "Quinta-feira",
        "hora_saida": "21:00",
        "origem": "Açailândia",
        "destino": "Barreirinhas",
        "chegada_prevista": "08:30 (03/04 - Sexta)",
        "obs": "Viagem noturna (Van)",
        "link": "https://maps.app.goo.gl/T1E8RpR2f5KNV1Nc9"
    },
    # VOLTA
    {
        "fase": "VOLTA",
        "data_saida": "05/04/2026",
        "dia_semana": "Domingo",
        "hora_saida": "12:00",
        "origem": "Barreirinhas",
        "destino": "Bacabeira",
        "chegada_prevista": "15:00",
        "obs": "Retorno tarde",
        "link": "https://maps.app.goo.gl/QY5GWX4Pf4agM8XD9"
    },
    {
        "fase": "VOLTA",
        "data_saida": "05/04/2026",
        "dia_semana": "Domingo",
        "hora_saida": "15:00",
        "origem": "Bacabeira",
        "destino": "São Luís",
        "chegada_prevista": "16:40",
        "obs": "Parada para jantar/descanso em SLZ",
        "link": "https://maps.app.goo.gl/PU3DqUfU5f5GnCHBA"
    },
    {
        "fase": "VOLTA",
        "data_saida": "06/04/2026",
        "dia_semana": "Segunda-feira",
        "hora_saida": "01:15",
        "origem": "São Luís (Aeroporto)",
        "destino": "Imperatriz",
        "chegada_prevista": "02:25",
        "obs": "Voo da Madrugada (Azul)",
        "link": "https://maps.app.goo.gl/T6tYNkkFLZZRawNz6"
    }
]

# --- FUNÇÕES VISUAIS ---
def card_viagem(item):
    """Cria um cartão visual para cada trecho"""
    with st.container(border=True):
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            st.markdown(f"**🕒 Saída:** {item['hora_saida']}")
            st.caption(f"{item['data_saida']}")
        
        with col2:
            st.markdown(f"### {item['origem']} ➝ {item['destino']}")
            st.info(f"🏁 Chegada: **{item['chegada_prevista']}**", icon="🏁")
            if item['obs']:
                st.caption(f"ℹ️ {item['obs']}")
        
        with col3:
            st.link_button("🗺️ Ver Rota", item['link'], use_container_width=True)

# --- APP PRINCIPAL ---
st.title("🚐 Viagem Lençóis Maranhenses")
st.subheader("Planejamento 2026")

# Contagem Regressiva
data_viagem = datetime(2026, 4, 2, 19, 0, 0)
hoje = datetime.now()
dias_restantes = (data_viagem - hoje).days

col_metrics1, col_metrics2 = st.columns(2)
col_metrics1.metric("Data da Partida", "02/04/2026")
col_metrics2.metric("Dias Restantes", f"{dias_restantes} dias")

st.divider()

# Separação por Abas
tab1, tab2 = st.tabs(["🚀 IDA (02/04)", "🏠 VOLTA (05/04)"])

with tab1:
    st.markdown("### Quinta-feira, 02 de Abril")
    for item in roteiro:
        if item['fase'] == "IDA":
            card_viagem(item)

with tab2:
    st.markdown("### Domingo, 05 de Abril")
    for item in roteiro:
        if item['fase'] == "VOLTA":
            card_viagem(item)

# Rodapé
st.markdown("---")
st.caption("Planejamento de viagem - Desenvolvido com Streamlit 🎈")