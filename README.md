🚀 **From Text to Intelligence: Build Real-World NLP Systems with Python**

<img width="384" height="688" alt="MuruganVadivel_NLP_realworld_usecase" src="https://github.com/user-attachments/assets/879f1d91-0d4f-4139-a006-1c90f4069bdd" />

If you're serious about **AI, Data Science, or Backend Engineering**, this project is your perfect starting point 👇

---

# 🔥 Natural Language Processing (NLP) with Natural Language Toolkit

I built a **hands-on NLP project** that transforms raw web data into meaningful insights using Python.

👉 Not just theory — this is **real-world, production-style NLP pipeline design**

---

## 💡 Why This Matters

We generate **huge amounts of text data daily**:

* Customer feedback
* Banking documents
* Emails & chats
* Social media

👉 NLP helps convert this **unstructured data → actionable insights**

---

# ⚙️ What This Project Does

🌐 Fetches **live Wikipedia data**
🧹 Cleans & preprocesses raw text
✂️ Tokenizes sentences & words
🚫 Removes stopwords
📊 Analyzes **word frequency patterns**
🏷️ Performs **POS tagging**
🧠 Uses **WordNet for semantic understanding**
📍 Visualizes insights (charts + dispersion plots)

---

# 🧠 Core NLP Concepts Covered

✔️ Tokenization
✔️ Stemming vs Lemmatization
✔️ Stopword Removal
✔️ Frequency Distribution
✔️ Part-of-Speech (POS) Tagging
✔️ Custom Model Training

---

# 💼 Real-World Applications (This is where it gets serious 👇)

### 🤖 Chatbots & AI Assistants

* Understand user queries
* Power intelligent conversations

### 💬 Sentiment Analysis

* Analyze product reviews & social media
* Brand monitoring at scale

### 📧 Spam Detection

* Detect unwanted emails/messages
* Improve security systems

### 🏦 Banking & FinTech (Critical 🔥)

* Automate loan document processing
* Extract data from financial reports
* Detect fraud patterns in text

### 🌍 Machine Translation

* Break language barriers
* Enable global communication

### 📄 Text Summarization

* Convert long reports → concise insights

---

# 🧪 What Makes This Project Stand Out?

✅ End-to-end pipeline (not just scripts)
✅ Clean, modular architecture
✅ Real data (Wikipedia scraping)
✅ Visualization-driven insights
✅ Beginner → Intermediate friendly
✅ Interview-ready concepts

---

# 🧰 Tech Stack

* Python 🐍
* NLTK
* Requests
* BeautifulSoup
* Matplotlib

---

# 📈 Why You Should Care

If you're aiming for:

* AI Engineer 🤖
* Data Scientist 📊
* Backend Engineer ⚙️

👉 This is a **must-have project in your portfolio**

---

# 🎯 Key Takeaway

> NLP is not just about processing text —
> it’s about **understanding human intent at scale**

---

# 🚀 What’s Next?

I’m planning to build:

* 🔥 Chatbot using NLP
* 🔥 Resume Analyzer (ATS-level)
* 🔥 Banking Document AI Parser

---

💬 **Comment “NLP”** if you want the GitHub repo + walkthrough
👍 Like if this helped you
🔁 Share with someone learning AI

---

#️⃣ #NLP #Python #AI #MachineLearning #DataScience #ChatGPT #FinTech #SoftwareEngineering #Developers #LearningJourney

## Key Features

| Feature | Description |
|---|---|
| 🌐 Web Scraping | Fetches live Wikipedia pages using `requests` |
| 🧹 Text Cleaning | Strips HTML and normalises whitespace |
| 🚫 Stopword Removal | Filters common English stopwords via NLTK corpus |
| 📊 Frequency Distribution | Plots the top-N most frequent words using `FreqDist` |
| 📍 Dispersion Plot | Visualises where specific keywords appear across the text |
| ✂️ Sentence Tokenization | Splits text into sentences with `sent_tokenize` |
| 🔤 Word Tokenization | Splits text into words with `word_tokenize` |
| 🧠 WordNet Lookup | Finds synsets, definitions, and usage examples |
| 🏷️ POS Tagging | Tags words with grammatical categories using the Averaged Perceptron Tagger |
| 🎓 Custom POS Training | Trains a `PerceptronTagger` on user-supplied labeled data |
| 🔡 Custom Sentence Tokenizer | Trains a `PunktSentenceTokenizer` on domain-specific text |

---

## NLP Concepts Covered

### Tokenization
Breaking down text into smaller units called **tokens** (words or sentences). This project demonstrates both sentence-level and word-level tokenization.

### Stopword Removal
Filtering out high-frequency but semantically low-value words such as *"the"*, *"is"*, *"in"* so that only meaningful content words remain for analysis.

### Frequency Distribution
Counting the occurrences of each token and plotting the top-N most common words. Useful for understanding the dominant themes in a corpus.

### WordNet & Synsets
**WordNet** is a large lexical database of English. A **synset** (synonym set) is a group of words that share a meaning. This project demonstrates how to query definitions and example sentences for any word.

### Part-of-Speech (POS) Tagging
Assigning a grammatical label — noun, verb, adjective, etc. — to each word based on its context. Uses NLTK's **Averaged Perceptron Tagger** by default, with an example of training a custom tagger.

### Dispersion Plot
Visualises the positions of specific words across the entire text corpus, making it easy to spot thematic clustering.

---

## Project Structure

```
NaturalLanguageProcessingTagAnalysisNLTK/
│
├── main.py                  # Refactored, production-style NLP pipeline
│
├── src/
│   └── nlp.py               # Step-by-step NLP exploration and learning examples
│
├── .env                     # Environment variable configuration
├── .python-version          # Pins Python version (3.11) for uv / pyenv
├── pyproject.toml           # Project metadata and dependencies (uv/PEP 517)
├── uv.lock                  # Locked dependency graph (generated by uv)
└── README.md                # Project documentation
```

---

## Prerequisites & Installation

### Requirements

- **Python 3.11+** (pinned via `.python-version`)
- **[uv](https://github.com/astral-sh/uv)** *(recommended)* — a fast Python package manager — **or** pip

### Option A — Using `uv` (Recommended)

```bash
# 1. Clone the repository
git clone <repository-url>
cd NaturalLanguageProcessingTagAnalysisNLTK

# 2. Create a virtual environment and install dependencies
uv sync

# 3. Activate the virtual environment (Windows)
.venv\Scripts\activate
```

### Option B — Using `pip`

```bash
# 1. Clone the repository
git clone <repository-url>
cd NaturalLanguageProcessingTagAnalysisNLTK

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install nltk requests bs4 html5lib matplotlib
```

### Dependencies

| Package | Purpose |
|---|---|
| `nltk` | Core NLP library — tokenization, POS tagging, corpora, WordNet |
| `requests` | HTTP client for fetching Wikipedia pages |
| `bs4` (BeautifulSoup4) | HTML parsing in `src/nlp.py` |
| `html5lib` | HTML5-compliant parser backend for BeautifulSoup |
| `matplotlib` | Plotting frequency distributions and dispersion plots |

> All dependencies are declared in [`pyproject.toml`](pyproject.toml) and pinned in [`uv.lock`](uv.lock).

---

## Environment Configuration

The `.env` file contains two project-level environment variables:

```env
# Adds src/ to the Python module search path
PYTHONPATH=src

# Directs NLTK to store/look for downloaded data in a local folder
NLTK_DATA=./nltk_data
```

> **Note:** NLTK data is downloaded automatically at runtime by both `main.py` and `src/nlp.py`. You do **not** need to run a separate download script.

---

## Usage

### Run the main pipeline

```bash
python main.py
```

This will:
1. Fetch and clean the **Tata Group** Wikipedia article
2. Print the filtered token count and a sample of 50 tokens
3. Display and plot the **top 20 most frequent words** (frequency distribution chart)
4. Print a tabulated count for the top 10 words
5. Display a **dispersion plot** for the keywords `tata`, `parser`, and `india`

### Run the exploration/learning script

```bash
python src/nlp.py
```

This script walks through all NLP concepts step-by-step:
1. Scrapes the `TATA` Wikipedia page using BeautifulSoup
2. Removes stopwords and prints frequency distribution
3. Plots the top-20 words
4. Demonstrates sentence tokenization
5. Trains a custom `PunktSentenceTokenizer`
6. Demonstrates word tokenization
7. Performs WordNet synset lookup for `"dog"`
8. Performs POS tagging on a sample sentence
9. Trains a custom `PerceptronTagger` and tests it

---

## Code Walkthrough

### `main.py` — Refactored Pipeline

`main.py` provides a clean, modular implementation using well-defined functions.

#### `HTMLTextExtractor` (class)
A lightweight custom HTML parser built on Python's stdlib `html.parser.HTMLParser`. It collects all text nodes from an HTML document without requiring BeautifulSoup.

```python
class HTMLTextExtractor(HTMLParser):
    def handle_data(self, data):
        self.text_parts.append(data)        # collect every text node

    def get_text(self):
        return " ".join(self.text_parts)    # join into a single string
```

#### `extract_text_from_html(html: str) -> str`
Feeds raw HTML into `HTMLTextExtractor` and collapses all whitespace into single spaces, returning clean plain text.

#### `fetch_and_clean_wiki_text(url: str) -> list[str]`
End-to-end pipeline that:
1. Fetches a Wikipedia URL with a desktop `User-Agent` header
2. Extracts plain text via `extract_text_from_html`
3. Downloads `stopwords` corpus silently (`quiet=True`)
4. Tokenizes with a regex (`[A-Za-z]+`) to extract only alphabetic tokens
5. Lowercases all tokens
6. Removes English stopwords
7. Returns the cleaned `list[str]` of meaningful words

#### `main()`
Orchestrates the pipeline and produces visualisations:

```python
wiki_url = "https://en.wikipedia.org/wiki/Tata_Group"
filtered_tokens = fetch_and_clean_wiki_text(wiki_url)

# Frequency distribution — bar chart of top 20 words
clean_token = FreqDist(filtered_tokens)
clean_token.plot(20, cumulative=False)
plt.show()

# Tabulate top 10
clean_token.tabulate(10)

# Dispersion plot — positional occurrence of keywords
text = Text(clean_token)
text.dispersion_plot(["tata", "parser", "india"])
plt.show()
```

---

### `src/nlp.py` — Exploration & Learning Examples

This script is structured as a sequence of labelled sections, each demonstrating one NLP concept.

#### Section 0 — Web Scraping & Frequency Distribution
Fetches the `TATA` Wikipedia page using **BeautifulSoup + html5lib**, removes stopwords, and plots the top-20 word frequencies.

```python
frequence = nltk.FreqDist(clean_token)
frequence.plot(20)
```

#### Section 1 — Basic Sentence Tokenization
Uses NLTK's pre-trained **Punkt** sentence tokenizer to split multi-sentence text, correctly handling abbreviations like *Dr.*, *Jan.*, and *U.S.*

```python
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize("NLTK is a great NLP toolkit. Dr. Smith, who joined in Jan. 2023 ...")
# Output: ['NLTK is a great NLP toolkit.', "Dr. Smith, who joined in Jan. 2023, ..."]
```

#### Section 2 — Custom Sentence Tokenizer
Trains a `PunktSentenceTokenizer` on a custom corpus so it can learn domain-specific abbreviations (e.g., `spec.`, `approx.`).

```python
custom_tokenizer = PunktSentenceTokenizer(train_text)
tokenized_sentences = custom_tokenizer.tokenize(new_text)
```

#### Section 3 — Word Tokenization
Uses `word_tokenize` to split a sentence into individual words and punctuation tokens, correctly handling contractions and possessives.

```python
words = word_tokenize("The CEO's announcement surprised investors on Wall St.")
# Output: ['The', 'CEO', "'s", 'announcement', 'surprised', 'investors', 'on', 'Wall', 'St', '.']
```

#### Section 4 — WordNet Synset Lookup
Queries **WordNet** for synonym sets, definitions, and example sentences.

```python
syns = wn.synsets("dog")
print(syns[0].name())       # dog.n.01
print(syns[0].definition()) # a domestic animal...
print(syns[0].examples())   # ['the dog barked all night']
```

#### Section 5 — POS Tagging with Averaged Perceptron Tagger
Tags each token in a sentence with its grammatical category using the pre-trained Averaged Perceptron model.

```python
text = "The quick brown fox jumps over the lazy dog."
tokens = word_tokenize(text)
tagged_text = nltk.pos_tag(tokens)
# [('The', 'DT'), ('quick', 'JJ'), ('brown', 'NN'), ('fox', 'NN'), ...]
```

#### Section 6 — Custom POS Tagger Training
Initialises a `PerceptronTagger` without loading the default model, trains it on custom `(word, tag)` pairs, then tags new text.

```python
custom_tagger = PerceptronTagger(load=False)
custom_tagger.train([
    [('Today', 'NN'), ('is', 'VBZ'), ('good', 'JJ')],
    ...
])
print(custom_tagger.tag(['Today', 'is', 'sunny']))
```

---

## Sample Output

```
Fetched: https://en.wikipedia.org/wiki/Tata_Group
Filtered token count: 3842
Sample filtered tokens: ['tata', 'group', 'indian', 'multinational', 'conglomerate', ...]

# Frequency table (top 10):
tata    group   india   companies  ...
 312      189     143      97      ...
```

Matplotlib windows will open displaying:
- **Bar chart** — top 20 most frequent words
- **Dispersion plot** — positions of `tata`, `parser`, `india` across the corpus

---

## NLTK Resources Downloaded

The following NLTK corpora/models are downloaded automatically at runtime:

| Resource | Used For |
|---|---|
| `stopwords` | Filtering common English words |
| `punkt_tab` | Pre-trained Punkt sentence tokenizer |
| `punkt` | Punkt tokenizer models (word/sentence) |
| `wordnet` | Lexical database for synset lookups |
| `averaged_perceptron_tagger` | Default POS tagging model |

NLTK data is stored in the path specified by `NLTK_DATA` in `.env` (`./nltk_data` by default).

---

## Common POS Tags Reference

| Tag | Meaning | Example |
|---|---|---|
| `DT` | Determiner | the, a |
| `JJ` | Adjective | quick, brown |
| `NN` | Noun (singular/mass) | fox, dog |
| `NNS` | Noun (plural) | foxes, dogs |
| `NNP` | Proper noun (singular) | Tata, India |
| `VB` | Verb (base form) | run, jump |
| `VBZ` | Verb (3rd person singular) | runs, jumps |
| `RB` | Adverb | quickly, very |
| `PRP` | Personal pronoun | he, she, it |
| `IN` | Preposition/conjunction | in, on, over |
| `CC` | Coordinating conjunction | and, but, or |

---

## Real-World Applications

| Domain | Use Case |
|---|---|
| 🤖 Chatbots & Virtual Assistants | Intent detection, entity extraction from user queries |
| 💬 Sentiment Analysis | Analysing product reviews, social media posts |
| 📧 Spam Detection | Classifying emails by content patterns |
| 🏦 Banking & Finance | Parsing loan applications, extracting data from financial reports |
| 🌍 Machine Translation | Translating text while preserving meaning |
| 📄 Text Summarisation | Condensing long documents into key points |
| 🔍 Search Engines | Query understanding, document ranking |
| 🏥 Healthcare NLP | Extracting clinical entities from medical notes |

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please follow PEP 8 style guidelines and include docstrings for any new functions.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or support, please open an issue on GitHub or contact the maintainers.


## 📊 Analysis Examples

### Tokenization
```
Original text: Natural language processing (NLP) is a field of artificial intelligence...
Tokens: ['Natural', 'language', 'processing', '(', 'NLP', ')', 'is', 'a', 'field', ...]
```

### Word Frequency
```
Top 10 most common words:
1. language: 5 times
2. processing: 4 times
3. natural: 3 times
...
```

### POS Tagging
```
Word: 'language' | Tag: 'NN' (Noun)
Word: 'processing' | Tag: 'NN' (Noun)
Word: 'is' | Tag: 'VBZ' (Verb, 3rd person singular)
```
