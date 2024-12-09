from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Página inicial - Exibe o formulário de inscrição
@app.route('/')
def home():
    return render_template('index.html')

# Rota para processar os dados do formulário
@app.route('/inscrever', methods=['POST'])
def inscrever():
    nome = request.form['nome'].strip()
    email = request.form['email'].strip()
    tipo_usuario = request.form.get('tipo_usuario', '').strip()  # Captura a escolha do tipo de usuário
    
    if not nome or not email or not tipo_usuario:
        return "<h1>Erro: Todos os campos são obrigatórios.</h1>", 400

    # Salvar os dados no CSV
    with open('lista_de_espera.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([nome, email, tipo_usuario])
    
    return redirect(url_for('sucesso', tipo_usuario=tipo_usuario))

# Página de sucesso
@app.route('/sucesso/<tipo_usuario>')
def sucesso(tipo_usuario):
    return render_template('sucesso.html', tipo_usuario=tipo_usuario)

if __name__ == '__main__':
    app.run(debug=True)
