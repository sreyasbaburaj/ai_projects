print("Hello. Welocme to the Mood-based Chatbot")
a=input("What is your name? ")
print(f"Well nice to meet you {a} ")

while True:
    b=input("How are you feeling today? ")
    if b.lower()=="great" or b.lower()=="good":
        print("Good to hear you are doing well.")
    elif b.lower()=="bad" or b.lower()=="not good":
        print("I am sorry to hear that. Hope things get well soon.")
    else:
        print("I get it. Sometimes it's hard to describe what we feel.")

    exit=input("Would you like to exit or continue(Yes or No): ")
    if exit.lower()=="yes":
        print("Goodbye!")
        break
    else:
        print("Ok, lets keep going.")