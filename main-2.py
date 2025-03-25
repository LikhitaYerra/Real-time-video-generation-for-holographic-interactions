import speech_recognition as sr
import pyttsx3
import os
import re
import mainpy as mp
import datetime
import json

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 0.9)

# Fixed prompt for when there's no input from LLM and emotion
FIXED_PROMPT = "Generate a video of a neutral fish character in an underwater scene with ambient movement"

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="fr-FR")
        print(f"Vous avez dit : {text}")
        return text
    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris.")
        return FIXED_PROMPT
    except sr.RequestError:
        print("Erreur de service de reconnaissance vocale.")
        return FIXED_PROMPT

def generate_response(user_input, context=""):
    result, context = mp.generate_response(user_input, context)
    return result, context

def text_to_speech(text):
    if not isinstance(text, str):
        raise TypeError("Le texte pour la synthèse vocale doit être une chaîne de caractères.")
    engine.stop()
    engine.say(text)
    engine.runAndWait()

def detect_child_emotion():
    """Empty function for detecting emotion from child observation"""
    pass

def generate_video(prompt):
    """Empty function for video generation"""
    pass

def process_prompt(text=None, child_emotion=None):
    """
    Process prompts based on:
    - Text from LLM
    - Emotion detected from child
    - If no input: use fixed prompt
    """
    if text and child_emotion:
        return f"Generate a video of a fish saying: '{text}' with {child_emotion} emotion"
    return FIXED_PROMPT

def save_conversation(input_text, response_text, child_emotion, final_prompt):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"conversation_{timestamp}.txt"
    
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"User: {input_text}\n")
        file.write(f"AI: {response_text}\n")
        file.write(f"Child Emotion: {child_emotion}\n")
        file.write(f"Final Prompt: {final_prompt}\n\n")

def exe():
    context = ""
    print("Bienvenue! La discussion se fera automatiquement. Dites 'au revoir' pour quitter.")
    
    while True:
        # Get child's emotion first
        child_emotion = detect_child_emotion()
        
        # Get speech input
        input_text = speech_to_text()
        
        if input_text == FIXED_PROMPT:
            final_prompt = FIXED_PROMPT
            print(f"Using fixed prompt: {final_prompt}")
            generate_video(final_prompt)
            save_conversation("No input detected", "No response", child_emotion, final_prompt)
            continue

        if "au revoir" in input_text.lower():
            print("Au revoir!")
            text_to_speech("Au revoir")
            save_conversation(input_text, "Au revoir", child_emotion, "Session ended")
            break

        # Generate LLM response
        response, context = generate_response(input_text, context)
        print(f"Réponse du modèle : {response}")
        
        # Generate final prompt with LLM response and child's emotion
        final_prompt = process_prompt(response, child_emotion)
        print(f"\nFinal Prompt: {final_prompt}")
        
        # Generate video
        generate_video(final_prompt)
        
        # Text to speech and save conversation
        text_to_speech(response)
        save_conversation(input_text, response, child_emotion, final_prompt)
        context += f"\nUser: {input_text}\nAI: {response}"

if __name__ == "__main__":
    exe()