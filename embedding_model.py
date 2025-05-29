from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
# bu mini yapay zeka cümleleri sayıya çeviriyor

# JSON dosyasından sorular ve cevapları yükle
with open('train_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

# Soruları gömme işlemi (embedding) :sorular sayı listesine geçiş
question_embeddings = model.encode(questions, convert_to_numpy=True)

def get_best_answer(user_question, threshold=0.80):
    user_embedding = model.encode([user_question], convert_to_numpy=True)
    similarities = cosine_similarity(user_embedding, question_embeddings)
    best_index = np.argmax(similarities)
    best_score = similarities[0][best_index]

    if best_score < threshold:
        return "Üzgünüz, bu konuda size net bir cevap veremiyoruz. Lütfen hukuki danışmana başvurunuz."
    else:
        return answers[best_index]
