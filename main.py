import sys
from PySide6 import QtWidgets, QtCore
from qt_material import apply_stylesheet
from sidebar import SideBar

app = QtWidgets.QApplication(sys.argv)

# Set the Material 3 style
apply_stylesheet(app, theme='dark_teal.xml')

# Create the main window
window = QtWidgets.QMainWindow()

# Create the templates
home_template = QtWidgets.QWidget()
about_template = QtWidgets.QWidget()
contact_template = QtWidgets.QWidget()

# Add the templates to a stacked widget
stacked_widget = QtWidgets.QStackedWidget()
stacked_widget.addWidget(home_template)
stacked_widget.addWidget(about_template)
stacked_widget.addWidget(contact_template)

# Create the sidebar
sidebar = SideBar()
sidebar.home_button.clicked.connect(lambda: stacked_widget.setCurrentIndex(0))
sidebar.about_button.clicked.connect(lambda: stacked_widget.setCurrentIndex(1))
sidebar.contact_button.clicked.connect(lambda: stacked_widget.setCurrentIndex(2))

# Add sidebar to a QDockWidget
dock = QtWidgets.QDockWidget()
dock.setWidget(sidebar)
dock.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)

window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)

# Set the stacked widget as the central widget
window.setCentralWidget(stacked_widget)

# Show the window
window.show()

# Run the application
app.exec()
