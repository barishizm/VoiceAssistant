# Riva Voice Assistant

Riva is a simple voice assistant built using Python. It can perform various tasks such as searching Wikipedia, opening websites, playing music, and more. This project leverages `pyttsx3` for text-to-speech, `speech_recognition` for voice recognition, and `wikipedia` for fetching information from Wikipedia.

## Features

- **Voice Interaction:** Interact with Riva using your voice.
- **Wikipedia Search:** Get summaries from Wikipedia.
- **Open Websites:** Open commonly used websites like YouTube, Google, GitHub, StackOverflow, and Spotify.
- **Local Disk Access:** Open local disks on your computer.
- **Custom Responses:** Responds to questions about its identity.

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Step-by-Step Guide

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/barishizm/VoiceAssistant.git
    cd VoiceAssistant
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv .venv
    ```

3. **Activate the Virtual Environment:**

    - On Windows:
    
        ```bash
        .\.venv\Scripts\activate
        ```
    
    - On macOS/Linux:
    
        ```bash
        source .venv/bin/activate
        ```

4. **Install Required Packages:**

    ```bash
    pip install setuptools
    pip install pyttsx3 SpeechRecognition wikipedia pywin32 pyaudio
    ```

### Additional Setup for `PyAudio`

For Windows users, if you encounter issues installing `PyAudio`, you can download the appropriate wheel file from [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it:

```bash
pip install path_to_whl_file/PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
