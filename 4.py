import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random
import time

# Настройки аудио
duration = 5  # секунды записи
sample_rate = 44100

# Словарь с уровнями сложности
words_by_level = {
    "easy": {
        "кот": "cat",
        "собака": "dog",
        "яблоко": "apple",
        "молоко": "milk",
        "солнце": "sun"
    },
    "medium": {
        "банан": "banana",
        "школа": "school",
        "друг": "friend",
        "окно": "window",
        "жёлтый": "yellow"
    },
    "hard": {
        "технология": "technology",
        "университет": "university",
        "информация": "information",
        "произношение": "pronunciation",
        "воображение": "imagination"
    }
}

def translator():
    print("Включаем режим перевода голосовухи...")
    time.sleep(5)
    import sounddevice as sd
    import numpy as np
    import scipy.io.wavfile as wav
    import speech_recognition as sr
    from googletrans import Translator
    import random

    duration = 5  # секунды записи
    sample_rate = 44100

    print("Говори...")
    recording = sd.rec(
    int(duration * sample_rate), # длительность записи в сэмплах
    samplerate=sample_rate,      # частота дискретизации
    channels=1,                  # 1 — это моно
    dtype="int16")               # формат аудиоданных
    sd.wait()  # ждём завершения записи

    wav.write("output.wav", sample_rate, recording)
    print("Запись завершена, теперь распознаём...")

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Ты сказал:", text)
    except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
        print("Не удалось распознать речь.")
        return None
    except sr.RequestError as e:             # - если нет интернета или API недоступен
        print(f"Ошибка сервиса: {e}")
        return None

    while True:
        b = input('Нужен ли перевод? да или нет ')
        if b == "да":    
            a = input("На какой язык перевести? en-Английский, es-Испанский ru-Русский,pt-Португальский,id-Индонезийский,pl-Польский,it-Итальянский,tr-Турецкий ")
            if a == 'en' or a == 'es' or a == 'ru' or a == 'pt' or a == 'id' or a == 'pl' or a == 'it' or a == 'tr':
                translator = Translator()
                translated = translator.translate(text, dest=a)  # здесь 'en' — это английский
            print("🌍 Перевод:", translated.text)
        if b == "нет":
            break
        print("Нет такого")







def select_level():
    """Выбор уровня сложности"""
    print("\nВыберите уровень сложности:")
    print("1 - Легкий🟢")
    print("2 - Средний⭐")
    print("3 - Сложный🔴")
    print("4 - Режим переводчика📄")

    while True:
        choice = input("Ваш выбор (1-4): ")
        if choice in ["1", "2", "3"]:
            return ["easy", "medium", "hard"][int(choice)-1]
        elif choice == "4":
            return translator()
        print("Пожалуйста, введите 1, 2, 3 или 4")

def record_audio():
    """Запись аудио с микрофона"""
    print("\nГоворите сейчас...")
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )
    sd.wait()
    wav.write("output.wav", sample_rate, recording)
    return "output.wav"

def recognize_speech(audio_file):
    """Распознавание речи из аудиофайла"""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"Вы сказали: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Не удалось распознать речь.")
        return None
    except sr.RequestError as e:
        print(f"Ошибка сервиса: {e}")
        return None

def play_game():
    """Основной игровой цикл"""
    print("Нello World!")
    print("/^-----^\ ")
    print("V  o o  V")
    print(" |  Y  |")
    print("  \ Q /")
    print("  / - \ ")
    print("  |    \ ")
    print("  |     \     )")
    print("  || (___\====")
    print("🎤 Игра: Переводчик с русского на английский 🎤")
    print("Произнесите английский перевод показанного русского слова")
    print("Для выхода скажите 'quit'")
    
    level = select_level()
    words = words_by_level[level]
    score = 0
    total_attempts = 0
    
    while True:
        # Выбираем случайное слово
        russian_word, correct_translation = random.choice(list(words.items()))
        print(f"\nСлово: {russian_word}")
        
        # Запись и распознавание речи
        audio_file = record_audio()
        user_translation = recognize_speech(audio_file)
        
        if user_translation == "quit":
            break
            
        total_attempts += 1
        
        # Проверка ответа
        if user_translation == correct_translation:
            print("✅ Правильно!")
            score += 1
            cont = input("Хотите продолжить?пиши да или нет  ")
            if cont == "да":
                continue
            elif cont == "нет":
                break
        elif user_translation:
            print(f"❌ Неправильно. Правильный ответ: {correct_translation}")
            cont = input("Хотите продолжить?пиши да или нет")
            if cont == "да":
                continue
            elif cont == "нет":
                break
        
        # Статистика
        print(f"Ваш счет: {score}/{total_attempts}")
        
        # Пауза перед следующим словом
        time.sleep(1)
    
    print("\nИгра окончена!")
    if total_attempts > 0:
        accuracy = (score / total_attempts) * 100
        print(f"Итоговая точность: {accuracy:.1f}%")
        if accuracy < 60:
            print("Game over! Ваша точность ниже 60!")
        else:
            print("Поздравляем!")    
            print("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───")   
            print("───█▒▒░░░░░░░░░▒▒█───") 
            print("────█░░█░░░░░█░░█────")    
            print("─▄▄──█░░░▀█▀░░░█──▄▄─")   
            print("█░░█─▀▄░░░░░░░▄▀─█░░█")    


if __name__ == "__main__":
    play_game()