import os
import tempfile
import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

print("Loading Whisper AI Model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Model Loaded Successfully!")


def clean_command(text):

    text = text.lower().strip()

    remove_words = [
        "please",
        "the",
        "could you",
        "would you",
        "can you",
        "assistant",
        "jarvis"
    ]

    for word in remove_words:
        text = text.replace(word, "")

    text = " ".join(text.split())

    replacements = {
        "start calculator": "open calculator",
        "launch calculator": "open calculator",

        "open note pad": "open notepad",
        "start notepad": "open notepad",

        "open file explorer": "open explorer",

        "start github": "open github",

        "start youtube": "open youtube",

        "start workspace": "initialize workspace"
    }

    return replacements.get(text, text)


def listen():

    SAMPLE_RATE = 16000

    print("Listening...")

    recording = sd.rec(
        int(8 * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    temp = tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    )

    write(temp.name, SAMPLE_RATE, recording)

    try:

        segments, info = model.transcribe(
            temp.name,
            beam_size=5,
            vad_filter=True
        )

        text = ""

        for segment in segments:
            text += segment.text + " "

        text = clean_command(text)

        print("Recognized:", text)

        return text

    finally:

        if os.path.exists(temp.name):
            os.remove(temp.name)