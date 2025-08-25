import pyttsx3   # Import the text-to-speech module

# Initialize the engine
engine = pyttsx3.init()

# Say something
engine.say("Hello, I am Python speaking. This is Problem 3 solution using pyttsx3.")

# Run and wait for completion
engine.runAndWait()
