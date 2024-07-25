import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalysisChatbot:
    def __init__(self):
        nltk.download('vader_lexicon')  
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, message):
        sentiment_scores = self.sia.polarity_scores(message)
        compound_score = sentiment_scores['compound']

        if compound_score >= 0.05:
            return "positive"
        elif compound_score <= -0.05:
            return "negative"
        else:
            return "neutral"

    def chat(self):
        print("Hello! I'm your sentiment analysis chatbot. Type 'exit' to end the conversation.")

        while True:
            user_input = input("You: ")

            if user_input.lower() == 'exit':
                print("Goodbye!")
                break

            sentiment = self.analyze_sentiment(user_input)
            print(f"Chatbot: You seem to have a {sentiment} sentiment.")

if __name__ == "__main__":
    chatbot = SentimentAnalysisChatbot()
    chatbot.chat()
