
from PyQt5.QtWidgets import QGraphicsScene
from Items import Unit
class Scene(QGraphicsScene):
	def __init__(self):
		QGraphicsScene.__init__(self)
		WIDTH=1000
		HEIGHT=1000
		self.setSceneRect(0, 0, WIDTH, HEIGHT)
		
		# self.addItem(Unit(100,100))
	def mousePressEvent(self,GraphicsSceneMouseEvent):
		PointF =GraphicsSceneMouseEvent.scenePos()
		x=PointF.x()
		y=PointF.y()
		u=Unit(x,y)
		self.addItem(u)
		qlist_Elements=self.collidingItems(u)
		if (len(qlist_Elements)!=0):
			self.removeItem(u)
			QGraphicsScene.mousePressEvent(self,GraphicsSceneMouseEvent)