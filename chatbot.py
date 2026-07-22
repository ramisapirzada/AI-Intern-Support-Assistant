import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class AIInternChatbot:

    def __init__(self):

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        faq = pd.read_csv("data/faq.csv")
        tickets = pd.read_csv("data/support_tickets.csv")

        self.questions = faq["Question"].tolist() + tickets["Issue"].tolist()

        self.answers = faq["Answer"].tolist() + tickets["Resolution"].tolist()

        self.embeddings = self.model.encode(self.questions)

    def get_response(self, user_query):

        query_embedding = self.model.encode([user_query])

        scores = cosine_similarity(query_embedding, self.embeddings)[0]

        best_index = scores.argmax()

        confidence = scores[best_index]

        if confidence < 0.45:
            return (
                "Sorry, I couldn't find a relevant answer. Please contact your mentor or check the internship documentation.",
                confidence,
            )

        return self.answers[best_index], confidence