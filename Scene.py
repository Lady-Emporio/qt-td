
from PyQt5.QtWidgets import QGraphicsScene,QGraphicsEllipseItem,QGraphicsLineItem
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor,QBrush,QPen
from Items import Unit
class Scene(QGraphicsScene):
	mobs=[]
	def __init__(self):
		QGraphicsScene.__init__(self)
		WIDTH=600
		HEIGHT=600
		self.setSceneRect(0, 0, WIDTH, HEIGHT)
		
		self.timer=QTimer()
		self.timer.timeout.connect(self.timerWork)
		self.timer.setInterval(16);
		self.timer.start() 

		
		
		

		self.addPointToPath(100,300)
		self.addPointToPath(300,200)
		self.addPointToPath(150,50)
		


		u=Unit(30,30)
		self.addItem(u)
		self.mobs.append(u)


		self.unit=QGraphicsEllipseItem(100, 100, 50, 50);
		self.unit.setBrush(QColor(0,128,128))
		self.addItem(self.unit);

	def mousePressEvent(self,GraphicsSceneMouseEvent):
		
		PointF =GraphicsSceneMouseEvent.scenePos()
		x=PointF.x()
		y=PointF.y()
		##print([self.unit.rect(),x,y])
		self.unit.setPos(x-125,y-125)
		self.unit.update()
		#u=Unit(x,y)
		#self.addItem(u)


		#self.mobs[0].initGoTo(x,y)
	#	qlist_Elements=self.collidingItems(u)
	#	if (len(qlist_Elements)!=0):
	#		self.removeItem(u)
	#		QGraphicsScene.mousePressEvent(self,GraphicsSceneMouseEvent)


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

		


	def timerWork(self):
		for mob in self.mobs:
			if mob.collidesWithItem(self.unit):
				print("collaps")
				return
			mob.move()
			