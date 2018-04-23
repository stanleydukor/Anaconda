import pyglet
from pyglet.window import key

window = pyglet.window.Window(500, 700)

state = {
    'score': 0
}

score_label_data = {
    'font_name': "Sans Serif",
    'font_size': 16,
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

pyglet.app.run()
