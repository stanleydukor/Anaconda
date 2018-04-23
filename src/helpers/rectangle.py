#
# Credit: Jeff - https://stackoverflow.com/users/518277/jeff
#

from pyglet.gl import *
import pyglet

class Rect:

  def __init__(self, x, y, w, h):
    self.set(x, y, w, h)

  def draw(self):
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, self._quad)

  def set(self, x=None, y=None, w=None, h=None):
    self._x = self._x if x is None else x
    self._y = self._y if y is None else y
    self._w = self._w if w is None else w
    self._h = self._h if h is None else h
    self._quad = ('v2f', (self._x, self._y,
                          self._x + self._w, self._y,
                          self._x + self._w, self._y + self._h,
                          self._x, self._y + self._h))