from embedding_model import get_best_answer
import json

# Veriyi yükle (legal_data_augmented.json dosyasındaki soru-cevaplar)
with open("test_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Doğru sayacı
correct = 0
total = len(data)

# Tüm veriyi test et
for i, item in enumerate(data):
    question = item["question"]
    true_answer = item["answer"]

    predicted_answer = get_best_answer(question)

    # Aynıysa doğru say
    if predicted_answer.strip().lower() == true_answer.strip().lower():
        correct += 1
    else:
        print(f"[{i+1}] Yanlış ❌")
        print("Soru     :", question)
        print("Beklenen:", true_answer)
        print("Cevap    :", predicted_answer)
        print("---------")

# Sonuç
accuracy = correct / total * 100
print(f"\n✅ Toplam: {total}")
print(f"✅ Doğru: {correct}")
print(f"🎯 Doğruluk Oranı: {accuracy:.2f}%")
