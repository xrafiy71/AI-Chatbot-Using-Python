from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train('chatterbot.corpus.english')

# Define a function to interact with the chatbot
def chat_with_bot():
    print("Hello! I am your chatbot. You can start chatting with me. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

# Call the function to start chatting with the bot
chat_with_bot()
