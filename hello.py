import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QTabWidget):
    def __init__(self):
        super().__init__()
        
        #add title
        self.setWindowTitle("hello world!")
        
        #set vertical layout
        self.setLayout(qtw.QVBoxLayout())
        
        #set layout
        #self.setLayout(qtw.QHBoxLayout())
        
        #create layout
        my_label=qtw.QLabel("Hello!")
        
        #change font 
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.layout().addWidget(my_label)
        
        #create entry box
        my_entry=qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)
        
        #create a button
        my_button=qtw.QPushButton("Press Me!", 
                    clicked=lambda: press_it())
        self.layout().addWidget(my_button)
        
       
        
        def press_it():
            my_label.setText(f'Hello {my_entry.text()}')
            #clear entry box
            my_entry.setText("elif")
            
        self.show()
            
app=qtw.QApplication([])
mw=MainWindow()
app.exec_()