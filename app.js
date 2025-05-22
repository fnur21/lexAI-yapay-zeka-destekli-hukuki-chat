document.getElementById('questionForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    let question = document.getElementById('question').value.trim();

    if (!question) {
        alert('Lütfen bir soru yazın.');
        return;
    }

    const responseContainer = document.getElementById('responseContainer');
    responseContainer.style.display = 'block';
    responseContainer.innerHTML = `<p><strong>Yanıt:</strong> Lütfen bekleyin, sorunuz analiz ediliyor...</p>`;

    try {
        let response = await fetch('http://127.0.0.1:5000/api/get_answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });

        let data = await response.json();
        responseContainer.innerHTML = `<p><strong>Yanıt:</strong> ${data.answer}</p>`;
        document.getElementById('question').value = '';

    } catch (error) {
        responseContainer.innerHTML = `<p><strong>Hata:</strong> Sunucuya bağlanırken bir sorun oluştu.</p>`;
    }
});
