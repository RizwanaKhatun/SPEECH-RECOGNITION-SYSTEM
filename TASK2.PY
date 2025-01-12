import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torchaudio

def transcribe_wav2vec2(audio_path):
    # Load pre-trained Wav2Vec2 model and processor
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h")
    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")

    # Load the audio file
    waveform, sample_rate = torchaudio.load(audio_path)

    # Resample audio to the sample rate required by the model
    waveform = waveform.squeeze()  # Remove extra dimension if stereo
    input_values = processor(waveform, return_tensors="pt", sampling_rate=sample_rate).input_values

    # Perform inference
    with torch.no_grad():
        logits = model(input_values).logits

    # Decode the output logits to text
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])

    print("Transcription: ", transcription)

# Path to your audio file
audio_path = "your_audio_file.wav"
transcribe_wav2vec2(audio_path)
