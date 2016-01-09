# Copyright (C) Daniel R. H. Jensen 

# Information
__author__ = "Daniel R. H. Jensen"
__copyright__ = "Copyright (C) Daniel Jensen"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__version__ = "1.0"

# Python imports
import os
from os.path import expanduser
import glob
import shutil
import sys

# PyQt4 imports
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class window(QMainWindow):
    
    def __init__(self):

        super().__init__()
        QMainWindow.__init__(self)

        self.setMinimumSize(400,500)
        self.setMaximumSize(400,500)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Desktop Sorter")
        
        self.setWindowIcon(QIcon("mainIcon.png"))

        self.home()
      
    def home(self):

        self.main_layout()

    def main_layout(self):

        # The plastique style
        self.plq_style = QStyleFactory.create("plastique")

        # The widgets

        # The button font
        sort_btn_font = QFont()
        sort_btn_font.setPointSize(20)

        # The sort button
        self.sort_btn = QPushButton("Sort Desktop")
        self.sort_btn.setFont(sort_btn_font)
        self.sort_btn.setStyle(self.plq_style)
        self.sort_btn.clicked.connect(self.sort_desktop)

        # The advanced mode check box
        self.advm_checkBox = QCheckBox("Advanced Mode")
        self.advm_checkBox.setStyle(self.plq_style)
        # If check box is pressed / state changes
        self.advm_checkBox.stateChanged.connect(self.toggleTextEdit)

        # The text edit font
        input_txtedit_font = QFont() 
        input_txtedit_font.setPointSize(10)
        input_txtedit_font.setFamily("system")

        # Input text edit
        self.input_txtedit = QTextEdit()
        self.input_txtedit.setReadOnly(True)
        self.input_txtedit.setStyle(self.plq_style)
        self.input_txtedit.setFont(input_txtedit_font)
        self.input_txtedit.hide()

        # The layout
        self.initial_layout = QGridLayout()

        self.initial_layout.addWidget(self.sort_btn, 1, 0)

        self.initial_layout.addWidget(self.input_txtedit, 2, 0)

        self.initial_layout.addWidget(self.advm_checkBox, 3, 0)

        centralWidget = QWidget()

        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(self.initial_layout)

        self.show()

    def toggleTextEdit(self, state):

        # If the check box is pressed
        if state == Qt.Checked:
            self.input_txtedit.show()
        # While the check box isn't checked
        else:
            self.input_txtedit.hide()

    def sort_desktop(self):
        # Makes a space between the inputs
        space = "\n"

        # Clears the textEdit for text - mainly used for clicking more than once at the pushButton
        self.input_txtedit.clear()

        global _home
        _home = expanduser("~")

        self.input_txtedit.insertPlainText("User directory:" + space)

        # Displays the Home directory
        self.input_txtedit.insertPlainText(_home + space)

        # Displays the Desktop directory
        global home
        home = _home + '/Desktop/'

        # Displays the files on the Desktop
        self.input_txtedit.insertPlainText(space + 'Files in Desktop:' + space)
        for name in glob.glob(home + r'*.*'):
            self.input_txtedit.insertPlainText(name + space)

        self.input_txtedit.insertPlainText(space)

        # Displays the directories on the Desktop
        self.input_txtedit.insertPlainText("Directories in Desktop:" + space)
        for dir_ in glob.glob(home + r'*/'):
            self.input_txtedit.insertPlainText(dir_ + space)

        self.input_txtedit.insertPlainText(space)

        # If a folder with the name, Text Documents, doesn't exist on the Desktop it will create it
        # The Text Documents folder contains text files, like .txt and/or .html
        if not os.path.exists(home + 'Text Documents'):
            os.makedirs(home + 'Text Documents')

        # If a folder with the name, Programs, doesn't exist on the Desktop it will create it
        if not os.path.exists(home + 'Programs'):
            os.makedirs(home + 'Programs')

        # If a folder with the name, Images, doesn't exist on the Desktop it will create it
        if not os.path.exists(home + 'Images'):
            os.makedirs(home + 'Images')

        # If a folder with the name, Media, doesn't exist on the Desktop it will create it
        # The Medias folder contains video and audio files
        if not os.path.exists(home + 'Medias'):
            os.makedirs(home + 'Medias')

        # The directory of the Text Documents folder
        dest_dir_files = home + 'Text Documents'

        # The directory of the Programs folder
        dest_dir_programs = home + 'Programs'

        # The directory of the Images folder
        dest_dir_images = home + 'Images'

        # The directory of the Medias folder
        dest_dir_medias = home + 'Medias'

        # Displays the files that have been moved under the process
        self.input_txtedit.insertPlainText("Files moved:" + space)

        # The function for moving program files in the Programs folder, and displaying the files that have been moved
        # Lnk
        for program in glob.glob(home + r"*.lnk"):
            self.input_txtedit.insertPlainText(program + space)

            # Tries to move a file to the Programs folder
            try:
                shutil.move(program, dest_dir_programs)

            # If the moved program file have the same name+extension as a program file in the folder...
            except:
                # it will Display it and will abort the moving process
                self.input_txtedit.insertPlainText("File already exists!: " + program + space)
                pass

        # Exe
        for program in glob.glob(home + r"*.exe"):
            self.input_txtedit.insertPlainText(program + space)

            try:
                shutil.move(program, dest_dir_programs)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + program + space)

        # url
        for program in glob.glob(home + r"*.url"):
            self.input_txtedit.insertPlainText(program + space)

            try:
                shutil.move(program, dest_dir_programs)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + program + space)

        # pif
        for program in glob.glob(home + r"*.pif"):
            self.input_txtedit.insertPlainText(program + space)

            try:
                shutil.move(program, dest_dir_programs)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + program + space)

        # shs
        for program in glob.glob(home + r"*.shs"):
            self.input_txtedit.insertPlainText(program + space)

            try:
                shutil.move(program, dest_dir_programs)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + program + space)

        # scf
        for program in glob.glob(home + r"*.scf"):
            self.input_txtedit.insertPlainText(program + space)

            try:
                shutil.move(program, dest_dir_programs)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + program + space)

        # xnk
        for program in glob.glob(home + r"*.xnk"):
            self.input_txtedit.insertPlainText(program + space)

            try:
                shutil.move(program, dest_dir_programs)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + program + space)


        # The image file extensions array
        image = ['*.jpeg', '*.png', '*.tif', '*.gif', '*.ico']

        # The function for moving the image files in the Images folder, and displaying the files that have been moved
        # Jpeg
        for image in glob.glob(home + r"" + image[0]):
            self.input_txtedit.insertPlainText(image + space)

            # Tries to move a file to the Images folder
            try:
                shutil.move(image, dest_dir_images)

            # If the move image file have the same name+extension as a image file in the folder...
            except:
                # It will display it and will abort the moveing process
                self.input_txtedit.insertPlainText("File already exists!: " + image + space)

        # Png
        for image in glob.glob(home + r"" + image[1]):
            self.input_txtedit.insertPlainText(image + space)

            try:
                shutil.move(image, dest_dir_images)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + image + space)

        # Tif
        for image in glob.glob(home + r"" + image[2]):
            self.input_txtedit.insertPlainText(image + space)

            try:
                shutil.move(image, dest_dir_images)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + image + space)

        # Gif
        for image in glob.glob(home + r"" + image[3]):
            self.input_txtedit.insertPlainText(image + space)

            try:
                shutil.move(image, dest_dir_images)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + image + space)

        # Ico
        for image in glob.glob(home + r"" + image[4]):
            self.input_txtedit.insertPlainText(image + space)

            try:
                shutil.move(image, dest_dir_images)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + image + space)


        # Files
        files = ['*.html', '*.txt', '*.py', '*.odt', '*.tmp', '*.doc', '*.rtf', '*.docx', '*.pdf', '*.so', '*.plain']

        # Html
        for file in glob.glob(home + r'' + files[0]):
            self.input_txtedit.insertPlainText(file + space)

            try:
                shutil.move(file, dest_dir_files)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + file + space)

        # Txt
        for file in glob.glob(home + r'' + files[1]):
            self.input_txtedit.insertPlainText(file + space)

            try:
                shutil.move(file, dest_dir_files)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + file + space)

        # Py
        for file in glob.glob(home + r'' + files[2]):
            self.input_txtedit.insertPlainText(file + space)

            try:
                shutil.move(file, dest_dir_files)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + file + space)

        # Odt
        for file in glob.glob(home + r'' + files[3]):
            self.input_txtedit.insertPlainText(file + space)

            try:
                shutil.move(file, dest_dir_files)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + file + space)

        # Tmp
        for file in glob.glob(home + r'' + files[4]):
            self.input_txtedit.insertPlainText(file + space)

            try:
                shutil.move(file, dest_dir_files)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + file + space)

        # Doc
        for file in glob.glob(home + r'' + files[5]):
            self.input_txtedit.insertPlainText(file + space)

            try:
                shutil.move(file, dest_dir_files)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + file + space)

        # Rtf
        for file in glob.glob(home + r'' + files[6]):
            self.input_txtedit.insertPlainText(file + space)

            try:
                shutil.move(file, dest_dir_files)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + file + space)

        # Docx
        for file in glob.glob(home + r'' + files[7]):
            self.input_txtedit.insertPlainText(file + space)

            try:
                shutil.move(file, dest_dir_files)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + file + space)

        # Pdf
        for file in glob.glob(home + r'' + files[8]):
            self.input_txtedit.insertPlainText(file + space)

            try:
                shutil.move(file, dest_dir_files)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + file + space)

        # So
        for file in glob.glob(home + r'' + files[9]):
            self.input_txtedit.insertPlainText(file + space)

            try:
                shutil.move(file, dest_dir_files)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + file + space)

        # Plain
        for file in glob.glob(home + r'' + files[10]):
            self.input_txtedit.insertPlainText(file + space)

            try:
                shutil.move(file, dest_dir_files)

            except:
                self.input_txtedit.insertPlainText('File already exists!: ' + file + space)


        # Media
        medias = ['*.mp3', '*.mp4', '*.webm',
                '*.mkv', '*.flv', '*.vob', '*.gif',
                '*.mpg', '*.io']

        for media in glob.glob(home + r"" + medias[0]):

            self.input_txtedit.insertPlainText(media + space)

            try:
                shutil.move(media, dest_dir_medias)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + media + space)

        # Mp3
        for media in glob.glob(home + r"" + medias[1]):

            self.input_txtedit.insertPlainText(media + space)

            try:
                shutil.move(media, dest_dir_medias)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + media + space)

        for media in glob.glob(home + r"" + medias[2]):

            self.input_txtedit.insertPlainText(media + space)

            try:
                shutil.move(media, dest_dir_medias)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + media + space)

        for media in glob.glob(home + r"" + medias[3]):

            self.input_txtedit.insertPlainText(media + space)

            try:
                shutil.move(media, dest_dir_medias)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + media + space)

        for media in glob.glob(home + r"" + medias[4]):

            self.input_txtedit.insertPlainText(media + space)

            try:
                shutil.move(media, dest_dir_medias)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + media + space)

        for media in glob.glob(home + r"" + medias[5]):

            self.input_txtedit.insertPlainText(media + space)

            try:
                shutil.move(media, dest_dir_medias)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + media + space)

        for media in glob.glob(home + r"" + medias[6]):

            self.input_txtedit.insertPlainText(media + space)

            try:
                shutil.move(media, dest_dir_medias)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + media + space)

        for media in glob.glob(home + r"" + medias[7]):

            self.input_txtedit.insertPlainText(media + space)

            try:
                shutil.move(media, dest_dir_medias)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + media + space)

        for media in glob.glob(home + r'' + medias[8]):
            self.input_txtedit.insertPlainText(media + space)

            try:
                shutil.move(media, dest_dir_medias)

            except:
                self.input_txtedit.insertPlainText("File already exists!: " + media + space)

        # When the sorting is done
        self.sortingDone()

    def sortingDone(self):
        # Message box displaying, that the sorting is done
        message_box = QMessageBox.about(self, "Sorting Process", "The Sorting Is Done")
        


# For running the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = window()
    window.show()
    window.raise_()
    sys.exit(app.exec_())
