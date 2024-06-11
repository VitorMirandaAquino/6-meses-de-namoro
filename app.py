import streamlit as st
from PIL import Image

# Função para exibir uma imagem centralizada
def display_image(image_path, caption):
    image = Image.open(image_path)
    st.image(image, caption=caption, use_column_width=True)

# Configuração da página
st.set_page_config(
    page_title="Minha cartinha",
    page_icon=":heart:",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Título principal
st.title("🌹 Minha Cartinha 🌹")

# Seção de boas-vindas
st.header("Para minha Ursinha!")
st.write("""
Em tão pouco tempo, já temos tantas lembranças inesquecíveis e um que amor que não cabe meu coração!!!!
Você me faz muito feliz e espero que eu possa fazer o mesmo. Em cada momento, como um cineminha,
um restaurante diferente que visitamos, nos nossos treinos ou em nossos momentos juntinhos. 
Seja no frio ou no calor, eu tenho uma certeza que é que eu te amo mais !!!!❤️
""")

# Linha do Tempo do Relacionamento
st.header("Nossa Linha do Tempo")
st.subheader("6 momentos especiais para celebrar os nossos 6 meses:")

# Adicione fotos e descrições dos marcos
with st.expander("Esse momento marcou a primeira vez que eu conheci os seus pais"):
    # Colação Bruna
    display_image("images/colacao-bruna-1.jpeg", "Colação de grau da melhor Cirurgiã Dentista do Mundo")

with st.expander("Esse momento poderia não ter acontecido, mas ainda bem que você é insistente"):
    # FORMATURA BRUNA
    display_image("images/formatura-bruna-1.jpeg", "Formatura Top em Marília")

with st.expander("Outro evento que quase não aconteceu, mas foi BA-BA-DO KKKKKK"):
    # FORMATURA BRUNA
    display_image("images/ano-novo-1.jpeg", "Ano Novo em Américo")

with st.expander("Sua primeira vez me visitando em São Paulo e conhecendo minha família"):
    # FORMATURA BRUNA
    display_image("images/pinacoteca-1.jpeg", "Turistando pela Pinacoteca")

with st.expander("Formatura ou Disputa por Espaço? Nessa valsa o que mais rolou foi trombada"):
    # FORMATURA BRUNA
    display_image("images/formatura-vitor-1.jpeg", "Minha Formatura cheia de familiares")

with st.expander("Conhecendo a Famosaaaa Tia Cidinha"):
    # FORMATURA BRUNA
    display_image("images/aniv-tio-1.jpeg", "Aniversário do seu Tio Avô")    


# Galeria de Fotos
st.header("Galeria de Fotos")

# Adicione fotos à galeria
with st.expander("Algumas fotinhas extras de nós dois:"):
    display_image("images/restaurante-1.jpeg", "Nós fazendo o que mais gostamos de fazer")
    display_image("images/formatura-bruna-2.jpeg", "Roda Gigante que te assustou muito")
    display_image("images/formatura-bruna-3.jpeg", "Nós dancançando muito na sua valsa")
    display_image("images/ano-novo-2.jpeg", "Dois fofos")


# Rodapé
st.write("Feito com ❤️ por Vitor Miranda")