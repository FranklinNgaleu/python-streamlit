import streamlit as st
import pandas

df = pandas.read_csv("data2.csv")

# Configuration de la page
st.set_page_config(
    page_title="MyApp",
    page_icon="🧊",
    layout="wide"
)

# Titre de la page
st.title("Votre Dashboard interactif avec Streamlit 🎨")

# Sous-titre de la page
st.subheader("Bienvenu sur votre Dashboard")

# Texte
st.text("Bienvenue sur notre plateforme interactive qui vous permettra d'explorer et d'analyser des données de manière intuitive. Ce Dashboard a été spécialement conçu \npour vous aider à mieux comprendre les concepts clés de la data science et à acquérir une expérience pratique en utilisant Streamlit")

# Sous-titre de la page
st.subheader("Comment utiliser `Streamlit`  ?")

# Texte
st.text("voici quelques commandes de bases pour utiliser `Streamlit`:")

# Sous-titre de la page
st.subheader("Titre et texte")
st.markdown("- `st.title('Title')` : pour afficher un titre\n- `st.markdown('Some text')`: pour afficher du texte\n- `st.write(data)` ou `st.dataframe(df)`: pour afficher des données")

# Sous-titre de la page
st.subheader("Widgets")
st.markdown("- `st.checkbox('Show raw data')` : pour afficher des données brutes\n- `st.selectbox('Choose a city',('London','New York','San Francisco'))`: pour afficher une liste déroulante\n- `st.button('Submit')` : pour afficher un bouton de soumission")

# Sous-titre de la page
st.subheader("Afficher des graphiques")
st.markdown("- `st.line_chart(data)` : pour afficher un graphique linéaire\n - `st.bar_chart(data)`: pour afficher un graphique à barres\n- `st.pyplot(fig)`: pour afficher un graphique matplotlib\n- `st.map(data)`: pour afficher une carte")

# Sous-titre de la page
st.subheader("Affichage des donnees brutes")
# Checkbox
if st.checkbox("Afficher les données brutes"):
    st.write(df)
    
# Sous-titre de la page
st.subheader("Affichage des Graphiques")


col1, col2 = st.columns(2)


st.subheader("Affichage dynamique des donnees")
with col1:
    profession = list(df.Profession.value_counts().index)
    st.write("1️⃣ Example de widget")
    age = st.slider("Sélectionnez un âge", min_value=20, max_value=100, value=30, step=1)
    pro = st.selectbox('Sélectionnez une profession', profession)
    st.write(df[(df.Profession == pro) & (df.Age > age)])


with col2:
    st.write("2️⃣ Example de widget formulaire")

    column = ['Graduated', 'Ever_Married']
    option = ['Yes', 'No']
    age_user = range(100)
    nb_children = range(14)

    form = st.form(key='my_form')

    with form:
        c1 = st.selectbox('Sélectionnez un crière', column)
        c2 = st.selectbox('Sélectionnez une option', option)
        c3 = st.selectbox('Sélectionnez un âge', age_user)
        c4 = st.selectbox('Sélectionnez un nombre d\'enfant', nb_children)

        submit = form.form_submit_button(label='Submit')

        if submit:
            st.write(df[(df[c1] == c2) & (df.Family_Size > c3)].Work_Experience.mean())

