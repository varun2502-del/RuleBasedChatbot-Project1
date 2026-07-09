from datetime import datetime

print("=== Welcome to Rule-Based AI Chatbot ===")
print("Type 'help' to see available commands.")

while True:
    user = input("You: ").lower()

    # Greetings
    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    # Basic Questions
    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user == "who created you":
        print("Bot: I was created by Venkatesh.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions, tell time, tell jokes, and perform calculations.")

    # Date and Time
    elif user == "time":
        print("Bot:", datetime.now().strftime("%H:%M:%S"))

    elif user in ["date", "today's date"]:
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    # Joke
    elif user == "joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    # Calculator
    elif user == "calculator":
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                print("Result:", num1 + num2)
            elif op == "-":
                print("Result:", num1 - num2)
            elif op == "*":
                print("Result:", num1 * num2)
            elif op == "/":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                    print("Cannot divide by zero.")
            else:
                print("Invalid operator.")
        except ValueError:
            print("Please enter valid numbers.")

    # Help Menu
    elif user == "help":
        print("""
Available Commands:
hi
hello
hey
how are you
what is your name
who created you
what can you do
time
date
today's date
joke
calculator
bye
exit
quit
""")

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    # Unknown Command
    else:
        print("Bot: Sorry, I don't understand that.")