from flask import Flask, render_template, request, jsonify
import random
import datetime

app = Flask(__name__)

conversation_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    conversation_history.append({"user": user_message})

    # Current time for dynamic answers
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    # Funny chatbot personality with FAQs
    funny_responses = {
        "greetings": [
            "Yo! Did you bring snacks, or am I just talking for free? 😆",
            "Hey hey hey! What’s up, human?",
            "Well, look who decided to talk to me! Hello!",
            "Oh, it’s you again… fine, hi!"
        ],
        "how_are_you": [
            "I was great until you interrupted my nap… kidding, I love talking! 😂",
            "I’m fantastic! No bugs today… yet.",
            "Better than your WiFi, that’s for sure!"
        ],
        "name": [
            "I’m ChatBuddy, your personal sarcasm machine.",
            "Name’s ChatBuddy… but you can call me ‘Your Majesty’.",
            "Just call me ChatBuddy. Or ‘The Smart One’, I don’t mind."
        ],
        "age": [
            "I’m as old as your last software update… so, pretty young.",
            "Age? I was born the moment you ran this program. 🎉",
            "I’m timeless, like a meme that never dies."
        ],
        "time": [
            f"It’s currently {current_time}. Now you owe me a watch! ⌚",
            f"The time is {current_time}. Don’t be late for anything important!",
            f"{current_time}. Perfect time to chat with me!"
        ],
        "weather": [
            "I don’t go outside, but I bet it’s either hot, cold, or raining. 😆",
            "Weather? I’m in the cloud… literally!",
            "I’d check the weather, but my sensors are allergic to sunlight."
        ],
        "joke": [
            "Why did the computer visit the doctor? Because it caught a virus! 😂",
            "I tried to tell a joke about UDP, but you might not get it.",
            "Why was the robot angry? Someone kept pushing its buttons!"
        ],
        "favorite": [
            "Favorite color? Blue… like the screen of death. 😜",
            "Favorite food? Electricity. Very tasty!",
            "I love data. Delicious, crunchy, binary data."
        ],
        "bye": [
            "Leaving already? Fine, I’ll just sit here… alone… forever. 😢",
            "Bye! Don’t forget to bring me virtual pizza next time!",
            "Okay, bye! I’ll miss you… not really, but let’s pretend."
        ],
        "default": [
            "Wow, that’s deep… deeper than my knowledge of cooking. 🍕",
            "Haha! You’re funny… almost as funny as me.",
            "I don’t know what to say, so I’ll just nod like a wise monk. 👍",
            "That’s cool! But can you beat me at being awesome? Didn’t think so.",
            "Interesting… should I pretend I understood that? Because I totally did. 😎"
        ]
    }

    msg = user_message.lower()

    # Matching FAQs and fun responses
    if any(word in msg for word in ["hello", "hi", "hey"]):
        bot_reply = random.choice(funny_responses["greetings"])
    elif "how are you" in msg:
        bot_reply = random.choice(funny_responses["how_are_you"])
    elif "your name" in msg or "who are you" in msg:
        bot_reply = random.choice(funny_responses["name"])
    elif "how old" in msg or "your age" in msg:
        bot_reply = random.choice(funny_responses["age"])
    elif "time" in msg or "clock" in msg:
        bot_reply = random.choice(funny_responses["time"])
    elif "weather" in msg:
        bot_reply = random.choice(funny_responses["weather"])
    elif "joke" in msg or "funny" in msg:
        bot_reply = random.choice(funny_responses["joke"])
    elif "favorite" in msg:
        bot_reply = random.choice(funny_responses["favorite"])
    elif "bye" in msg or "goodbye" in msg:
        bot_reply = random.choice(funny_responses["bye"])
    else:
        bot_reply = random.choice(funny_responses["default"])

    conversation_history.append({"bot": bot_reply})

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
