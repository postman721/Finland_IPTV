#!/usr/bin/env python3
# Finland IPTV v.1.0
# Copyright (c) 2024 JJ Posti <techtimejourney.net>
# This program comes with ABSOLUTELY NO WARRANTY; for details see: http://www.gnu.org/copyleft/gpl.html
# This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991

import sys
import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import re

# URL of the Finland IPTV M3U (Markdown) file
IPTV_URL = "https://raw.githubusercontent.com/Free-TV/IPTV/refs/heads/master/lists/finland.md"

# Function to download and parse the IPTV M3U Markdown file
def get_channels():
    try:
        response = requests.get(IPTV_URL, timeout=10)  # Add a timeout to prevent hanging
        response.raise_for_status()  # Raise an exception for HTTP errors
        content = response.text
        channels = []

        # Regular expression to match channel names and URLs inside table-like structures
        pattern = re.compile(r'([^\|]+)\|\s*\[[^\]]+\]\((http[^\s\)]+)')

        # Extract channel name and URL
        for match in pattern.findall(content):
            channel_name, channel_url = match
            # Clean up the channel name, removing unwanted characters like @, Ⓖ, and extra spaces
            channel_name = re.sub(r'[Ⓖ@]+$', '', channel_name).strip()  # Remove trailing @ and Ⓖ symbols
            channel_name = re.sub(r'[^a-zA-Z0-9\s]+$', '', channel_name).strip()  # Remove any remaining non-alphanumerics
            channels.append((channel_name, channel_url.strip()))

        return channels

    except requests.exceptions.RequestException as e:
        print(f"Error fetching channels: {e}")
        return []  # Return an empty list if there's an error


# PyQt5 Application class
class IPTVApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finland IPTV")
        self.setGeometry(100, 100, 800, 600)

        # Center the window on the screen
        self.center_window()

        # Set up layout
        layout = QVBoxLayout()

        # Channel Drop-down (ComboBox) with smaller size
        self.channel_combo = QComboBox()
        self.channel_combo.setFixedSize(228, 30)  # Set smaller size for ComboBox
        layout.addWidget(self.channel_combo)

        # QVideoWidget for video playback
        self.video_widget = QVideoWidget()
        layout.addWidget(self.video_widget)

        # Create a media player object
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(self.video_widget)

        # Connect error handling for media playback
        self.media_player.error.connect(self.handle_media_error)

        # Set layout to the main widget
        self.setLayout(layout)

        # Load channels and populate combo box
        self.channels = get_channels()
        if not self.channels:
            QMessageBox.critical(self, "Error", "No channels found or failed to load channels.")
            sys.exit(1)

        for channel_name, _ in self.channels:
            self.channel_combo.addItem(channel_name)  # Add only the cleaned-up channel name

        # Connect the combo box selection change to the play function
        self.channel_combo.currentIndexChanged.connect(self.on_channel_selected)

        # Start playing the first channel by default
        self.channel_combo.setCurrentIndex(0)

        # Set full screen toggle flag
        self.is_full_screen = False

        # Apply custom stylesheet (CSS-like styling)
        self.apply_stylesheet()

    def center_window(self):
        """ Center the window on the screen. """
        screen = QDesktopWidget().availableGeometry().center()
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(screen)
        self.move(frame_geometry.topLeft())

    def on_channel_selected(self, index):
        """ Play the selected channel from the combo box. """
        if index >= 0:
            channel_url = self.channels[index][1]  # Get the URL for the selected channel
            self.play_channel(channel_url)

    def play_channel(self, url):
        """ Set the media content to the player and start playing. """
        if url:
            self.media_player.setMedia(QMediaContent(QUrl(url)))
            self.media_player.play()
        else:
            QMessageBox.critical(self, "Error", "Failed to load the media content.")

    def handle_media_error(self):
        """ Handle media playback errors. """
        error_message = self.media_player.errorString()
        if error_message:
            QMessageBox.critical(self, "Media Error", f"Playback error: {error_message}")

    def toggle_full_screen(self):
        """ Toggle between full-screen and windowed mode. """
        if self.is_full_screen:
            self.showNormal()  # Exit full screen
            self.channel_combo.show()  # Show the extra widgets
        else:
            self.showFullScreen()  # Enter full screen
            self.channel_combo.hide()  # Hide the extra widgets
        self.is_full_screen = not self.is_full_screen

    def keyPressEvent(self, event):
        """ Bind F11 to toggle full-screen mode. """
        if event.key() == Qt.Key_F11:
            self.toggle_full_screen()

    def apply_stylesheet(self):
        """ Apply styles to the entire application. """
        self.setStyleSheet("""            
            * { color: white                /* White as a default text color */ }
            
            QWidget {
                background-color: #2E3B4E;  /* Dark background for the main window */
            }
            QComboBox {
                font-size: 14px;
                padding: 5px;
                border: 1px solid #9DAAB6;  /* Light gray border for better contrast */
                border-radius: 5px;
                background-color: #4A5B70;  /* Darker background for the combo box */
                color: #FFFFFF;  /* White text for clarity */
            }
            QComboBox::drop-down {
                border: 0px;
                color: #FFFFFF;
            }
            QComboBox QAbstractItemView {
                background-color: blue;  /* White background for dropdown items */
                selection-background-color: #57697C;  /* Slightly lighter for selected items */
                selection-color: #FFFFFF;  /* White text when selected */
                color: #000000;  /* Black text for unselected items */
                border: 1px solid #9DAAB6;  /* Light gray border around dropdown */
            }
            QPushButton {
                font-size: 14px;
                padding: 7px;
                border: 1px solid #9DAAB6;
                border-radius: 5px;
                background-color: #57697C;  /* Modern blue-gray button color */
                color: #FFFFFF;  /* White text for buttons */
            }
            QPushButton:hover {
                background-color: #4A5B70;  /* Slightly darker on hover */
            }
            QPushButton:pressed {
                background-color: #3B495E;  /* Darker background on press */
            }
            QVideoWidget {
                border: 2px solid #007ACC;  /* Bright blue border for the video widget */
                border-radius: 5px;
                background-color: #1B2633;  /* Darker video widget background */
            }
        """)

# Main Application
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = IPTVApp()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
