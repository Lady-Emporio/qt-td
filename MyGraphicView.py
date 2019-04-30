
from PyQt5.QtWidgets import (
QGraphicsView  
)
from PyQt5.QtCore import QObject, pyqtSignal
from Scene import Scene
class MyGraphicView(QGraphicsView):
	hpChange = pyqtSignal()
	def __init__(self):
		QGraphicsView.__init__(self)
		scene = Scene();
		self.setScene(scene);    
		
		self.hpChange.connect(self.handle_trigger)
		
	def handle_trigger(self):
		self.parent().changeHP()