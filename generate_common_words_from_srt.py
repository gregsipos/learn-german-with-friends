import os
import srt
import re
import json
from collections import Counter

DATA_FOLDER = "data"
OUTPUT_FILE = "common_words.json"

def load_subtitles_from_folder(folder):
    all_lines = []

    for filename in os.listdir(folder):
        if filename.endswith(".srt") and filename.lower().endswith(".de.srt"):
            filepath = os.path.join(folder, filename)
            try:
                with open(filepath, "r", encoding="cp1252") as f:
                    content = f.read()
                subtitles = list(srt.parse(content))
                lines = [sub.content.replace("\n", " ").strip() for sub in subtitles]
                all_lines.extend(lines)
                print(f"✅ Loaded {len(lines)} lines from {filename}")
            except Exception as e:
                print(f"⚠️ Could not read {filename}: {e}")

    return all_lines

def clean_word(word):
    return re.sub(r"[^\wäöüßÄÖÜ]", "", word.lower())

def extract_words_from_lines(lines):
    all_words = []
    for line in lines:
        words = line.split()
        cleaned = [clean_word(w) for w in words if clean_word(w)]
        all_words.extend(cleaned)
    return all_words

def main():
    lines = load_subtitles_from_folder(DATA_FOLDER)
    all_words = extract_words_from_lines(lines)
    counter = Counter(all_words)
    most_common = counter.most_common(100)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(most_common, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Found {len(counter)} unique words.")
    print(f"📄 Top 100 words saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
