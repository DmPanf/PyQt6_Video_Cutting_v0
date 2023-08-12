import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QSlider, QLineEdit, QPushButton, QFileDialog)
from PyQt6.QtCore import Qt, QTimer
import cv2

class VideoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.video_path = None
        self.cap = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.play_video)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Video Slider
        self.slider = QSlider(Qt.Orientation.Horizontal)
        layout.addWidget(self.slider)

        # Info Panel
        info_layout = QHBoxLayout()
        
        self.start_time = QLineEdit("0")
        self.end_time = QLineEdit("0")
        self.skip_frames = QLineEdit("1")
        self.output_name = QLineEdit("./OUTPUT/")

        info_layout.addWidget(QLabel("Start Time:"))
        info_layout.addWidget(self.start_time)
        info_layout.addWidget(QLabel("End Time:"))
        info_layout.addWidget(self.end_time)
        info_layout.addWidget(QLabel("Skip Frames:"))
        info_layout.addWidget(self.skip_frames)
        info_layout.addWidget(QLabel("Output Name:"))
        info_layout.addWidget(self.output_name)
        
        layout.addLayout(info_layout)

        # Button Panel
        btn_layout = QHBoxLayout()
        
        self.load_btn = QPushButton("VIDEO LOAD")
        self.play_btn = QPushButton("PLAY/STOP")
        self.cut_btn = QPushButton("cutting frames")
        self.return_btn = QPushButton("RETURN")

        self.load_btn.clicked.connect(self.load_video)
        self.play_btn.clicked.connect(self.toggle_play)
        self.cut_btn.clicked.connect(self.cut_frames)
        self.return_btn.clicked.connect(self.return_values)

        btn_layout.addWidget(self.load_btn)
        btn_layout.addWidget(self.play_btn)
        btn_layout.addWidget(self.cut_btn)
        btn_layout.addWidget(self.return_btn)
        
        layout.addLayout(btn_layout)

        self.setLayout(layout)
        self.setWindowTitle('Video App')
        self.show()

    def load_video(self):
        self.video_path, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi)")
        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
            self.slider.setMaximum(int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)))

    def toggle_play(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(30)

    def play_video(self):
        ret, frame = self.cap.read()
        if ret:
            # Note: need to implement video display using QLabel and QPixmap or another method.
            # This example only focuses on GUI layout.
            pass
        else:
            self.timer.stop()

    def cut_frames(self):
        # Note: need to implement frame saving using OpenCV
        pass

    def return_values(self):
        self.start_time.setText("0")
        self.end_time.setText("0")
        self.skip_frames.setText("1")
        self.output_name.setText("./OUTPUT/")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = VideoApp()
    sys.exit(app.exec())
