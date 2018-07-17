from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
import json
from DomNode import DomNode

class Ui_MainWindow(object):
    
    nodeList = []
    
    def toDOM(self, obj):
        if (isinstance(obj,str)):
            json_obj = json.loads(obj)  #use json lib to load our json string
            print(json_obj)
            nodeType = json_obj['nodeType']
            node = DomNode(nodeType)
            if nodeType == 1: #ELEMENT NODE
                node.createElement(json_obj['tagName'])
                
                attributes = json_obj['items']
                for attribute in attributes:
                    if attribute != None:
                        node.setAttributes(attribute[0],attribute[1])
                
            elif nodeType == 3:
                node.createTextNode(json_obj['nodeValue'])
            else:
                return node
            if nodeType == 1:
                childNodes = json_obj['childNodes']
                for i in range(0, len(childNodes)):
                    node.appendChild(self.toDOM(childNodes[i]))
            
            self.nodeList.append(node)
            return node
        else:
            print(obj)
        
    def getDomTree(self):
        for node in self.nodeList:
            if(node.nodeType == 1):
                print (node.tagName, ", ",node.nodeType)
            else:
                print (node.nodeValue, ", ",node.nodeType)


    def someCallback(self, x):
        print("Callback")
        #this callback simply calls toDOM method with x as return value
        self.toDOM(x)

    def runSomeJS(self):
        #read in our DOM js file as string
        file = open("dom.js", 'r')
        jscript = file.read()
        #add additional javascript code to run our DOM js's toJSON method
        jscript += '\ntoJSON(document.getElementsByTagName("BODY")[0]);'
        #finally run the javascript, and wait for it to finish and call the someCallback function.
        self.webView.page().runJavaScript(jscript, self.someCallback)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        #go lazada web page
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl("http://adam.goucher.ca/parkcalc/"))
        self.webView.setObjectName("webView")
        #wait for lazada page to finish loading..., then call runSomeJS function.
        self.webView.loadFinished.connect(self.runSomeJS)
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
