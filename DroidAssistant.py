# droid_assistant.py
import requests

def search_duckduckgo(query):
    url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json",
        "no_redirect": 1,
        "no_html": 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Try Abstract first, fallback to related topics
    if data.get("AbstractText"):
        return data["AbstractText"]
    elif data.get("Answer"):
        return data["Answer"]
    elif data.get("RelatedTopics"):
        for topic in data["RelatedTopics"]:
            if "Text" in topic:
                return topic["Text"]
        return "No summary found, but related topics exist."
    else:
        return "Sorry, I couldn't find anything useful."

def chat_response(prompt):
    prompt = prompt.lower()

    if "hi" in prompt or "hello" in prompt:
        return "Hello! I'm Droid Assistant 🤖"
    elif "how are you" in prompt:
        return "I'm doing great, thanks! How about you?"
    elif "joke" in prompt:
        return "Why did the computer catch a cold? Because it left its Windows open! 😂"
    elif "who made you" in prompt:
        return "I was built by Lucan and coded into Droid Hub!"
    elif "bye" in prompt:
        return "Goodbye! 🖖"
    else:
        return "I'm not sure how to respond to that yet."

def main():
    print("🤖 Welcome to Droid Assistant v1.0!")
    print("Type something to chat. Use 'search for ...' to look things up.")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("You > ")

        if prompt.lower() == "exit":
            print("Assistant > Bye for now! 👋")
            break
        elif prompt.lower().startswith("search for "):
            query = prompt[11:].strip()
            if query:
                print("Assistant > Searching...")
                result = search_duckduckgo(query)
                print("Assistant >", result)
            else:
                print("Assistant > What should I search for?")
        else:
            print("Assistant >", chat_response(prompt))

if __name__ == "__main__":
    main()