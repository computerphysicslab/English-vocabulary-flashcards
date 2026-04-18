# 📚 English Vocabulary Flashcards: CEFR Knowledge Scale

An interactive, browser-based flashcard application designed to help learners master English vocabulary through visual association. The app features an adaptive scoring system that maps user accuracy to the **CEFR (A1–C2)** scale in real-time.

## 🚀 Key Features

* **Dynamic Choice Generation:** Every card presents the correct answer plus three unique distractors pulled randomly from the database.
* **Intelligent Progression:** Features a hands-free experience with a **3-second automatic transition** to the next card after an answer is selected.
* **Adaptive CEFR Leveling:** A custom algorithm calculates proficiency level based on cumulative accuracy, ranging from A1 (Beginner) to C2 (Mastery).
* **Randomized Experience:** Uses a **Fisher-Yates shuffle** on page load to ensure the deck order is unique every session.
* **Robust Error Handling:** Includes SVG placeholders for missing images to ensure the UI remains clean even if local assets are disconnected.
* **Responsive UI:** Optimized for all devices using a flexible CSS layout that adapts from a wide view to a 2×2 mobile-friendly grid.

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Structure** | HTML5 | Semantic markup and structure |
| **Styling** | CSS3 | Responsive layout, gradients, and animations |
| **Logic** | Vanilla JavaScript | Game logic, state management, and timers |
| **Assets** | Local Images | Image files stored in the directory with SVG fallbacks |

*Zero dependencies. No frameworks, no libraries, just pure web standards.*

---

## 📊 The Knowledge Scale

The app tracks your performance across all attempts to determine your standing on the Common European Framework of Reference for Languages:

| Accuracy Range | CEFR Level | Description |
| :--- | :--- | :--- |
| 0% – 15% | **A1** | Beginner |
| 16% – 30% | **A2** | Elementary |
| 31% – 45% | **B1** | Intermediate |
| 46% – 60% | **B2** | Upper Intermediate |
| 61% – 84% | **C1** | Advanced |
| 85% – 100% | **C2** | Mastery |

---

## 📂 Installation & Setup

0. You may test the flashcard game just by openning the following URL on your browser: https://computerphysicslab.github.io/English-vocabulary-flashcards/

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/english-flashcards.git
    cd english-flashcards
    ```

2.  **Add Your Images**
    Ensure your vocabulary images (e.g., `apple.png`, `carrot.jpg`) are placed in the root directory or update the paths in the `flashcards` array within `index.html`.

3.  **Launch the App**
    Simply double-click `index.html` to open it in any modern web browser.

---

## ⚙️ Customization

To add your own words, locate the `flashcards` array in the `<script>` tag within `index.html`:

```javascript
let flashcards = [
    { image: "your-image.jpg", word: "Your Word" },
    // Add more objects here
];
```

## 📝 License
This project is open-source and available under the **MIT License**.

---
*Developed to make language learning visual, fast, and fun.*