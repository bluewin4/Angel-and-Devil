import openai

def generate_response(prompt, goal):
    model_engine = "text-davinci-002"  # Replace with the desired model (e.g., "gpt-4" or "gpt-3.5-turbo").
    prompt = f"Your goal is: {goal}\n\n{prompt}\nHow would a person with this goal respond?"

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=50,  # Adjust based on the desired response length.
        n=1,
        stop=None,
        temperature=0.7
    )

    message = response.choices[0].text.strip()
    return message