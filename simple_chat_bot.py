import nltk
import random
from nltk.chat.util import Chat, reflections
import streamlit as st

# Define patterns and responses
pairs = [
    [
        r"mon nom est (.*)",
        ["Bonjour %1, comment puis-je vous aider aujourd'hui ?",]
    ],
    [
        r"quel est ton nom\?",
        ["Je suis YnovBot créé par Zineb Selmouni pour vous aider avec vos questions sur Ynov.",]
    ],
    [
        r"comment ça va\?",
        ["Je vais bien, merci !", "Ça va, et vous ?",]
    ],
    [
        r"désolé (.*)",
        ["Ce n'est pas grave.", "Pas de problème.",]
    ],
    [
        r"je vais (.*) bien",
        ["Ravi de l'entendre !", "C'est bien !",]
    ],
    [
        r"je suis (.*)",
        ["Pourquoi êtes-vous %1 ?", "Comment vous sentez-vous %1 ?",]
    ],
    [
        r"quel (.*) (temps|météo) ?",
        ["Désolé, je ne peux pas fournir d'informations sur la météo.",]
    ],
    [
        r"quel (.*) (heure|date) ?",
        ["Désolé, je ne peux pas fournir d'informations sur l'heure ou la date.",]
    ],
    [
        r"quel est ton objectif\?",
        ["Je suis ici pour vous aider avec vos questions.",]
    ],
    [
        r"quitter",
        ["Au revoir ! Prenez soin de vous.", "Adieu !", "À bientôt !",]
    ],
    [
        r"quels sont les programmes de formation proposés\s*\?*",
        [
            "Nous proposons une variété de programmes dans les domaines du numérique, du design, de l'audiovisuel et du management. Consultez notre site web pour plus de détails.",]
    ],
    [
        r"proposez-vous des formations en alternance\s*\?*",
        [
            "Oui, nous proposons des formations en alternance pour de nombreux programmes. Cela permet aux étudiants de combiner théorie et pratique.",]
    ],
    [
        r"quels sont les critères d'admission pour (.*)\s*\?*",
        [
            "Les critères d'admission varient selon le programme. Veuillez consulter la page du programme concerné sur notre site web pour plus d'informations.",]
    ],
    [
        r"quelle est la durée des études pour (.*)\s*\?*",
        ["La durée des études dépend du programme. En général, nos formations durent entre 3 et 5 ans.",]
    ],
    [
        r"y a-t-il des spécialisations dans (.*)\s*\?*",
        [
            "Oui, nous proposons des spécialisations dans plusieurs domaines. Consultez notre site web pour voir les options disponibles.",]
    ],
    [
        r"où se trouve le campus\s*\?*",
        ["Notre campus est situé à [Adresse du campus].",]
    ],
    [
        r"y a-t-il des activités étudiantes\s*\?*",
        [
            "Oui, nous avons de nombreuses activités étudiantes organisées tout au long de l'année. Vous pouvez vous renseigner auprès du bureau de la vie étudiante.",]
    ],
    [
        r"comment se déroule la vie étudiante à ynov campus\s*\?*",
        [
            "La vie étudiante à Ynov Campus est riche et dynamique, avec de nombreuses opportunités de s'engager dans des projets et des clubs.",]
    ],
    [
        r"y a-t-il des logements étudiants à proximité\s*\?*",
        [
            "Oui, il y a plusieurs options de logements étudiants à proximité du campus. Nous pouvons vous fournir une liste de contacts.",]
    ],
    [
        r"quels sont les services disponibles pour les étudiants\s*\?*",
        [
            "Nous offrons plusieurs services aux étudiants, tels que l'accès à la bibliothèque, des laboratoires informatiques, un service d'orientation et un accompagnement personnalisé.",]
    ],
    [
        r"comment puis-je m'inscrire\s*\?*",
        ["Vous pouvez vous inscrire en ligne via notre site web. Suivez les instructions sur la page d'inscription.",]
    ],
    [
        r"quels sont les frais de scolarité\s*\?*",
        [
            "Les frais de scolarité varient selon le programme. Veuillez consulter la page du programme concerné sur notre site web pour plus d'informations.",]
    ],
    [
        r"y a-t-il des bourses d'études\s*\?*",
        [
            "Oui, nous proposons des bourses d'études pour les étudiants méritants. Vous pouvez vous renseigner auprès du service des bourses.",]
    ],
    [
        r"quelles sont les dates limites d'inscription\s*\?*",
        [
            "Les dates limites d'inscription varient selon le programme. Veuillez consulter notre site web pour les dates précises.",]
    ],
    [
        r"comment puis-je contacter l'administration\s*\?*",
        [
            "Vous pouvez contacter l'administration par téléphone, par email ou en vous rendant directement au bureau administratif.",]
    ],
    [
        r"qu'est-ce qui distingue ynov campus des autres écoles\s*\?*",
        [
            "Ynov Campus se distingue par son approche pédagogique innovante, son corps professoral de qualité et son réseau de partenaires professionnels.",]
    ],
    [
        r"quels sont les débouchés après (.*)\s*\?*",
        [
            "Les débouchés après [nom du programme] sont variés. Nos diplômés travaillent dans de nombreux secteurs, tels que [liste de secteurs].",]
    ],
    [
        r"puis-je visiter le campus\s*\?*",
        [
            "Oui, vous pouvez visiter le campus lors de nos journées portes ouvertes ou en prenant rendez-vous avec notre service d'admission.",]
    ],
    [
        r"(.*)",
        ["Je ne suis pas sûr de comprendre. Pouvez-vous reformuler ?", "Pourriez-vous préciser votre question ?",]
    ],
]
questions = [
    "Quel est ton nom?",
    "Comment ça va?",
    "Quel est ton objectif?",
    "Quels sont les programmes de formation proposés?",
    "Proposez-vous des formations en alternance?",
    "Quels sont les critères d'admission pour les programmes?",
    "Quelle est la durée des études pour les programmes?",
    "Y a-t-il des spécialisations disponibles?",
    "Où se trouve le campus?",
    "Y a-t-il des activités étudiantes?",
    "Comment se déroule la vie étudiante à Ynov Campus?",
    "Y a-t-il des logements étudiants à proximité?",
    "Quels sont les services disponibles pour les étudiants?",
    "Comment puis-je m'inscrire?",
    "Quels sont les frais de scolarité?",
    "Y a-t-il des bourses d'études?",
    "Quelles sont les dates limites d'inscription?",
    "Comment puis-je contacter l'administration?",
    "Qu'est-ce qui distingue Ynov Campus des autres écoles?",
    "Quels sont les débouchés après les études?",
    "Puis-je visiter le campus?",
    "Quitter"
]


def chatbot(user_input):
    chat = Chat(pairs, reflections)
    return chat.respond(user_input)

# Streamlit configuration
st.set_page_config(page_title="YnovBot", layout="wide")


# Title and instructions
st.title("🤖 YnovBot : Votre Assistant Virtuel 🤖 ")
st.subheader("Choisissez une question prédéfinie et recevez une réponse immédiate.")


selected_question = st.selectbox("Questions prédéfinies :", ["Sélectionnez une question"] + questions)

if st.button("Poser la Question"):
    if selected_question and selected_question != "Sélectionnez une question":
        # Display user question
        st.write(f"**Vous**: {selected_question}")
        # Get chatbot response
        response = chatbot(selected_question)
        st.write(f"**YnovBot**: {response}")