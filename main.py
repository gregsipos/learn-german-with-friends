
import srt
import os
import json
from deep_translator import GoogleTranslator
import time

CACHE_FILE = "translations.json"

def load_subtitles(filepath):
    """
    Load subtitles from a file and return them as a list of strings.

    Args:
        filepath (str): The path to the subtitle file.

    Returns:
        list: A list of subtitle lines as strings.
    """
    with open(filepath, "r", encoding="cp1252") as f:
        contents = f.read()
    subtitles = list(srt.parse(contents))
    lines = [sub.content.replace("\n", " ").strip() for sub in subtitles]
    return lines

def load_cache():
    """
    Load cached data from a file if it exists.

    This function checks if the cache file exists. If it does, it reads the file
    and loads the cached data as a dictionary. If the file does not exist, it 
    returns an empty dictionary.

    Returns:
        dict: The cached data if the file exists, otherwise an empty dictionary.
    """
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def get_episode_id(filepath):
    # Example: data/friends_s01e01.de.srt → S01E01
    filename = os.path.basename(filepath)
    parts = filename.lower().split("s")
    if len(parts) >= 2 and "e" in parts[1]:
        se = parts[1].split(".")[0].upper()  # E01.DE.SRT → E01
        return f"S{se}"
    return "UNKNOWN"

def translate_text(text, cache, episode_id, index):
    if episode_id not in cache:
        cache[episode_id] = {}

    if str(index) in cache[episode_id]:
        return cache[episode_id][str(index)]["en"]

    try:
        translated = GoogleTranslator(source='de', target='en').translate(text)
        cache[episode_id][str(index)] = {
            "de": text,
            "en": translated
        }
        save_cache(cache)
        return translated
    except Exception as e:
        print(f"❌ Translation error: {e}")
        return "[Translation failed]"

def main():
    """
    Main function to run the "Learn German with Friends (CLI Edition)" application.

    This function loads German subtitles for an episode of "Friends", translates each line to English,
    and displays both the original German text and the English translation in the console. The user
    can navigate through the subtitles line by line.

    Steps:
    1. Prints the application title.
    2. Checks if the subtitle file exists.
    3. Loads the episode ID, cache, and subtitle lines.
    4. Iterates through each subtitle line, displaying the German text and its English translation.
    5. Allows the user to continue to the next line or quit the application.

    Handles:
    - Missing subtitle file.
    - Keyboard interrupt to exit the application gracefully.

    Note:
    - The subtitle file path is hardcoded as "data/friends_s01e01.de.srt".
    - The function assumes the existence of helper functions: `get_episode_id`, `load_cache`, `load_subtitles`, and `translate_text`.

    """
    print("📺 Learn German with Friends (CLI Edition)")
    subtitle_path = "data/friends_s01e01.de.srt"

    if not os.path.exists(subtitle_path):
        print(f"⚠️ Subtitle file not found: {subtitle_path}")
        return

    episode_id = get_episode_id(subtitle_path)
    cache = load_cache()
    lines = load_subtitles(subtitle_path)
    print(f"✅ Loaded {len(lines)} subtitle lines for {episode_id}.\n")

    try:
        for index, line in enumerate(lines):
            if len(line.strip()) < 3:
                continue

            print(f"\n🎬 {episode_id} | Line {index}")
            print(f"🗨️ German: {line}")
            translation = translate_text(line, cache, episode_id, index)
            print(f"📘 English: {translation}")

            user_input = input("Press Enter to continue, or type 'q' to quit: ")
            if user_input.strip().lower() == 'q':
                print("👋 Exiting... Bye!")
                break

            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\n👋 Exiting... (Keyboard Interrupt)")

if __name__ == "__main__":
    main()