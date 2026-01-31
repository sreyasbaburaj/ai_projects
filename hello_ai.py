print("Hello! I am an AI chatbot.")
a=input("What is your name? ")
print(f"Nice to meet you {a}")
b=input("How are you feeling today? ").lower()
if "good" in b or "great" in b:
    print("I am glad to hear that.")
elif b=="bad" or b=="not good":
    print("I am sorry to hear that. Hope things get better soon.")
else:
    print("I understand, sometimes it's hard to describe how we feel,take your time")
print(f"It was nice talking to you, {a}")
print("Goodbye")
