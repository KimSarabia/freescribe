# FreeScribe

FreeScribe is a free, open-source transcription tool that captures live audio and transcribes it in real-time using OpenAI's Whisper model. This app is designed to offer real-time transcription without any fees or subscription costs.

## Features
- Record live audio from your microphone.
- Transcribe audio chunks in real-time.
- View live transcriptions as you speak.
- No internet connection required after installation.

## Getting Started

### Prerequisites

To run FreeScribe locally, you'll need the following installed:

1. **Python 3.x** (Make sure Python is installed and added to your system's PATH)
2. **Git** (optional, for cloning the repository)
3. **Whisper Model** (Installed via Python's `pip`)
4. **PyAudio** (For capturing microphone input)

### Installation

Follow these steps to get FreeScribe up and running:

1. **Clone the Repository** (or download it):
   ```bash
   git clone https://github.com/yourusername/freescribe.git
   cd freescribe
   ```

2. **Create and Activate a Virtual Environment**:
   Create a Python virtual environment to keep dependencies isolated.
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` yet, here’s how to create it:
   ```bash
   pip freeze > requirements.txt
   ```

4. **Install PyAudio**:
   PyAudio is required for microphone input. Install it via `pip`:
   ```bash
   pip install pyaudio
   ```

   If you encounter issues installing PyAudio on macOS, you may need to install `portaudio`:
   ```bash
   brew install portaudio
   ```

5. **Run FreeScribe**:
   Once all dependencies are installed, start FreeScribe by running the Python script:
   ```bash
   python freescribe_ui.py
   ```

### Usage

1. Press the **Record** button to start capturing live audio.
2. Watch the transcription appear in real-time in the text box.
3. Press **Stop** to end the recording and final transcription.

### Configuration

- **Chunk Duration**: Adjust the duration of audio chunks by modifying the `RECORD_SECONDS` variable in `freescribe_ui.py`.
- **Whisper Model**: You can switch to a larger Whisper model for better transcription accuracy by modifying the `model` variable:
  ```python
  model = whisper.load_model("small")
  ```

### Troubleshooting

- **PyAudio Installation Issues**: If you encounter issues installing PyAudio, make sure you have installed `portaudio` or are using the appropriate system libraries.
- **Buffer Overflow Errors**: Increase the `CHUNK` size in `freescribe_ui.py` if you run into buffer overflow issues.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


### TODO

1. **Speaker Differentiation**:
   - TODO: Implement speaker diarization (using `pyannote.audio` or similar).
   - TODO: Automatically add a new line in the transcription when a different voice is detected.

2. **Stop Recording and Transcription**:
   - TODO: Ensure the live transcription also stops at the right place.
   - TODO: Use OpenAI API to create cleaned up transcript.

### Additional Features
3. **Save and Export**:
   - TODO: Allow the user to export the final transcription as a text file.

4. **Error Handling and Notifications**:
   - TODO: Add basic error handling (e.g., alert if the microphone is unavailable).
   - TODO: Notify if transcription fails or if there are issues with speaker detection.

5. TODO: Make the interface downloadable as a zip and run as a standalone app without needing the command line
