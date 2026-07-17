# Rule-Based Chatbot in Python

print("=" * 50)
print("🤖 Welcome to Rule-Based Chatbot")
print("Type 'bye' to exit.")
print("=" * 50)

while True:
    user = input("\nYou: ").lower().strip()

    if user == "hello" or user == "hi" or user == "hey":
        print("Bot: Hello! How can I help you today?")

    elif "your name" in user:
        print("Bot: My name is RuleBot. Nice to meet you!")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "time" in user:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"Bot: Current time is {current_time}")

    elif "date" in user:
        from datetime import datetime
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    elif "python" in user:
        print("Bot: Python is a powerful programming language used for AI, Data Science, Web Development, and Automation.")

    elif "data science" in user:
        print("Bot: Data Science involves collecting, analyzing, and visualizing data to gain insights.")

    elif "ai" in user or "artificial intelligence" in user:
        print("Bot: Artificial Intelligence enables machines to perform tasks that normally require human intelligence.")

    elif "help" in user:
        print("Bot: You can ask me about:")
        print("     - Python")
        print("     - AI")
        print("     - Data Science")
        print("     - Date")
        print("     - Time")

    elif "thank" in user:
        print("Bot: You're welcome! 😊")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")