import streamlit as st
import time
import random

# Configuração da página
st.set_page_config(
    page_title="Giro dos Famosos e Anônimos",
    page_icon="💣",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------- Sidebar
st.sidebar.image("Giro.png", width=250)
st.sidebar.title('Somente  💣💣')

fofocas = ["Anonimos", "Famosos"]
opcao = st.sidebar.selectbox('Escolha a bomba da semana', fofocas)

# Adicionar uma descrição na sidebar
st.sidebar.markdown("---")
st.sidebar.info("💡 Selecione uma categoria acima e clique em 'Revelar bomba!' para ver a fofoca quente!")

# ----------------------------------------------- Principal 
st.title('Bomba da Semana 💣💣💣💣💣')

# Adicionar um botão para iniciar a contagem regressiva
if st.button('Revelar bomba!', key="reveal_button"):
    
    # Container para a contagem regressiva
    countdown_placeholder = st.empty()
    
    # Animação de contagem regressiva
    with countdown_placeholder.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>PREPAREM-SE!</h1>", 
                       unsafe_allow_html=True)
            
            # Contagem regressiva com estilo
            for i in range(5, -1, -1):
                if i > 0:
                    st.markdown(f"<h2 style='text-align: center; font-size: 80px;'>{i}</h2>", 
                               unsafe_allow_html=True)
                else:
                    st.markdown(f"<h2 style='text-align: center; color: #ff4b4b; font-size: 80px;'>BOMBA!</h2>", 
                               unsafe_allow_html=True)
                time.sleep(1)
    
    # Limpar a contagem regressiva
    countdown_placeholder.empty()
    
    # Revelar a imagem
    try:
        st.image(f'{opcao}.png', use_container_width=True)
        
        # Adicionar uma mensagem aleatória para tornar mais divertido
        mensagens = [
            "Essa vai abalar as estruturas! 💥",
            "Ninguém estava esperando por essa! 😲",
            "Essa bomba vai dar o que falar! 🗣️",
            "Preparem-se para ficar chocados! ⚡"
        ]
        st.success(random.choice(mensagens))
        
    except:
        st.error('Poxa que pena o Giro dos anônimos está sem conteúdo 😭😭😭😭')
        st.balloons()  # Adiciona animação de balões para tornar mais divertido

    st.markdown('---')
    
    # Adicionar um botão para reiniciar a experiência
    if st.button('Revelar outra bomba!', key="rerun_button"):
        st.rerun()  # Correção aplicada aqui

else:
    st.info("👈 Selecione uma categoria na sidebar e clique no botão acima para revelar a bomba!")

# Adicionar algum estilo CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #ff4b4b;
        text-align: center;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 5px;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #ff2b2b;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Rodapé
st.markdown("---")

st.markdown("© 2026 Giro dos Famosos e Anônimos - Todas as bombas são para o entretenimento")
