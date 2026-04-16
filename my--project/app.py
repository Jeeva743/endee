# AI Chatbot using TF-IDF and Cosine Similarity

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Questions & Answers
questions = [
    "hello",
    "what is your name",
    "what is python",
    "what is ai",
    "how are you"
]

answers = [
    "Hi there!",
    "I am an AI chatbot.",
    "Python is a programming language.",
    "AI stands for Artificial Intelligence.",
    "I am doing great!"
]

# Convert text to vectors
vectorizer = TfidfVectorizer()
q_vectors = vectorizer.fit_transform(questions)

print("AI Smart Chatbot (type 'exit' to stop)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, q_vectors)

    index = similarity.argmax()

    print("Bot:", answers[index])