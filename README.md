# English Vocabulary Flashcards – CEFR Knowledge Scale

An interactive web‑based flashcard app that helps learners build English vocabulary. Each card shows an image; the user must choose the correct English word from **4 options**. The score adapts in real time, and the user’s proficiency is displayed on the **A1 → C2** scale (Common European Framework of Reference for Languages).

After answering, the next card loads **automatically after 3 seconds** – no need to click “Next”. The order of flashcards is **randomised on every page load** (time‑seeded shuffle), ensuring a fresh experience each session.

## Features

- **4‑choice answers** – One correct word + three unique distractors.
- **Automatic card progression** – 3‑second delay after each answer.
- **CEFR level tracking** – Accuracy from 0% → 100% maps to A1, A2, B1, B2, C1, C2.
- **Score system** – Correct answer: +1 point; wrong answer: score unchanged (only total attempts increase).
- **Randomised card order** – Fisher‑Yates shuffle seeded by `Math.random()` (time‑based) on every page reload.
- **Local image support** – Place your `.jpg` / `.png` files in the same directory as the HTML file.
- **Responsive design** – Works on desktop, tablet, and mobile (2×2 button grid on narrow screens).
- **Reset button** – Resets score without changing the current card.

## Tech Stack

| Technology | Purpose |
|------------|---------|
| HTML5 | Structure and semantic markup |
| CSS3 | Responsive layout, gradients, shadows, animations |
| Vanilla JavaScript (ES6) | Game logic, state management, DOM manipulation, timer handling |
| Local file system | Images stored alongside the HTML file (no backend required) |

No external libraries or frameworks – pure static web app.

## Installation & Usage

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/english-flashcards.git
   cd english-flashcards