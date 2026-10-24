from groq import generate_response

import time

def temperature_prompt_activity():
    print("=" * 70)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE + INSTRUCTIONS")
    print("=" * 70)

    # PART 1: Temperature
    print("\nPART 1: TEMPERATURE EXPLORATION")
    base = input("Enter a creative prompt: ").strip()

    for t, label in [(0.1, "LOW (0.1) - Deterministic"),
                     (0.5, "MEDIUM (0.5) - Balanced"),
                     (0.9, "HIGH (0.9) - Creative")]:
        print(f"\n--- {label} ---")
        print(generate_response(base, temperature=t, max_tokens=512))
        time.sleep(1)

    # PART 2: Instruction-based prompts
    print("\nPART 2: INSTRUCTION-BASED PROMPTS")
    topic = input("Choose a topic (e.g., climate change, space exploration): ").strip()
    prompts = [
        f"Summarize key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I'm a 10-year-old child.",
        f"Write a pro/con list about {topic}.",
        f"Create a fictional news headline from 2050 about {topic}.",
    ]
    for i, p in enumerate(prompts, 1):
        print(f"\n--- INSTRUCTION {i} ---\n{p}")
        print(generate_response(p, temperature=0.7, max_tokens=512))
        time.sleep(1)

    # PART 3: Your prompt
    print("\nPART 3: YOUR OWN INSTRUCTION PROMPT")
    custom = input("Enter your instruction-based prompt: ").strip()
    try:
        temp = float(input("Set temperature (0.1 to 1.0): ").strip())
        if not (0.1 <= temp <= 1.0): 
            raise ValueError
    except ValueError:
        print("Invalid temperature. Using 0.7.")
        temp = 0.7

    print(f"\n--- YOUR PROMPT @ TEMP {temp} ---")
    print(generate_response(custom, temperature=temp, max_tokens=512))

    # Reflection + Challenge
    print("\nREFLECTION:")
    print("1) What changed when prompts became more specific?")
    print("2) What improved when context was added?")
    print("3) Which prompt felt most useful and why?")
    print("\nCHALLENGE: Create a prompt chain:")
    print("Generate content → rewrite with constraints → create a sequel (try different temps).")


if __name__ == "__main__":
    temperature_prompt_activity()
