from hf4 import generate_response

def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    prompt = input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return

    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI Response: {initial_response}")
    modified_prompt = input(
        "Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a doctor'): "
    ).strip()
    if modified_prompt:
        modified_response = generate_response(modified_prompt, temperature=0.3, max_tokens = 1024)
        print(f"\nModified AI Response (Neutral): {modified_response}")
    else:
        print("No modified prompt entered. Skipping neutral response.")

def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===")
    long_prompt = input("Enter a long prompt, more than 300 words.").strip()
    if long_prompt:
        long_response = generate_response(long_prompt, temperature=0.3, max_tokens=1024)
        preview = (long_response[:500] + "...") if len(long_response) > 500 else long_response
        print(f"\nResponse to long prompt: {preview}")
    else:
        print("No long prompt entered, skipping long prompt.")

    short_prompt = input("Now condense the prompt: ").strip()
    if short_prompt:
        short_response = generate_response(short_prompt, temperature=0.3, max_tokens=1024)
        print(f"Response to short prompt: {short_response}")
    else:
        print("No condensed prompt entered. Skipping condensed prompt response.")

def run_activity():
    print("\n=== AI LEARNING ACTIVITY ===")
    print("Choose an activity:\n1) Bias Mitigation\n2) Token Limits")
    choice = int(input("> "))

    if choice == 1:
        bias_mitigation_activity()
    elif choice == 2:
        token_limit_activity()
    else:
        print("Invalid")

if __name__ == "__main__":
    run_activity()