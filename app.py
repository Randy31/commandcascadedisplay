import google.generativeai as genai
import speech_recognition as sr


# Assuming you have already set your Google Cloud project and API key
GOOGLE_API_KEY = 'your api key'  # Replace with your actual API key

# Configure the library with your API key
genai.configure(api_key=GOOGLE_API_KEY)

def main():
    print('Content Generator')


    # Capture voice input
    audio_input = capture_voice_input()

    # Generate content only if audio input is captured
    if audio_input:
        print('Generating Content...')
        generated_content = generate_content(audio_input)
        print('loading.....')
        print('\nGenerated Content:')
        print(generated_content)

def generate_content(audio_input):
    model = genai.GenerativeModel(model_name='gemini-pro')

    # Convert voice input to text
    prompt = convert_voice_to_text(audio_input)

    # Generate content using the prompt
    response = model.generate_content(prompt)
    result = response.text
    return result

recognizer = sr.Recognizer()

def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Error: {e}")
        return ""

if __name__ == '__main__':
    main()
