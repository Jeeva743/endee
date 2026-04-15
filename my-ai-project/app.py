
print("AI Chatbot (type 'exit' to stop)")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye!")
        break
    elif "hello" in user_input:
        print("Bot: Hi there!")
    elif "how are you" in user_input:
        print("Bot: I am fine!")
    else:
        print("Bot: I don't understand.")