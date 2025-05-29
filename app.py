
#flask ile web sitesine entegre (framework


from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from embedding_model import get_best_answer  # embedding modelin fonksiyonu
# başka yerlerden gelen isteklere izin ver dmeek
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html') #html sayfasını render etmek i.iç

#/api/get_answer adresine biri soru yollarsa fonk çalıştır

@app.route('/api/get_answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    question = data.get('question', '')
    print("Gelen soru:", question)

    answer = get_best_answer(question)
    print("Cevap:", answer)

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
