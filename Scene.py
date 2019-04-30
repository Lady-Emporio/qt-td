
from PyQt5.QtWidgets import QGraphicsScene,QGraphicsEllipseItem,QGraphicsLineItem,QListWidget ,QSizePolicy
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor,QBrush,QPen,QTransform
from Items import Unit
from tower import Tower,Place,ChooseTower,FirstTower,SecondTower,ThirdTower
class Scene(QGraphicsScene):
	MAXHP=20
	HP=MAXHP
	mobs=[]
	towers=[]
	createPos=[100,100]
	widget=None;
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
		
		self.createPlace(190,120)
		self.createPlace(370, 120)
		self.createPlace(370,180)
		self.createPlace(225,180)
		self.createPlace(225,280)
		self.createPlace(300,150)
		
		
		self.timer=QTimer()
		self.timer.timeout.connect(self.timerWork)
		self.timer.setInterval(16);
		self.timer.start() 

	
	
	def itemClicked(self,qListWidgetItem ):
		text=qListWidgetItem.text()
		if text==ChooseTower.FIRST:
			self.createTypeTower(FirstTower,self.widget.place.x(),self.widget.place.y())
		elif text==ChooseTower.SECOND:
			self.createTypeTower(SecondTower,self.widget.place.x(),self.widget.place.y())
		else:
			self.createTypeTower(ThirdTower,self.widget.place.x(),self.widget.place.y())
				
		
	def mousePressEvent(self,GraphicsSceneMouseEvent):
		
		PointF =GraphicsSceneMouseEvent.scenePos()

		deviceTransform=QTransform()
		item=self.itemAt(PointF, deviceTransform)
		if isinstance(item,ChooseTower) :
			QGraphicsScene.mousePressEvent(self,GraphicsSceneMouseEvent)
			return
		if isinstance(item,Place):
			if item.tower==None:
				if self.widget!=None:
					self.removeItem(self.widget)
					self.widget=None
				
				# list=QListWidget()
				# list.setGeometry(PointF.x(),PointF.y(), 100, 100)
				# list.addItem("Первая башня")
				# list.addItem("Вторая башня")
				# list.addItem("Третья башня")
				# self.widget=self.addWidget(list)
				self.widget=ChooseTower(PointF.x(),PointF.y(),item);
				self.addItem(self.widget)
				
				self.widget.widget().itemClicked.connect(self.itemClicked)
				return
		else:
			if self.widget!=None and item!=self.widget:
				self.removeItem(self.widget)
				self.widget=None
				return

		QGraphicsScene.mousePressEvent(self,GraphicsSceneMouseEvent)
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

	def createPlace(self,x,y):
		r_x=x-Place.WIDTH/2
		r_y=y-Place.WIDTH/2
		p=Place(r_x,r_y)
		self.addItem(p)
		
	def createTower(self,x,y):
		r_x=x-Tower.RADIUS_DAMAGE/2
		r_y=y-Tower.RADIUS_DAMAGE/2
		t=Tower(r_x,r_y)
		self.addItem(t)
		self.towers.append(t)
	def timerWork(self):
		for tower in self.towers:
			tower.shoot(self.mobs)
		for mob in self.mobs:
			mob.move()
		
	def createTypeTower(self,typeTower,x,y):
		r_x=x-typeTower.RADIUS_DAMAGE/2+Place.WIDTH/2
		r_y=y-typeTower.RADIUS_DAMAGE/2+Place.WIDTH/2
		t=typeTower(r_x,r_y)
		self.addItem(t)
		self.towers.append(t)
			
		self.widget.place.tower=t
			
		self.widget.place.setZValue(-2)
		self.widget.place.tower.setZValue(-1)
		if self.widget!=None:
			self.removeItem(self.widget)
			self.widget.deleteLater()#Не понимаю, что тут происходит, но без этого не работает.
			# Возможно это не в основном цикле происходит.
			self.widget=None