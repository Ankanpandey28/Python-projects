# Voice Recorder

A simple Python project to record audio from your microphone and save it as WAV files.

---

## Features
- Record audio from your default microphone.
- Save recordings using both `scipy.io.wavfile.write` and `wavio.write`.
- Automatically adjusts to your input device’s channel count (mono/stereo).

---

## Requirements
- Python 3.8 or higher
- Python libraries:
  - `sounddevice`
  - `scipy`
  - `wavio`
  - `numpy`

Install dependencies using:

```bash
pip install sounddevice scipy wavio numpy
Or, if you have a requirements.txt file:
pip install -r requirements.txt
#how to Run
Create and activate a virtual environment
macOS/Linux:
python3 -m venv venv
source venv/bin/activate
Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1
#Install dependencies
pip install -r requirements.txt
Run the script
python V_R.py
# Output
--recording0.wav → Saved using scipy.io.wavfile.write
--recording1.wav → Saved using wavio.write
Both files will be saved in the Voice_Recorder project folder.
#Notes
-Ensure your microphone supports the number of channels selected.
-Mono (1 channel) works on most built-in microphones.
-WAV files are uncompressed audio files, suitable for further processing.
#Author
Ankan Pandey
