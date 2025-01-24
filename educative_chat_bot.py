import streamlit as st

# Define the knowledge base (as before)
knowledge_base = {
    "Algorithmics": {
        "What is an algorithm?": {
            "answer": "An algorithm is a step-by-step method for solving a problem or completing a task. It is a set of well-defined instructions that can be executed by a computer to achieve a desired output.",
            "options": {
                "What are examples of algorithms?": {
                    "answer": "Examples of algorithms include: \n- Sorting algorithms (e.g., QuickSort, MergeSort)\n- Searching algorithms (e.g., Binary Search, Linear Search)\n- Graph traversal algorithms (e.g., Dijkstra's, BFS, DFS)",
                },
                "What are the properties of a good algorithm?": {
                    "answer": "A good algorithm has the following properties:\n1. Correctness: Produces the correct output for all valid inputs.\n2. Efficiency: Uses minimal resources (time and space).\n3. Clarity: Easy to understand and implement.\n4. Finiteness: Terminates after a finite number of steps.",
                }
            }
        },
        "What is Big-O Notation?": {
            "answer": "Big-O Notation is a mathematical notation used to describe the time complexity or space complexity of an algorithm in terms of input size.",
            "options": {
                "What are common time complexities?": {
                    "answer": "Common time complexities include:\n- O(1): Constant time\n- O(log n): Logarithmic time\n- O(n): Linear time\n- O(n^2): Quadratic time\n- O(2^n): Exponential time",
                },
                "Why is Big-O important?": {
                    "answer": "Big-O helps developers understand the scalability of algorithms and compare their efficiency, particularly for large inputs.",
                }
            }
        }
    },
    "Programming": {
        "What is Programming?": {
            "answer": "Programming is the process of creating and implementing instructions for a computer to perform specific tasks.",
            "options": {
                "What are common programming languages?": {
                    "answer": "Common programming languages include Python, JavaScript, Java, C++, Go, and Ruby.",
                },
                "What is a programming paradigm?": {
                    "answer": "A programming paradigm is a style or way of programming. Examples include procedural programming, object-oriented programming (OOP), functional programming, and declarative programming.",
                }
            }
        },
        "What are software design patterns?": {
            "answer": "Software design patterns are reusable solutions to common problems in software design. They act as templates for solving recurring issues.",
            "options": {
                "What are examples of design patterns?": {
                    "answer": "Examples include:\n- Creational Patterns (e.g., Singleton, Factory)\n- Structural Patterns (e.g., Adapter, Decorator)\n- Behavioral Patterns (e.g., Observer, Strategy)",
                },
                "Why use design patterns?": {
                    "answer": "Design patterns improve code readability, reusability, and maintainability while promoting best practices in software development.",
                }
            }
        }
    },
    "Databases": {
        "What is a database?": {
            "answer": "A database is an organized collection of data stored electronically for easy access, retrieval, and management.",
            "options": {
                "What are relational databases?": {
                    "answer": "Relational databases use a tabular structure with rows and columns. Examples include MySQL, PostgreSQL, and SQL Server.",
                },
                "What are NoSQL databases?": {
                    "answer": "NoSQL databases are designed for unstructured or semi-structured data and include types like document-based (MongoDB), key-value stores (Redis), and graph databases (Neo4j).",
                }
            }
        },
        "What is SQL?": {
            "answer": "SQL (Structured Query Language) is a language used to manage and manipulate relational databases.",
            "options": {
                "What are common SQL commands?": {
                    "answer": "Common SQL commands include:\n- SELECT: Retrieve data\n- INSERT: Add data\n- UPDATE: Modify data\n- DELETE: Remove data\n- CREATE: Create a database or table",
                },
                "What are SQL joins?": {
                    "answer": "SQL joins combine rows from two or more tables based on related columns. Types of joins include INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.",
                }
            }
        }
    },
    "Security": {
        "What is cybersecurity?": {
            "answer": "Cybersecurity involves protecting computer systems, networks, and data from cyber threats such as hacking, malware, and unauthorized access.",
            "options": {
                "What are common cyber threats?": {
                    "answer": "Common threats include:\n- Phishing attacks\n- Ransomware\n- Denial-of-service (DoS) attacks\n- SQL injection\n- Social engineering",
                },
                "What is multi-factor authentication?": {
                    "answer": "Multi-factor authentication (MFA) is a security measure requiring two or more forms of verification to access a system, such as a password and a one-time code.",
                }
            }
        },
        "What is encryption?": {
            "answer": "Encryption converts data into a secure format that can only be read with a decryption key.",
            "options": {
                "What are common encryption types?": {
                    "answer": "Common types include:\n- Symmetric encryption (e.g., AES)\n- Asymmetric encryption (e.g., RSA, ECC)",
                },
                "What is HTTPS?": {
                    "answer": "HTTPS (Hypertext Transfer Protocol Secure) encrypts data transmitted between a web browser and a server to ensure secure communication.",
                }
            }
        }
    },
    "Cloud Computing": {
        "What is cloud computing?": {
            "answer": "Cloud computing delivers computing services (e.g., storage, servers, databases) over the Internet.",
            "options": {
                "What are the cloud service models?": {
                    "answer": "Cloud service models include:\n- IaaS (Infrastructure as a Service): e.g., AWS EC2\n- PaaS (Platform as a Service): e.g., Heroku\n- SaaS (Software as a Service): e.g., Google Workspace",
                },
                "What are the benefits of cloud computing?": {
                    "answer": "Benefits include:\n- Scalability\n- Cost efficiency\n- Flexibility\n- Disaster recovery",
                }
            }
        },
        "What is serverless computing?": {
            "answer": "Serverless computing allows developers to run applications without managing servers. Examples include AWS Lambda and Azure Functions.",
            "options": None
        }
    },
    "Programming Languages": {
        "What is Python?": {
            "answer": "Python is a versatile programming language used in data science, web development, AI, and more.",
            "options": {
                "Why is Python popular?": {
                    "answer": "Python is popular due to its simplicity, vast libraries, and wide community support.",
                },
                "What is Python used for?": {
                    "answer": "Python is used for:\n- Data analysis\n- Machine learning\n- Web applications\n- Automation",
                }
            }
        },
        "What is Java?": {
            "answer": "Java is an object-oriented, platform-independent language widely used in enterprise applications and Android development.",
            "options": {
                "What is the JVM?": {
                    "answer": "The JVM (Java Virtual Machine) runs Java bytecode and makes Java platform-independent.",
                },
                "What is an interface in Java?": {
                    "answer": "An interface is a contract that specifies methods a class must implement.",
                }
            }
        }
    }
}


# Initialize session state
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None
if "selected_question" not in st.session_state:
    st.session_state.selected_question = None
if "selected_sub_question" not in st.session_state:
    st.session_state.selected_sub_question = None

# Title and instructions
st.title("🤖 YnovBot Educative : Votre Assistant Virtuel 🤖 ")


st.sidebar.title("Knowledge Base")
category = st.sidebar.radio("Choose a category:", list(knowledge_base.keys()))

# Reset state if category changes
if category != st.session_state.selected_category:
    st.session_state.selected_category = category
    st.session_state.selected_question = None
    st.session_state.selected_sub_question = None

# Main content
if category:
    st.title(category)
    questions = knowledge_base[category]

    for question, content in questions.items():
        # Display questions as clickable buttons
        if st.button(question):
            st.session_state.selected_question = question
            st.session_state.selected_sub_question = None  # Reset sub-question selection

    # Display the selected question's answer and follow-ups
    if st.session_state.selected_question:
        selected_question = st.session_state.selected_question
        st.subheader(selected_question)
        st.write(questions[selected_question]["answer"])

        # Display follow-up questions
        if questions[selected_question].get("options"):
            st.write("### Follow-up Questions:")
            for sub_question, sub_content in questions[selected_question]["options"].items():
                if st.button(sub_question):
                    st.session_state.selected_sub_question = sub_question

            # Display the selected sub-question's answer
            if st.session_state.selected_sub_question:
                selected_sub_question = st.session_state.selected_sub_question
                st.write(f"#### {selected_sub_question}")
                st.write(questions[selected_question]["options"][selected_sub_question]["answer"])