
from PyQt5.QtWidgets import (QMainWindow,QWidget,QHBoxLayout,QVBoxLayout,
QListView,QLabel,QPushButton)
from MyGraphicView import MyGraphicView
class CentalWidget(QWidget):

	
	def __init__(self):
		QWidget.__init__(self)
		
		self.sceneView=MyGraphicView()
		
		self.score=QLabel("")
		self.score.setMaximumWidth(40)
		self.score.setStyleSheet("QLabel {"
                             "border-style: solid;"
                             "border-width: 1px;"
                             "border-color: black; "
                             "}");
							 
		addMob=QPushButton("create unit")
		addMob.clicked.connect(self.createUnit)
		mainLaoyt=QHBoxLayout(self)
		leftLayout=QVBoxLayout()
		left_Top_Layout=QHBoxLayout()
		rightLayout=QVBoxLayout()
		self.setLayout(mainLaoyt)
		mainLaoyt.addLayout(leftLayout)
		mainLaoyt.addLayout(rightLayout)
		
		LISTWIDTH=100
		list=QListView(self)
		list.setMaximumWidth(LISTWIDTH)
		rightLayout.addWidget(list)
		
		
		left_Top_Layout.addWidget(self.score)
		left_Top_Layout.addWidget(addMob)
		leftLayout.addLayout(left_Top_Layout)
		leftLayout.addWidget(self.sceneView)
		
		
		
		
		self.changeHP()
		
	def createUnit(self):
		self.sceneView.scene().createUnit()
	def changeHP(self):
		text="HP:"+str(self.sceneView.scene().HP)
		self.score.setText(text)
class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		centralWidget=CentalWidget()
		self.setCentralWidget(centralWidget);
		self.show()