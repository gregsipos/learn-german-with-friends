import json
import time
from deep_translator import GoogleTranslator
import os

INPUT_FILE = "common_words.json"
OUTPUT_FILE = "translated_words.json"

def load_words():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_translations():
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_translations(translations):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)

def translate_word(word):
    try:
        return GoogleTranslator(source="de", target="en").translate(word)
    except Exception as e:
        print(f"⚠️ Error translating '{word}': {e}")
        return "[Translation failed]"

def main():
    word_counts = load_words()
    translations = load_translations()

    for word, count in word_counts:
        if word in translations:
            continue  # already translated

        print(f"\n🔤 German: {word} (used {count} times)")
        user_input = input("Press Enter to translate or type 'q' to quit: ")

        if user_input.strip().lower() == 'q':
            print("👋 Bye!")
            break

        translation = translate_word(word)
        translations[word] = {
            "en": translation,
            "count": count
        }

        print(f"📘 English: {translation}")
        save_translations(translations)
        time.sleep(0.3)  # optional – avoid hitting API too hard

    print("\n✅ All done!")

if __name__ == "__main__":
    main()
