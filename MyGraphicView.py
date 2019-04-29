
from PyQt5.QtWidgets import (
QGraphicsView  
)
from Scene import Scene
class MyGraphicView(QGraphicsView):
	def __init__(self):
		QGraphicsView.__init__(self)
		scene = Scene();
		self.setScene(scene);      