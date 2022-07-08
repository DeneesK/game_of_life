from flask import Flask, render_template
from game_of_life import*

app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(20, 20)
    return render_template('index.html')

@app.route('/live')
def live():
    life = GameOfLife()
    game_of_live = GameOfLife()
    if life.counter > 0:
        game_of_live.form_new_generation()
    life.counter += 1
    return render_template('live.html', game = game_of_live, life = life)

if __name__ == '__main__':
    app.run(debug=True)