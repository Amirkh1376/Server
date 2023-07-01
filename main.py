import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QComboBox
import Update_V1_0
import download_V1_0
import run_py_files_V1_0
import upload_py_files_V1_0

access_token = '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'
repository = 'Amirkh1376/Server'
target_branch = 'Test'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Add the output box
        self.output_box = QTextEdit(self)
        self.output_box.move(10, 60)
        self.output_box.setFixedWidth(600)
        self.output_box.setFixedHeight(150)

        # Add the buttons
        self.run_button = Buttons('Run', self, self.output_box)
        self.cancel_button = Buttons('Cancel', self, self.output_box)
        self.apply_button = Buttons('Apply', self, self.output_box)
        self.yes_button = Buttons('Yes', self, self.output_box)
        self.no_button = Buttons('No', self, self.output_box)
        self.no_button = Buttons('Download', self, self.output_box)

        # Add the combo box
        self.combo_box = QComboBox(self)
        repository_list = Update_V1_0.update_files(access_token, repository, target_branch)
        # print(repository_list)
        for repositoryÙ€filename , fileURL in repository_list:
            self.combo_box.addItem(repositoryÙ€filename)
            # print(filename)
        self.combo_box.setFixedWidth(200)
        self.combo_box.setFixedHeight(30)
        self.combo_box.currentIndexChanged.connect(self.on_combo_box_changed)
        
        # Initialize the file URL variable
        self.selected_file_url = ""

        # Store a reference to the apply button
        self.apply_button_ref = self.apply_button

    def on_combo_box_changed(self, index):
        print(f"Selected item: {self.combo_box.itemText(index)}")
        if self.apply_button_ref.button.isChecked():  # Check if the apply button is checked
            self.apply_button_ref.button.setChecked(False)  # Uncheck the button
            self.output_box.append(self.combo_box.itemText(index))
        
        # Get the selected item's file URL
        repository_list = Update_V1_0.update_files(access_token, repository, target_branch)
        _, self.selected_file_url = repository_list[index]

    def on_apply_button_click(self):
        selected_index = self.combo_box.currentIndex()
        selected_item = self.combo_box.itemText(selected_index)
        self.output_box.append(selected_item)
    
    def on_download_button_click(self):
        # print(self.selected_file_url)
        download_V1_0.download_file(self.selected_file_url)
        # print("AA")

    def on_run_button_click(self):
        file_content = run_py_files_V1_0.fetch_contentÙ€py_files(self.selected_file_url)
        print(file_content)
        self.output_box.append(file_content)

class Buttons:
    count = 0

    def __init__(self, button_name, main_window, output_box):
        Buttons.count = Buttons.count + 1
        self.button_name = button_name
        self.button = QPushButton(main_window)
        self.button.setText(self.button_name)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.on_button_click)
        self.button.move((Buttons.count + 1) * 100, 0)
        self.button.setFixedWidth(100)
        self.button.setFixedHeight(30)
        self.output_box = output_box  # Save a reference to the output box

    def on_button_click(self):
        self.output_box.clear()
        if self.button.isChecked():
            print(self.button_name)
            self.button.setChecked(False)  # uncheck the button
            if self.button_name == "Apply":
                self.output_box.parent().on_apply_button_click()
            elif self.button_name == "Download":
                self.output_box.parent().on_download_button_click()
            elif self.button_name == "Run":
                self.output_box.parent().on_run_button_click()
            else:   
                self.output_box.append(self.button_name)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.update()
    window.setWindowTitle("GUI_V1_4")  # App name
    x_CWin = 500  # x screen coordinates where the window will be placed
    y_CWin = 500  # y screen coordinates where the window will be placed
    w_Win = 900  # windowâ€™s width
    h_Win = 300  # windowâ€™s height
    window.setGeometry(x_CWin, y_CWin, w_Win, h_Win)
    window.show()
    sys.exit(app.exec_())
