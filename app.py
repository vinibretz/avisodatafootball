import streamlit as st
import time
import os

# Configurações da página
st.set_page_config(
    page_title="DataFootball - Endereço Atualizado", 
    page_icon="⚽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Remover o menu e rodapé
# Infelizmente ainda precisamos de um pouco de CSS para isso
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Logo do DataFootball
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        logo_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'logo.png')
        if os.path.exists(logo_path):
            st.image(logo_path, width=200)
        else:
            st.title("DataFootball")
    except:
        st.title("DataFootball")

# Título e subtítulo
st.title("📣 Nosso endereço mudou!")
st.subheader("Estamos de casa nova 🎉")

# Informação sobre o novo endereço
st.write("O DataFootball agora está disponível no novo endereço:")

# URL do novo site em destaque - usando components nativos
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.code("https://datafootball.com.br", language=None)

# Alerta de descontinuação
st.error("⚠️ ATENÇÃO: Este endereço será descontinuado em breve. Por favor, atualize seus favoritos com o novo link.")

# Informações adicionais
st.info("Todas as funcionalidades e dados continuam disponíveis no novo endereço, com melhorias na experiência e novas funcionalidades.")

# Botão de redirecionamento
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Ir para o novo site agora", type="primary", use_container_width=True):
        # Ainda precisamos usar html para redirecionamento, o Streamlit não tem API nativa para isso
        st.markdown(
            '<meta http-equiv="refresh" content="0; url=https://datafootball.com.br">',
            unsafe_allow_html=True
        )
        # Para mostrar ao usuário que algo está acontecendo
        with st.spinner("Redirecionando..."):
            time.sleep(1)
        st.stop()

# Separador
st.divider()

# Texto de redirecionamento
st.caption("Redirecionando automaticamente em alguns segundos...")

# Barra de progresso
progress = st.progress(0)

# Redirecionamento automático
for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.30)  # 30 segundos total

# Para mostrar ao usuário que o redirecionamento está acontecendo
with st.spinner("Redirecionando agora..."):
    time.sleep(1)

# Redirecionamento
st.markdown(
    '<meta http-equiv="refresh" content="0; url=https://datafootball.com.br">',
    unsafe_allow_html=True
)

# Rodapé
st.caption("© DataFootball 2025. Todos os direitos reservados.")