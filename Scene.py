
from PyQt5.QtWidgets import QGraphicsScene,QGraphicsEllipseItem,QGraphicsLineItem
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor,QBrush,QPen
from Items import Unit
from tower import Tower
class Scene(QGraphicsScene):
	MAXHP=20
	HP=MAXHP
	mobs=[]
	towers=[]
	createPos=[100,100]
	def __init__(self):
		QGraphicsScene.__init__(self)
		
		
		WIDTH=480
		HEIGHT=600
		self.setSceneRect(0, 0, WIDTH, HEIGHT)
		


		
		
		

		
		self.addPointToPath(self.createPos[0],self.createPos[1])
		self.addPointToPath(400,100)
		self.addPointToPath(400,200)
		self.addPointToPath(200,200)
		self.addPointToPath(200,300)
		self.addPointToPath(100,300)
		

		self.createUnit()

		self.timer=QTimer()
		self.timer.timeout.connect(self.timerWork)
		self.timer.setInterval(16);
		self.timer.start() 

	def mousePressEvent(self,GraphicsSceneMouseEvent):
		
		PointF =GraphicsSceneMouseEvent.scenePos()
		x=PointF.x()-Tower.WIDTH/2
		y=PointF.y()-Tower.HEIGHT/2
		self.createTower(x,y)
		
	def unitGoToLastPoint(self,unit):
		if unit.hp>0:
			self.HP-=unit.DAMAGE
			self.removeItem(unit)
			self.mobs.remove(unit)
			view=self.views()[0]
			view.hpChange.emit()
	def addPointToPath(self,x,y):
		widthEllipse=20;
		heightEllipse=20;
		EllipseX=x-widthEllipse/2
		EllipseY=y-heightEllipse/2

		if(len(Unit.PATH)!=0):
			lastPoint=Unit.PATH[len(Unit.PATH)-1]
			line=QGraphicsLineItem(lastPoint[0],lastPoint[1],x,y)
			line.setPen(QPen(QBrush(QColor(128,0,0)),5))
			self.addItem(line);
		Unit.PATH.append([x,y])	

		item =QGraphicsEllipseItem(EllipseX, EllipseY, widthEllipse, heightEllipse);
		item.setBrush(QColor(0,0,128))
		self.addItem(item);

	def createUnit(self):
		u=Unit(self.createPos[0],self.createPos[1])
		self.addItem(u)
		self.mobs.append(u)

	def createTower(self,x,y):
		t=Tower(x,y)
		self.addItem(t)
		self.towers.append(t)
	def timerWork(self):
		for tower in self.towers:
			tower.update(self.mobs)
		for mob in self.mobs:
			mob.move()
		
			