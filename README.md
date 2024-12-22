# DownloadTube

![DownloadTube Banner](https://img.shields.io/badge/DownloadTube-v1.0-blue) 

<img src="https://raw.githubusercontent.com/v1ck3/DownloadTube/refs/heads/main/DownloadTube.png" width="300" />

**DownloadTube** is a Python-based tool for downloading YouTube videos in **MP4** format, with the ability to choose video quality, show available qualities, and convert the video to MP4 using FFmpeg.

---

## Features 🚀
- **Download YouTube Videos** in the best available quality (video + audio).
- **Convert videos to MP4** format after downloading using FFmpeg.
- **Display available video qualities** before downloading.
- Clean and simple **ASCII art header** to enhance user experience.
  
---

## Table of Contents 📑

- [Installation](#installation-)
  - [Set Up a Virtual Environment](#set-up-a-python-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Install FFmpeg](#install-ffmpeg)
- [Usage](#usage-)
  - [Running the Script](#running-the-script)
  - [Sample Output](#sample-output)
- [Project Structure](#project-structure-)
- [License](#license-)
- [Acknowledgments](#acknowledgments-)

---

## Installation ⚙️

### Set Up a Python Virtual Environment

To ensure that you have an isolated environment for running the script and installing dependencies, it’s highly recommended to use a virtual environment.

#### 1. Create a Virtual Environment
Navigate to your project folder and create a virtual environment:

python3 -m venv venv

This will create a folder called `venv` in your project directory.

#### 2. Activate the Virtual Environment

- **On Linux/macOS:**

  source venv/bin/activate

- **On Windows:**

  .\venv\Scripts\activate

You should see `(venv)` appear in your terminal prompt, indicating the virtual environment is active.

---

### Install Dependencies

With your virtual environment activated, you can install the necessary Python dependencies.

1. First, create a `requirements.txt` file with the following contents:

yt-dlp
pyfiglet

2. Then, run the following command to install the dependencies:

pip install -r requirements.txt

---

### Install FFmpeg

FFmpeg is required for video conversion. To install FFmpeg:

- **On Linux (Debian/Ubuntu):**
  sudo apt update
  sudo apt install ffmpeg

- **On macOS (using Homebrew):**

  brew install ffmpeg

- **On Windows:**
  1. Download FFmpeg from [FFmpeg Official Site](https://ffmpeg.org/download.html).
  2. Extract the files and add the bin folder to your system's PATH.

---

## Usage 🎬

### Running the Script

Once everything is set up, you can run the `DownloadTube` script. Make sure your virtual environment is activated.

1. Run the script:

python DownloadTube.py

2. Follow the prompts:
   - Enter the **YouTube URL** or **Shorts link**.
   - Optionally view **available qualities** before downloading.
   - Choose the **format** (MP4 or MP3).
   - Choose a **download location**.

---

### Sample Output

Enter the YouTube URL or Shorts link: https://www.youtube.com/watch?v=abcd1234
Do you want to see available qualities? (y/n): y
Available qualities for video: Sample Video
18 - 720p - mp4
22 - 1080p - mp4
Do you want to download in MP4 or MP3? (mp4/mp3): mp4
Enter the folder path where you want to save the video (default is current folder):

The video will begin downloading in the chosen format and quality.

---

## Project Structure 📂

DownloadTube/
│
├── DownloadTube.py       # Main Python script for video download
├── requirements.txt          # List of dependencies
├── README.md                 # Project documentation (this file)
└── venv/                     # Virtual environment (created automatically)

### `requirements.txt`

Contains the necessary Python dependencies:

yt-dlp
pyfiglet

---

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments 🙏

- **yt-dlp**: Provides the ability to download YouTube videos and handle different formats.
- **pyfiglet**: Used to generate ASCII art for a clean and stylized banner.
- **FFmpeg**: Converts the downloaded video to the desired format (MP4).

---

## Contributing 🤝

Feel free to fork this repository and contribute by opening an issue or submitting a pull request.  
Make sure to test any changes in your local environment before submitting!

---

### Final Thoughts 💭

Thank you for using **DownloadTube**! This project is designed to be simple, yet effective for downloading YouTube videos and making them available in your preferred format. If you encounter any issues or need new features, feel free to open an issue.

---

### GitHub Badges (Optional)

You can add badges to make your README look more professional. Here are some examples you can include at the top of the README:

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.x-blue)

---
