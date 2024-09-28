from openai import OpenAI

def main():
    print("Running python-chatgpt")

    client = OpenAI()

    # THIS IS THE INPUT TO CHATGPT. CHANGE THIS TO WHAT YOU NEED
    content = "Say this is a test"

    # config
    model = "gpt-4o-mini"
    role = "user"

    response = client.chat.completions.with_raw_response.create(
        model=model,
        messages=[{"role": role, "content": content}],
    )

    print(f"Response Code: {response.status_code}")
    print(f"Response Status: {response.status}")
    print(response.content)


if __name__ == '__main__':
    main()

"""
HOW TO USE
1. Generate a new API key here: https://platform.openai.com/api-keys
2. Add your API key to your environment
    - mac: export OPENAI_API_KEY="your_api_key_here"
    - windows: setx OPENAI_API_KEY "your_api_key_here"
3. Run 'pip install openai'
4. Run the script
"""

