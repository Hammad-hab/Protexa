from application import QApplication, Application
import qdarktheme
import sys

def exec_app():
    
	qapp = QApplication(sys.argv)
	qdarktheme.setup_theme()
	app = Application()
	app.showMaximized()
	app.show()
	sys.exit(qapp.exec())

if __name__ == "__main__":
	exec_app()
