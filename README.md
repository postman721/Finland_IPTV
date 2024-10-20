# Finland IPTV v.1.0

**Copyright (c) 2024 JJ Posti <techtimejourney.net>**

This program comes with ABSOLUTELY NO WARRANTY; for details see: [GNU GPL](http://www.gnu.org/copyleft/gpl.html).  
This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991.

## Overview

**Finland IPTV v.1.0** is a lightweight PyQt5-based IPTV player for streaming free Finland IPTV channels. The application downloads an M3U playlist in Markdown format, parses the channel list, and provides a graphical interface for users to select and play channels.

![tv](https://github.com/user-attachments/assets/eec172ec-d0bd-43d9-a889-669c2f691b8a)

This app is specifically designed for simplicity, providing a dropdown list of channels and supporting full-screen playback. Channels are freely available, and the source list is regularly updated from: [Free-TV IPTV GitHub Repository](https://github.com/Free-TV/IPTV).

## Features

- **Auto-fetching Channels:** Automatically downloads and parses the latest Finland IPTV channel list from a remote Markdown file.
- **Graphical Interface:** Channels are displayed in an easy-to-use dropdown menu for quick selection.
- **Media Playback:** Play selected IPTV channels directly within the built-in media player.
- **Full-screen Mode:** Toggle full-screen mode on/off by pressing `F11`.
- **Channel Name Cleanup:** Filters out unwanted characters and symbols from channel names for clarity.
- **Custom Styling:** Modern and clear user interface design with custom styling.

## Requirements

Before running the application, make sure that the following dependencies are installed on your system.

### Python Dependencies

- **Python 3.x**
- **PyQt5** (for graphical interface)
- **PyQt5 Multimedia** (for video playback)
- **requests** (for downloading the IPTV list)

### Installing Dependencies on Debian/Ubuntu

Use the following commands to install the required dependencies:

```bash
sudo apt-get update

sudo apt-get install python3 python3-pip python3-pyqt5 python3-pyqt5.qtmultimedia python3-requests -y
 
sudo apt-get install gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav -y

sudo apt-get install gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-pulseaudio -y

```

### Running on Linux

To run the Finland IPTV player, use the following command:

```bash 

python3 tv.py
```

## For Windows: See the windows_binary folder.


### How to Use

- Select a Channel: Choose a channel from the dropdown menu. Please note that channels do not play automatically upon selection.
  This can be changed by placing 1 to:

  ```bash
  self.channel_combo.setCurrentIndex(0)
  ```

- Playback: The selected channel will begin streaming. If the stream doesn't load, try selecting another channel and then returning to your initial choice.

- Full-screen Mode: Press F11 to toggle full-screen mode on or off.

- Playback Issues: In some cases (like Yle TV1), you may need to select another channel and then return to the original channel to begin playback.


<b> Notice. In the case of Yle TV1: You will first need to select something else and then reselect it for viewing. </b>

In case of an error happening in the program you might see something like this: ![error](https://github.com/user-attachments/assets/78187f6c-4ecc-4774-8501-657d69126785)



