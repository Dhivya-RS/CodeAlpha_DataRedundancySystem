import datetime

print("=======================================")
print("        SMART AI CHATBOT SYSTEM        ")
print("=======================================")
print("Type 'help' to see commands")
print("Type 'bye' to exit\n")

name = input("Enter your name: ")
print(f"\nHello {name}! I am your AI assistant.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am functioning perfectly!")

    elif user == "your name":
        print("Bot: I am SmartBot, your AI assistant.")

    elif user == "time":
        now = datetime.datetime.now()
        print("Bot: Current time is:", now.strftime("%H:%M:%S"))

    elif user == "date":
        today = datetime.date.today()
        print("Bot: Today's date is:", today)

    elif user == "help":
        print("\nAvailable Commands:")
        print("hello")
        print("how are you")
        print("your name")
        print("time")
        print("date")
        print("bye\n")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I didn't understand that.")