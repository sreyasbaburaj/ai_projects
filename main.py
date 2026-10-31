from groq import generate_response

def reinforcement_learning_activity():
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")
    prompt=input("Enter a prompt for the AI model (e.g. Describe the lion): ")
    if not prompt:
        print("Please enter a prompt to run the activity")
        return

    initial_response=generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI Response: {initial_response}")

    try:
        rating=int(input("Rate the response from 1 to 5: ").strip())
        if rating <1 or rating > 5:
            print("Invalid rating. Using 3.")
            rating=3

    except ValueError:
        print("Invalid rating. Using 3.")            
        rating=3

    feedback=input("Provide a feedback for improvement: ").strip()
    imporved_prompt=prompt + " " + feedback
    improved_response=generate_response(imporved_prompt,temperature=0.3, max_tokens=1024)
    print(f"\nImproved AI Response: {improved_response}")

def role_base_prompt_activity():
    print("\n===ROLE BASE PROMPTS ACTIVITY ===\n")
    category = input("Enter a category (e.g., science, history): ").strip()
    item=input(f"Enter a specific {category} topic (e.g., photosynthesis for science): ")

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return

    teacher_prompt=f"You are a teacher. Explain {item} in simple terms."
    expert_prompt=f"You are an expert in {category}. Explain {item} in a detailed, technical manner."

    teacher_response=generate_response(teacher_prompt, temperature=0.3,max_tokens=1024)
    expert_response=generate_response(expert_prompt, temperature=0.3, max_tokens=1024)

    print(f"\n--- Teacher's Perspective ---\n{teacher_response}")
    print(f"\n--- Expert's Response ---\n{expert_response}")

def run_activity():
    print("\n=== AI LEARNING ACTIVITY ===")
    print("Choose an activity:")
    print("1) Reinforcement Learning")
    print("2) Role-Based Prompts")
    choice=input("> ").strip()

    if choice=="1":
        reinforcement_learning_activity()
    if choice=="2":
        role_base_prompt_activity()
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__=="__main__":
    run_activity()