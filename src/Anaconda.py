import pyglet
from pyglet.window import key

from helpers.rectangle import Rect

window = pyglet.window.Window(500, 700)
pyglet.gl.glClearColor(0.22,0.55,0.3,1)

state = {
    'score': 0
}

score_label_data = {
    'font_name': "Sans Serif",
    'font_size': 16,
    # 'font_color': 'red',
    'x': window.width // 2,
    'y': 20,
    'anchor_x': 'center',
    'anchor_y': 'center'
}

score_label = pyglet.text.Label("Score: {}".format(state['score']), **score_label_data)

header_label_data = {
    'font_name': "Sans Serif",
    'font_size': 32,
    'x': window.width // 2,
    'y': 680,
    'anchor_x': 'center',
    'anchor_y': 'center'
}

game_area = Rect(20, 40, 460, 600)

header_label = pyglet.text.Label("Anaconda", **header_label_data)

@window.event
def on_key_press(symbol, modifier):
    if symbol == key.LEFT: 
        print("left arrow was pressed")
    elif symbol == key.RIGHT:
        print("right arrow was pressed")
    elif symbol == key.UP:
        print("up arrow was pressed")
    elif symbol == key.DOWN:
        print("down arrow was pressed")
    elif symbol == key.P:
        print("pause key was pressed")
    elif symbol == key.ENTER:
        print("start key was pressed")

@window.event
def on_draw():
    window.clear()
    score_label.draw()
    header_label.draw()
    game_area.draw()

pyglet.app.run()
