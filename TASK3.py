import nltk
from nltk.chat.util import Chat, reflections
from datetime import datetime

# conversations between user and chatbot
coversation = [
    # Greetings
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I assist you?"]],
    ["good morning|good afternoon|good evening", ["Good day!", "Hello! Hope you're having a great day."]],
    ["good night",["Have a peaceful sleep!","Sweet dreams!","Rest well!"]],

    # Basic questions
    ["how are you?", ["I'm just code, but I'm functioning perfectly!", "Doing great! How about you?"]],
    ["what is your name?", ["I am Codtech Bot!", "You can call me Codtech Assistant."]],
    ["who created you?", ["I was created by a Python intern at Codtech IT Services."]],
    ["what can you do?", ["I can chat with you, answer basic questions, and provide useful information."]],
    ["Are you a robot?", ["Yes I'm chatbot designed to assist you!"]],

    # Date & Time
    ["what time is it?|current time", [f"The current time is {datetime.now().strftime('%H:%M:%S')}."]],
    ["what is today's date?|current date", [f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."]],

    # Fun Questions
    ["tell me a joke", [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why don't skeletons fight each other? They don't have the guts!"
    ]],
    ["can you tell me a fun fact?", [
        "Did you know? Honey never spoils. Archaeologists found 3000-year-old honey in ancient Egyptian tombs, and it was still edible!",
        "Octopuses have three hearts!"
    ]],

    # Coding-related Questions
    ["what is python?", ["Python is a high-level, interpreted programming language known for its readability and versatility."]],
    ["what is a chatbot?", ["A chatbot is an AI-based program designed to simulate conversations with users automatically."]],
    ["how do I learn python?", [
        "You can start with online tutorials, YouTube videos, and coding platforms like Codecademy or Coursera.",
        "Practice by building small projects, like me!"
    ]],

    # General Queries
    ["how old are you?", ["I'm as old as the code that created me!", "I was just created recently, so I'm quite new."]],
    ["what is ai?", ["AI stands for Artificial Intelligence, which enables machines to mimic human intelligence."]],
    ["what is nlp?", ["NLP stands for Natural Language Processing. It helps machines understand and respond to human language."]],

    # Exit conditions
    ["bye|exit|quit", ["Goodbye!", "See you soon!", "Take care!"]],
]

# Fallback response if the chatbot doesn't understand the user_input
fallback_responses = [
    "Sorry, I didn't get that. Can you rephrase?",
    "I'm not sure I understand. Could you clarify?",
    "Hmm, I don't have an answer for that yet."
]

# Chatbot function for chatting
def chatbot():
    print("Hi, I'm Codtech Bot! Type 'exit' anytime to end the chat.")
    talk = Chat(coversation, reflections)

    while True:
        user_input = input("You: ").lower()

        # Exit condition for ending the coversation
        if user_input in ['exit', 'bye', 'quit']:
            print("Bot: Goodbye! Have a great day!")
            break

        # Response handling
        response = talk.respond(user_input)
        if response:
            print("Bot:", response)
        else:
            print("Bot:", fallback_responses[len(user_input) % len(fallback_responses)])

# Run the chatbot
if __name__ == "__main__":
    chatbot()                #function calling
