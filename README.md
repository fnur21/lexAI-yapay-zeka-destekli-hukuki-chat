## lexAI/ yapay zeka destekli hukuki danışman - minitaslak


## 🚀 Proje Hakkında
Bu proje, Türkçe hukuki sorulara yapay zeka destekli yanıtlar verebilen bir danışmanlık uygulamasıdır. Kullanıcının sorduğu soruya en yakın cevabı bulmak için `SentenceTransformer` modeliyle embedding (vektör) tabanlı benzerlik karşılaştırması yapılır.

## 🚀 Özellikler

- 🔍 **Embedding tabanlı arama:** Kullanıcıdan alınan soru, önceden tanımlı soru-cevap veri kümesiyle karşılaştırılarak en benzer yanıt bulunur.
- 📁 **JSON veri kümesi:** Türkçe hukuki sorular ve cevaplardan oluşan veri kümesi ile çalışır.
- 🧾 **Konsol üzerinden kolay kullanım.**

## 🛠️ Kullanılan Teknolojiler

- Python 3.10+
- [sentence-transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`)
- scikit-learn
- NumPy
- Pandas
  
