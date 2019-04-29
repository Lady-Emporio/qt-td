from PyQt5.QtWidgets import QGraphicsRectItem 
from PyQt5.QtGui import QColor ,QFontMetrics 
from PyQt5.QtCore import Qt,QRectF
class Unit(QGraphicsRectItem):
	WIDTH=30
	HEIGHT=30
	def __init__(self,x,y):
		QGraphicsRectItem.__init__(self,0,0,self.WIDTH,self.HEIGHT)
		self.hp=100
		
		self.setPos(x-self.WIDTH/2,y-self.HEIGHT/2)
	def paint(self,painter , StyleOptionGraphicsItem , Widget ):
		painter.setBrush(QColor(0,128,0))
		painter.drawRect(self.rect())
		
		painter.setPen(QColor(255,0,0))
		
		rect=QRectF(0,0,self.WIDTH,self.HEIGHT)
		painter.drawText(rect, Qt.AlignHCenter|Qt.AlignTop, str(self.hp))
		
	def mousePressEvent(self,QGraphicsSceneMouseEvent):
		self.hp-=20
		if(self.hp<=0):
			self.scene().removeItem(self)
		self.update()