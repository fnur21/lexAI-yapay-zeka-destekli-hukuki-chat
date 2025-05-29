import json
from sklearn.model_selection import train_test_split

# Ana veriyi oku
with open("legal_data_augmented.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Veriyi %80 eğitim, %20 test olarak böl
train, test = train_test_split(data, test_size=0.2, random_state=42)

# Eğitim verisini kaydet
with open("train_data.json", "w", encoding="utf-8") as f:
    json.dump(train, f, ensure_ascii=False, indent=2)

# Test verisini kaydet
with open("test_data.json", "w", encoding="utf-8") as f:
    json.dump(test, f, ensure_ascii=False, indent=2)

print("train_data.json ve test_data.json başarıyla oluşturulduuu")
