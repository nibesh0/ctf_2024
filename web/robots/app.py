from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/Yo_ho_ho_ho!_A_door!')
def secret_page():
    return "CTF{9462914920886f13906522e167250f19}"

if __name__ == '__main__':
    app.run()
