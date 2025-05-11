import speech_recognition as sr
import pyttsx3
import ollama

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        return {"success": False, "error": "Recognizer not an instance of sr.Recognizer"}
    if not isinstance(microphone, sr.Microphone):
        return {"success": False, "error": "Microphone not an instance of sr.Microphone"}

    with microphone as source:
        print("Adjusting for ambient noise, please wait...")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
        except Exception as e:
            return {"success": False, "error": f"Could not adjust for ambient noise: {e}"}
        
        print("\nListening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)
        except sr.WaitTimeoutError:
            return {"success": False, "error": "No speech detected within the timeout period."}
        except Exception as e:
            return {"success": False, "error": f"Error capturing audio: {e}"}

    print("Transcribing speech...")
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable. Check your internet connection."
    except sr.UnknownValueError:
        # Speech was unintelligible
        response["success"] = False
        response["error"] = "Unable to recognize speech."
    except Exception as e:
        response["success"] = False
        response["error"] = f"An unexpected error occurred during transcription: {e}"
        
    return response


def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        engine.setProperty
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def ask_jarvis(user_message, history):
    try:
        history.append({"role": "user", "content": user_message})
        response = ollama.chat(model='gemma3:4b', messages=history)
        answer = response.message.content
        history.append({"role": "assistant", "content": answer})
        return answer
    except Exception as e:
        return f"An error occurred: {str(e)}"



conversation_history = [
    {"role": "system", "content": "You are Jarvis, a polite and efficient AI assistant. Respond in a short, crisp, and respectful manner. Avoid unnecessary details and focus only on what is essential to answer the user's question or request."}
]



recognizer = sr.Recognizer()
try:
    microphone = sr.Microphone()
except Exception as e:
    print(f"Error initializing microphone: {e}")
    print("Please ensure you have a microphone connected and configured.")
    print("If you have multiple microphones, you might need to specify the device_index in sr.Microphone(device_index=X).")
    exit(1)

text_to_speech("Hello there! My name is Jarvis. I am here to answer all your queries. Please ask me anything.")

try:
    while True:
        text_to_speech("hmmmm")

        speech_result = recognize_speech_from_mic(recognizer, microphone)

        if speech_result["transcription"]:
            user_input = speech_result["transcription"]
            reply = ask_jarvis(user_input, conversation_history)
            text_to_speech(reply)
        elif speech_result["error"]:
            print(f"Error: {speech_result['error']}")
        
except KeyboardInterrupt:
    print("\nApplication interrupted. Exiting...")
finally:
    print("\nThank you for using the app!")