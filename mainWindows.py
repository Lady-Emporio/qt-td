
from PyQt5.QtWidgets import (QMainWindow,QWidget,QHBoxLayout,QVBoxLayout,
QListView)
from MyGraphicView import MyGraphicView
class CentalWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		mainLaoyt=QHBoxLayout(self)
		leftLayout=QVBoxLayout()
		rightLayout=QVBoxLayout()
		self.setLayout(mainLaoyt)
		mainLaoyt.addLayout(leftLayout)
		mainLaoyt.addLayout(rightLayout)
		
		LISTWIDTH=100
		list=QListView(self)
		list.setMaximumWidth(LISTWIDTH)
		rightLayout.addWidget(list)
		sceneView=MyGraphicView()
		leftLayout.addWidget(sceneView)
		

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		centralWidget=CentalWidget()
		self.setCentralWidget(centralWidget);
		self.show()