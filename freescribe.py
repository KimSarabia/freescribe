import tkinter as tk
import time
import threading
import pyaudio
import whisper
import numpy as np

# Create the main application window
window = tk.Tk()
window.title("FreeScribe")
window.geometry("400x300")

# Whisper model
model = whisper.load_model("base")

# Global variables for recording status and time
recording = False
start_time = None

# PyAudio configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()


# Update the timestamp during recording
def update_timestamp():
    while recording:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        timestamp_label.config(text=f"Recording... {minutes:02}:{seconds:02}")
        time.sleep(1)


# Capture live audio and transcribe in real-time
def transcribe_audio():
    global recording
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    while recording:
        audio_data = np.frombuffer(stream.read(CHUNK), dtype=np.int16).flatten()
        audio_data = audio_data.astype(np.float32) / 32768.0  # Normalize the audio data
        result = model.transcribe(audio_data, fp16=False)  # Transcribe audio data
        transcription_text.insert(tk.END, result["text"] + "\n")  # Append transcription
        transcription_text.see(tk.END)  # Auto-scroll to the latest transcription

    stream.stop_stream()
    stream.close()


# Start recording when the "Record" button is pressed
def start_recording():
    global recording, start_time
    if not recording:
        recording = True
        start_time = time.time()
        threading.Thread(
            target=update_timestamp
        ).start()  # Run timestamp in a separate thread
        threading.Thread(
            target=transcribe_audio
        ).start()  # Run transcription in a separate thread
        transcription_text.insert(
            tk.END, "Recording started...\n"
        )  # Placeholder for transcription
        record_button.config(
            state=tk.DISABLED
        )  # Disable the record button while recording


# Stop recording when the "Stop" button is pressed
def stop_recording():
    global recording
    if recording:
        recording = False
        transcription_text.insert(tk.END, "Recording stopped.\n")
        timestamp_label.config(text="Recording stopped.")
        record_button.config(state=tk.NORMAL)  # Re-enable the record button


# Add a label to show the app name or instructions
title_label = tk.Label(window, text="FreeScribe", font=("Helvetica", 16))
title_label.pack(pady=10)

# Add a label for the recording timestamp
timestamp_label = tk.Label(
    window, text="Press 'Record' to start", font=("Helvetica", 12)
)
timestamp_label.pack(pady=10)

# Add a record button with functionality
record_button = tk.Button(
    window,
    text="Record",
    font=("Helvetica", 14),
    bg="green",
    fg="white",
    command=start_recording,
)
record_button.pack(pady=20)

# Add a stop button with functionality
stop_button = tk.Button(
    window,
    text="Stop",
    font=("Helvetica", 14),
    bg="red",
    fg="white",
    command=stop_recording,
)
stop_button.pack(pady=10)

# Add a text area for showing transcription
transcription_text = tk.Text(window, height=10, width=40)
transcription_text.pack(pady=10)

# Start the main event loop
window.mainloop()
