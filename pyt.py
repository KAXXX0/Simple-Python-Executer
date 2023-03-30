import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create layout for window
        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()
        
        # Create label for instructions
        instructions_label = QLabel("Type Python code below and press 'Run' to execute it:")
        top_layout.addWidget(instructions_label)
        
        # Create text editor for code input
        self.code_editor = QTextEdit()
        top_layout.addWidget(self.code_editor)
        
        # Create button to run code
        run_button = QPushButton("Run")
        run_button.clicked.connect(self.run_code)
        bottom_layout.addWidget(run_button)
        
        # Create text editor for output
        self.output_editor = QTextEdit()
        self.output_editor.setReadOnly(True)
        bottom_layout.addWidget(self.output_editor)
        
        # Add layouts to main layout
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)
        
        # Set main layout for window
        self.setLayout(main_layout)
    
    def run_code(self):
        code = self.code_editor.toPlainText()
        try:
            exec(code)
        except Exception as e:
            self.output_editor.setText(str(e))

if __name__ == '__main__':
    # Create application instance
    app = QApplication(sys.argv)
    
    # Create main window
    window = MainWindow()
    window.show()
    
    # Run application
    sys.exit(app.exec_())