from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtGui import QColor ,QFontMetrics ,QVector2D
from PyQt5.QtCore import Qt,QRectF,pyqtSignal
class Unit(QGraphicsRectItem):
	WIDTH=30
	HEIGHT=30
	PATH=[]
	SPEED=1;
	DAMAGE=1;
	def __init__(self,x,y):
	
		self.isAlive=True
		QGraphicsRectItem.__init__(self,0,0,self.WIDTH,self.HEIGHT)

		
		self.hp=100
		
		self.setPos(x-self.WIDTH/2,y-self.HEIGHT/2)

		self.point=0;
		self.needGoTo=QVector2D(0,0)
		self.moveX=0;
		self.moveY=0;

		self.actuallyX=self.x();
		self.actuallyY=self.y();
		
		if self.point<=len(self.PATH)-1:
			needGoTo=self.PATH[self.point]
			self.initGoTo(needGoTo[0],needGoTo[1])

	def paint(self,painter , StyleOptionGraphicsItem , Widget ):
		painter.setBrush(QColor(0,128,0))
		painter.drawRect(self.rect())
		
		painter.setPen(QColor(255,0,0))
		
		rect=QRectF(0,0,self.WIDTH,self.HEIGHT)
		painter.drawText(rect, Qt.AlignHCenter|Qt.AlignTop, str(self.hp))

	def initGoTo(self,x,y):

		nowPosition=QVector2D(self.x(),self.y())
		self.needGoTo=QVector2D(x-self.WIDTH/2,y-self.HEIGHT/2)
		distance=nowPosition.distanceToPoint(self.needGoTo)
		iterTimeToGoToGoal=distance/self.SPEED;

		if iterTimeToGoToGoal==0:
			self.moveX=0;
			self.moveY=0;
			return

		needGo=self.needGoTo-nowPosition
		needGoToX=needGo.x();
		needGoToY=needGo.y();

		self.moveX=needGoToX/iterTimeToGoToGoal
		self.moveY=needGoToY/iterTimeToGoToGoal

	def move(self):
		if not self.isAlive:
			return;
		if self.x()==self.needGoTo.x() and self.y()==self.needGoTo.y():
			self.point+=1
			if self.point<=len(self.PATH)-1:
				needGoTo=self.PATH[self.point]
				self.initGoTo(needGoTo[0],needGoTo[1])
			else:
				self.isAlive=False
				self.scene().unitGoToLastPoint(self)
				
		if self.moveX==0 and self.moveY==0:
			return 
		if self.moveX>0:
			if self.actuallyX>=self.needGoTo.x():
				self.actuallyX=self.needGoTo.x()
				self.moveX=0
		elif self.moveX<0:
			if self.actuallyX<=self.needGoTo.x():
				self.actuallyX=self.needGoTo.x()
				self.moveX=0

		if self.moveY>0:
			if self.actuallyY>=self.needGoTo.y():
				self.actuallyY=self.needGoTo.y()
				self.moveY=0
		elif self.moveY<0:
			if self.actuallyY<=self.needGoTo.y():
				self.actuallyY=self.needGoTo.y()
				self.moveY=0


		self.actuallyX+=self.moveX
		self.actuallyY+=self.moveY
		self.setPos(self.actuallyX,self.actuallyY)
		self.update()
		
		
	