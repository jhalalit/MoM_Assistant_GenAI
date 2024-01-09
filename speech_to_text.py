import tkinter as tk
import speech_recognition as sr

class SpeechToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech to Text")

        self.text_label = tk.Label(root, text="Spoken Text:")
        self.text_label.pack()

        self.text_display = tk.Label(root, text="")
        self.text_display.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_listening)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_listening, state=tk.DISABLED)
        self.stop_button.pack()

        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Variable to store recognized text
        self.recognized_text = ""

    def start_listening(self):
        # Enable the stop button and disable the start button
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Start listening in a separate thread
        self.listen_thread = threading.Thread(target=self.continuous_listen)
        self.listen_thread.start()

    def continuous_listen(self):
        try:
            with self.microphone as source:
                print("Listening...")
                audio_data = self.recognizer.listen(source, timeout=None, phrase_time_limit=None)
                print("Recognizing...")
                self.recognized_text = self.recognizer.recognize_google(audio_data)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    def stop_listening(self):
        # Disable the stop button and enable the start button
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

        # Update the displayed text in the GUI
        self.text_display.config(text=self.recognized_text)

if __name__ == "__main__":
    import threading

    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()