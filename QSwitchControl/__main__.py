"""
MIT License

Copyright (c) 2021 Parsa.py

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

from Modern.QSwitchControl import SwitchControl as ModernSwitchControl
from Classic.QSwitchControl import SwitchControl as ClassicSwitchControl


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.resize(400, 400)
		self.setWindowTitle("SwitchControl test")
		self.setStyleSheet("""
		background-color: #222222;
		""")
		classic_switch_control = ClassicSwitchControl()
		classic_switch_control.setToolTip("SwitchControl with Classic style")
		modern_switch_control = ModernSwitchControl()
		modern_switch_control.setToolTip("SwitchControl with Modern style")
		h_box = QHBoxLayout()
		h_box.addWidget(classic_switch_control, Qt.AlignCenter, Qt.AlignCenter)
		h_box.addWidget(modern_switch_control, Qt.AlignCenter, Qt.AlignCenter)
		self.setLayout(h_box)
		self.show()


app = QApplication(sys.argv)
form = Form()
if __name__ == '__main__':
	sys.exit(app.exec_())
