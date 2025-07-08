# chatbot.py
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "your name" in user_input:
        return "I'm CodBot, your virtual assistant."
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
