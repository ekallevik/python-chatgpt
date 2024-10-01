from openai import OpenAI

def main():
    print("Running python-chatgpt")

    client = OpenAI()

    # config
    model = "gpt-4o-mini"
    role = "system"

    object_codes = ["motor", "hjul", "vindu", "kjøler"]
    object_codes_str = ', '.join(object_codes)

    # todo: improve this
    repair_descriptions = [
        ['posisjon: hull i kjøler for vacumanl.', 'kort: Hull i kjøler for vacumsystem', 'beskrivelse: Hull i kjøler for vacumsystem\n'],
        ["posisjon: motor", "kort: vindu", "beskrivelse: dekkluft\n"],
    ]

    repair_descriptions_str = ', '.join([item for sublist in repair_descriptions for item in sublist])

    short_answers_only = True

    content = f"""
        Her en fullstendig oversikt over alle komponenter: [
            ${object_codes_str}
        ]
    
        En reparasjonsbestilling består av tre deler: posisjonstekst, korttekst og beskrivelse. Disse er manuelt registrert, og inneholder ofte motsetninger.
        
        Her er en liste over reperasjonsbestillinger: [
            ${repair_descriptions_str}
        ]
        
        For hver reparasjonsbestilling hvilken komponent tror du bestillingen handler om? 
        
        ${"Svar med en sannsynlighet for de mest relevante komponentene, adskilt av linjeskift" if short_answers_only else ""}
    """

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": role, "content": content},
        ],
        temperature=0.1, # how creative chatgpt should be, from 0.0 to 1.0
        max_tokens=300, # number of words-ish
        frequency_penalty=0 # encourages repeated phrases
    )

    for choice in resp.choices:
        print(choice.message.content)


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

