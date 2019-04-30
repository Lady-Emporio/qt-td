
from PyQt5.QtWidgets import QGraphicsEllipseItem 
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt,QRectF
class Tower(QGraphicsEllipseItem):
	HEIGHT=200
	WIDTH=200
	RECHARGE_ITER=30
	DAMAGE=1
	def __init__(self,x,y):
		QGraphicsEllipseItem.__init__(self,x, y, self.WIDTH,self.HEIGHT)
		self.recharge=self.RECHARGE_ITER;
		self.goal=None
	def paint(self,painter , StyleOptionGraphicsItem , Widget ):
		
		center=self.rect().center()
		OneFourPart=self.HEIGHT/4
		rectangle=QRectF(center.x()-OneFourPart/2, center.y()-OneFourPart/2, OneFourPart, OneFourPart);
		
		painter.setBrush(QColor(0,128,0))
		painter.drawEllipse(rectangle)
		
		color=QColor()
		color.setRgb(0,255,0,255/3)
		painter.setBrush(color)
		painter.drawEllipse(self.rect())
		
	def update(self,group):
		if self.recharge<self.RECHARGE_ITER:
			self.recharge+=1
			return
		else:
			if self.goal!=None:
				if self.collidesWithItem(self.goal):
					self.recharge=0;
					self.goal.hp-=self.DAMAGE
					return
					
			for mob in group:
				if self.collidesWithItem(mob):
					self.goal=mob
					self.recharge=0;
					self.goal.hp-=self.DAMAGE
					return
		
