from PySide6 import QtWidgets

class SideBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SideBar, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)

        self.home_button = QtWidgets.QPushButton('Home')
        self.about_button = QtWidgets.QPushButton('About')
        self.contact_button = QtWidgets.QPushButton('Contact')

        self.layout.addWidget(self.home_button)
        self.layout.addWidget(self.about_button)
        self.layout.addWidget(self.contact_button)

        self.layout.addStretch()  # add stretchable space at the end
