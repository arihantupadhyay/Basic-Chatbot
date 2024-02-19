import tkinter as tk
from tkinter import scrolledtext, Entry, Button, END
from nltk.chat.util import Chat, reflections

class ChatbotApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Chatbot")

        self.create_widgets()

        # Initialize NLTK Chat
        self.chatbot = Chat(self.get_responses(), reflections)

    def create_widgets(self):
        self.chat_display = scrolledtext.ScrolledText(self.master, width=60, height=30, wrap=tk.WORD)
        self.chat_display.pack(padx=10, pady=10)

        self.user_input = Entry(self.master, width=50)
        self.user_input.pack(padx=10, pady=10)

        self.send_button = Button(self.master, text="Send", command=self.send_message,width=10)
        self.send_button.pack(pady=10)

    def get_responses(self):
        # Define chat patterns and responses
        patterns = [
            (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
            (r'i am a Sai Ganesh', ['Sir!, Sai Ganesh your my Boss. how may i help you']),
            (r'how are you', ['I am good, thank you!']),
            (r'What are you doing', ['I am doing well.']),
            (r'What is you name', ['I am a Chatbot']),
            (r'How old are you?', ['I am a machine,I have no Age,and no emotion']),

            # Add more patterns and responses as needed
        ]
        return patterns

    def send_message(self):
        user_message = self.user_input.get()
        self.user_input.delete(0, END)  # Clear the input field

        # Display user message in the chat
        self.display_message(f"User: {user_message}")

        # Get and display chatbot response
        bot_response = self.get_chatbot_response(user_message)
        self.display_message(f"Chatbot: {bot_response}")

    def get_chatbot_response(self, user_message):
        # Use NLTK chat to get a response
        response = self.chatbot.respond(user_message)
        return response

    def display_message(self, message):
        # Display messages in the chat display
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.yview(tk.END)  # Auto-scroll to the bottom

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_app = ChatbotApp(root)
    root.mainloop()