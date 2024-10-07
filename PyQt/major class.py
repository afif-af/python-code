import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      self.initUI()

   def initUI(self):
      self.setWindowTitle("PyQt Major Classes Demo")

      # Create QLabel
      label = QLabel("Hello, PyQt!")

      # Create QPushButton
      button = QPushButton("Click Me")
      button.clicked.connect(self.onButtonClick)

      # Create a vertical layout
      layout = QVBoxLayout()
      layout.addWidget(label)
      layout.addWidget(button)

      # Create a central widget and set the layout
      central_widget = QWidget()
      central_widget.setLayout(layout)
      self.setCentralWidget(central_widget)

   def onButtonClick(self):
      print("Button clicked!")

if __name__ == "__main__":
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec())