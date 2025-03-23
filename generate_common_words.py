import json
import re
from collections import Counter

TRANSLATION_FILE = "translations.json"
OUTPUT_FILE = "common_words.json"

def load_translations():
    with open(TRANSLATION_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def clean_word(word):
    return re.sub(r"[^\wäöüßÄÖÜ]", "", word.lower())

def extract_all_words(translations):
    all_words = []

    for episode_data in translations.values():
        for line_data in episode_data.values():
            de_text = line_data.get("de", "")
            words = de_text.split()
            cleaned = [clean_word(w) for w in words if clean_word(w)]
            all_words.extend(cleaned)

    return all_words

def main():
    translations = load_translations()
    words = extract_all_words(translations)

    counter = Counter(words)
    most_common = counter.most_common(100)

    # Save to JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(most_common, f, ensure_ascii=False, indent=2)

    print(f"✅ Extracted {len(counter)} unique words.")
    print(f"💾 Top 100 saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()