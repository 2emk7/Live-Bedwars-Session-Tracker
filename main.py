import sys
import getstats
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTimer
from GUI import Ui_Form
from threading import Thread


class MainWindow(QWidget):
    def __init__(self):

        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tracker_thread = None

        self.ui.EnterNameBox.textChanged.connect(self.username_changed)
        self.ui.ResetButton.clicked.connect(self.reset_pressed)

        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_stats)
        self.update_timer.start(500) 


    def reset_pressed(self):
        getstats.stats = [0, 0, 0, 0, 0, 0]
        self.ui.EnterNameBox.clear()
        getstats.win_list.clear()
        getstats.game_status = 0
        getstats.isRunning = False
        print("Stats reset")
    
    def update_stats(self):
        import getstats
        stats = getstats.stats

        self.ui.WINS_Label_2.setText(str(stats[0]))
        self.ui.LOSSES_Label_2.setText(str(stats[1]))
        self.ui.BD__Label_2.setText(str(stats[2]))
        self.ui.BL__Label_2.setText(str(stats[3]))
        self.ui.FK__Label_2.setText(str(stats[4]))
        self.ui.FD__Label_2.setText(str(stats[5]))
        fkdr = stats[4] / stats[5] if stats[5] != 0 else stats[4]
        wlr = stats[0] / stats[1] if stats[1] != 0 else stats[0]

        self.ui.FKDR__Label_2.setText(str(round(fkdr, 2)))
        self.ui.WLR_Label_2.setText(str(round(wlr, 2)))


    def username_changed(self, text):
        getstats.username = text.strip()

        #start tracker
        if getstats.username and self.tracker_thread is None:
            getstats.isRunning = True
            self.tracker_thread = Thread(
                target=getstats.start_Tracker,
                daemon=True
            )
            self.tracker_thread.start()

    def closeEvent(self, event):
        print("GUI is closing!")
        getstats.isRunning = False
        event.accept()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
