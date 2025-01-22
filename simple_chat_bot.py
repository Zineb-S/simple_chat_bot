import nltk
import random
from nltk.chat.util import Chat, reflections
import streamlit as st

# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Zineb Selmouni.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No problem.",]
    ],
    [
        r"i'm (.*) doing well",
        ["Great to hear!", "That's good!",]
    ],
    [
        r"i'm (.*)",
        ["Why are you %1?", "How are you feeling %1?",]
    ],
    [
        r"what (.*) (weather|temperature) ?",
        ["I'm sorry, I cannot provide weather information.",]
    ],
    [
        r"what (.*) (time|date) ?",
        ["I'm sorry, I cannot provide time or date information.",]
    ],
    [
        r"what is your purpose?",
        ["I am here to assist you with your questions.",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!", "See you later!",]
    ],
    [
        r"quels sont les programmes de formation proposés\s*\?*",
        [
            "Nous proposons une variété de programmes dans les domaines du numérique, du design, de l'audiovisuel et du management. Consultez notre site web pour plus de détails.", ]
    ],
    [
        r"proposez-vous des formations en alternance\s*\?*",
        [
            "Oui, nous proposons des formations en alternance pour de nombreux programmes. Cela permet aux étudiants de combiner théorie et pratique.", ]
    ],
    [
        r"quels sont les critères d'admission pour (.*)\s*\?*",
        [
            "Les critères d'admission varient selon le programme. Veuillez consulter la page du programme concerné sur notre site web pour plus d'informations.", ]
    ],
    [
        r"quelle est la durée des études pour (.*)\s*\?*",
        ["La durée des études dépend du programme. En général, nos formations durent entre 3 et 5 ans.", ]
    ],
    [
        r"y a-t-il des spécialisations dans (.*)\s*\?*",
        [
            "Oui, nous proposons des spécialisations dans plusieurs domaines. Consultez notre site web pour voir les options disponibles.", ]
    ],
    [
        r"où se trouve le campus\s*\?*",
        ["Notre campus est situé à [Adresse du campus].", ]
    ],
    [
        r"y a-t-il des activités étudiantes\s*\?*",
        [
            "Oui, nous avons de nombreuses activités étudiantes organisées tout au long de l'année. Vous pouvez vous renseigner auprès du bureau de la vie étudiante.", ]
    ],
    [
        r"comment se déroule la vie étudiante à ynov campus\s*\?*",
        [
            "La vie étudiante à Ynov Campus est riche et dynamique, avec de nombreuses opportunités de s'engager dans des projets et des clubs.", ]
    ],
    [
        r"y a-t-il des logements étudiants à proximité\s*\?*",
        [
            "Oui, il y a plusieurs options de logements étudiants à proximité du campus. Nous pouvons vous fournir une liste de contacts.", ]
    ],
    [
        r"quels sont les services disponibles pour les étudiants\s*\?*",
        [
            "Nous offrons plusieurs services aux étudiants, tels que l'accès à la bibliothèque, des laboratoires informatiques, un service d'orientation et un accompagnement personnalisé.", ]
    ],
    [
        r"comment puis-je m'inscrire\s*\?*",
        ["Vous pouvez vous inscrire en ligne via notre site web. Suivez les instructions sur la page d'inscription.", ]
    ],
    [
        r"quels sont les frais de scolarité\s*\?*",
        [
            "Les frais de scolarité varient selon le programme. Veuillez consulter la page du programme concerné sur notre site web pour plus d'informations.", ]
    ],
    [
        r"y a-t-il des bourses d'études\s*\?*",
        [
            "Oui, nous proposons des bourses d'études pour les étudiants méritants. Vous pouvez vous renseigner auprès du service des bourses.", ]
    ],
    [
        r"quelles sont les dates limites d'inscription\s*\?*",
        [
            "Les dates limites d'inscription varient selon le programme. Veuillez consulter notre site web pour les dates précises.", ]
    ],
    [
        r"comment puis-je contacter l'administration\s*\?*",
        [
            "Vous pouvez contacter l'administration par téléphone, par email ou en vous rendant directement au bureau administratif.", ]
    ],
    [
        r"qu'est-ce qui distingue ynov campus des autres écoles\s*\?*",
        [
            "Ynov Campus se distingue par son approche pédagogique innovante, son corps professoral de qualité et son réseau de partenaires professionnels.", ]
    ],
    [
        r"quels sont les débouchés après (.*)\s*\?*",
        [
            "Les débouchés après [nom du programme] sont variés. Nos diplômés travaillent dans de nombreux secteurs, tels que [liste de secteurs].", ]
    ],
    [
        r"puis-je visiter le campus\s*\?*",
        [
            "Oui, vous pouvez visiter le campus lors de nos journées portes ouvertes ou en prenant rendez-vous avec notre service d'admission.", ]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase?", "Could you please elaborate?",]
    ],
]

def chatbot(user_input):
    chat = Chat(pairs, reflections)
    response = chat.respond(user_input)
    return response

# Streamlit UI
st.title("Ynov Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Predefined questions
questions = [
    "What is your name?",
    "How are you?",
    "What is your purpose?",
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
    "Quit"
]

# Display clickable questions
selected_question = st.selectbox("Choose a question to ask:", options=["Select a question"] + questions)

if st.button("Ask"):
    if selected_question and selected_question != "Select a question":
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": selected_question})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(selected_question)

        # Get chatbot response
        response = chatbot(selected_question)
        # Add chatbot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        # Display chatbot response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)