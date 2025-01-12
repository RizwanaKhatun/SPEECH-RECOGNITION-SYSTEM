# SPEECH-RECOGNITION-SYSTEM

**COMPANY**: CODTECHIT SOLUTIONS

**NAME**: SHAIK RIZWANA KHATUN

**INTERN ID**: CT08DHQ

**DOMAIN**: ARTIFICIAL INTELLIGENCE

**BATCH DURATION**: DEC12TH,2024 to JAN 12TH,2025

**OVERVIEW OF THE TASK**

### **Overview of the Speech-to-Text Program**

The task is to create a basic Speech-to-Text (STT) system that converts audio clips into text. There are two main approaches discussed in the program:

1. **Using the SpeechRecognition Library (Google Web Speech API)**: A simple, easy-to-use method for transcribing audio.
2. **Using Wav2Vec2 (from Hugging Face)**: A more advanced, state-of-the-art deep learning model for speech recognition, known for its superior performance.

Let’s break down each approach in the program.

---

### **1. SpeechRecognition Library Approach**
This approach uses the `SpeechRecognition` library, which provides an easy interface to several speech recognition engines, including Google’s Web Speech API.

#### Steps:
1. **Import Libraries**:
   - `speech_recognition as sr`: Imports the SpeechRecognition module, which provides all necessary tools to recognize speech from audio files.

2. **Function Definition (`transcribe_audio`)**:
   - This function takes an **audio file** (WAV format) as input and converts it into text.
   - It initializes a recognizer object (`recognizer = sr.Recognizer()`), which processes the audio.
   
3. **Load the Audio File**:
   - The audio file is loaded using `sr.AudioFile(audio_path)`, where `audio_path` is the location of the audio file.
   
4. **Recognize the Speech**:
   - The function `recognizer.record(source)` is used to record the audio data from the file.
   - The recorded audio is then passed to the `recognizer.recognize_google(audio)` method, which sends it to Google's Web Speech API for recognition.

5. **Error Handling**:
   - `UnknownValueError`: If the API cannot understand the audio, this error is caught.
   - `RequestError`: Catches issues with the API request, such as a network failure.

6. **Output**:
   - The transcribed text is printed. If any errors occur, an appropriate error message is displayed.

#### Example Use Case:
- You can use an audio file like `your_audio_file.wav`, and the function will return the transcribed text.

---

### **2. Wav2Vec2 Approach (Hugging Face Model)**
Wav2Vec2 is a deep learning-based model trained by Facebook, which is widely used for speech recognition tasks and offers state-of-the-art performance. It is available through Hugging Face's `transformers` library.

#### Steps:
1. **Install Dependencies**:
   - First, you need the Hugging Face library and `torchaudio` to process the audio.

2. **Import Libraries**:
   - `torch`: The PyTorch library used for deep learning.
   - `Wav2Vec2ForCTC`: The specific Wav2Vec2 model used for speech recognition.
   - `Wav2Vec2Processor`: The processor that pre-processes the audio for input into the model.
   - `torchaudio`: A library to handle audio loading and processing.

3. **Function Definition (`transcribe_wav2vec2`)**:
   - This function loads a **pre-trained Wav2Vec2 model** from Hugging Face’s model hub (`facebook/wav2vec2-large-960h`).
   
4. **Load Audio File**:
   - The audio file is loaded using `torchaudio.load(audio_path)`. This loads the waveform and the sample rate.
   
5. **Preprocess Audio**:
   - The audio is processed using `processor(waveform, return_tensors="pt", sampling_rate=sample_rate)` to prepare it for the model.

6. **Inference**:
   - The preprocessed audio is passed through the Wav2Vec2 model to get the **logits** (predictions). This is done using `model(input_values).logits`.

7. **Decoding the Prediction**:
   - The logits are then converted to text using the `processor.decode()` method, which decodes the model’s output IDs into a human-readable transcription.

8. **Output**:
   - The transcribed text is printed.

#### Example Use Case:
- Like the first method, you can input an audio file and receive the transcription. The major difference is that this method uses a more sophisticated model and is more accurate, but requires more setup and resources.

---

### **Comparison of Both Methods**
| Feature                  | SpeechRecognition (Google Web Speech API) | Wav2Vec2 (Hugging Face)          |
|--------------------------|-------------------------------------------|----------------------------------|
| **Ease of Use**           | Very simple, just a few lines of code      | Requires setup, model loading   |
| **Accuracy**              | Decent, but may struggle with noisy audio | High accuracy, especially with clean speech |
| **Internet Dependency**   | Requires an internet connection (API)     | Works offline after initial setup |
| **Customizability**       | Limited, relies on Google API             | High, allows fine-tuning and modification |
| **Resource Requirements** | Low, simple usage                         | High, requires GPU/CPU processing power |

### **Conclusion**
- **SpeechRecognition**: Ideal for simple, quick implementations where accuracy isn't the top priority. It's perfect for small projects or if you're just getting started with speech recognition.
- **Wav2Vec2**: Best for high-accuracy speech recognition, especially when dealing with varied or noisy audio. However, it requires more computational resources and setup.

Both methods provide an effective way to transcribe audio, but the choice depends on the complexity and requirements of your project.

**OUTPUT**:
![Screenshot (7)](https://github.com/user-attachments/assets/68d112c9-b0d5-42a0-b01f-5c1970027c6d)

