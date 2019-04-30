
from PyQt5.QtWidgets import QGraphicsEllipseItem ,QGraphicsRectItem, QGraphicsProxyWidget ,QGraphicsLinearLayout  ,QListWidget,QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt,QRectF
class Tower(QGraphicsEllipseItem):
	RADIUS_DAMAGE=200
	T_RADIUS=20
	RECHARGE_ITER=30
	DAMAGE=1
	color=QColor(0,128,0)
	def __init__(self,x,y):
		QGraphicsEllipseItem.__init__(self,x, y, self.RADIUS_DAMAGE,self.RADIUS_DAMAGE)
		self.recharge=self.RECHARGE_ITER;
		self.goal=None
		# self.setZValue(-1)
	def paint(self,painter , StyleOptionGraphicsItem , Widget ):
		
		center=self.rect().center()
		OneFourPart=self.T_RADIUS
		rectangle=QRectF(center.x()-OneFourPart/2, center.y()-OneFourPart/2, OneFourPart, OneFourPart);
		
		painter.setBrush(self.color)
		painter.drawEllipse(rectangle)
		
		color=QColor()
		color.setRgb(0,255,0,255/3)
		painter.setBrush(color)
		painter.drawEllipse(self.rect())
	
	def shoot(self,group):
		
		if self.recharge<self.RECHARGE_ITER:
			self.recharge+=1
			return
		if self.goal!=None and self.goal.hp<=0:
			self.goal=None
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
	
	
	
class Place(QGraphicsRectItem):
	WIDTH=20
	def __init__(self,x,y):
		QGraphicsRectItem.__init__(self,0,0,self.WIDTH,self.WIDTH)
		self.setPos(x,y)
		self.tower=None
	def paint(self,painter , StyleOptionGraphicsItem , Widget ):
		painter.setBrush(QColor(0,255,0))
		painter.drawRect(self.rect())

class FirstTower(Tower):
	RADIUS_DAMAGE=150
	RECHARGE_ITER=10
	DAMAGE=5
	color=QColor(255,0,128)
class SecondTower(Tower):
	RADIUS_DAMAGE=100
	RECHARGE_ITER=200
	DAMAGE=50
	color=QColor(255,0,0)
	
class ThirdTower(Tower):
	RADIUS_DAMAGE=400
	RECHARGE_ITER=100
	DAMAGE=20
	color=QColor(0,255,255)
	
class ChooseTower(QGraphicsProxyWidget ):
	FIRST="Первая башня"
	SECOND="Вторая башня"
	THIRD="Третья башня"
	def __init__(self,x,y,place):
		QGraphicsProxyWidget.__init__(self)
		self.setPos(x,y)
		self.place=place
		
		list=QListWidget()
		list.setGeometry(x,y, 100, 100)
		list.addItem(self.FIRST)
		list.addItem(self.SECOND)
		list.addItem(self.THIRD)
		self.setWidget(list)