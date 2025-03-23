# 🇩🇪 Learn German with Friends (CLI Project)

A fun and simple command-line tool to help you learn basic German vocabulary using subtitle files from the TV series **Friends**.

---

## 🚀 Features

- 📁 Parses `.srt` subtitle files in German
- 💬 Translates each line using Google Translate (via `deep-translator`)
- 🧠 Extracts common German words from subtitles
- 🌍 Translates most-used words to English
- 📎 Caches everything locally in `.json` so you don't lose progress
- 🎮 Interactive CLI experience (press Enter to translate, or `q` to quit)

---

## 🗂️ Project Structure

```
learn-german-with-friends/
│
├── data/
│   └── friends_s01e01.de.srt        # German subtitle file(s)
│
├── main.py                          # CLI viewer: view + translate subtitle lines
├── generate_common_words_from_srt.py # Extracts & saves top 100 most common words
├── translate_common_words.py        # Interactive translation of top words
│
├── common_words.json                # Output of most frequent German words
├── translated_words.json            # German words with English translations
├── translations.json                # Cached subtitle line translations
│
├── requirements.txt                 # Python dependencies
└── README.md                        # You are here
```

---

## 🧪 Scripts Overview

### `main.py`
> CLI subtitle translator (line-by-line)

- Loads one subtitle `.srt` file
- Shows each German line and its English translation
- Press Enter to go to next line or `q` to quit
- Caches translations in `translations.json`

---

### `generate_common_words_from_srt.py`
> Extracts most-used German words from subtitle files

- Parses all `*.de.srt` files in the `data/` folder
- Cleans and tokenizes the words
- Counts how often each word is used
- Saves top 100 to `common_words.json`

---

### `translate_common_words.py`
> Translates the top 100 German words to English

- Loads words from `common_words.json`
- Press Enter to translate each word (or `q` to quit)
- Translations are stored in `translated_words.json`

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 💡 Subtitle File Format

Make sure your subtitle files are:
- In German (`.de.srt`)
- Named like: `friends_s01e01.de.srt`
- Stored inside the `data/` folder

You can get `.srt` files from [OpenSubtitles.org](https://www.opensubtitles.org/) or similar sites.

---

## 🏑 To Start

```bash
# Step 1: View & translate subtitle lines
python main.py

# Step 2: Extract common words
python generate_common_words_from_srt.py

# Step 3: Translate frequent words interactively
python translate_common_words.py
```

---

## 👨‍💻 Created by Gergely Sipos

Feel free to contribute or fork!

