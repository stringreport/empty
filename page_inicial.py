import streamlit as st

# Função de autenticação
def authenticate(username, password):
    # Aqui você deve adicionar a lógica de autenticação real
    # Por exemplo, verificar contra um banco de dados
    if username == "admin" and password == "admin":
        return True
    return False

# Controle de navegação
def main():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        st.write("Bem-vindo ao aplicativo!")
        # Aqui você pode adicionar mais conteúdo ou funcionalidades do app
        if st.button("Logout"):
            st.session_state.authenticated = False
    else:
        login()

# Função de login dentro de um container
def login():
    with st.container():
        st.image('logocomunismen.png')

        username = st.text_input("Nome de Usuário")
        password = st.text_input("Senha", type="password")

        if st.button("Login"):
            if authenticate(username, password):
                st.success("Login bem-sucedido!")
                st.session_state.authenticated = True
            else:
                st.error("Nome de usuário ou senha incorretos. Tente novamente.")

# Executa o aplicativo
if __name__ == '__main__':
    main()
