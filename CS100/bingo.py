import tkinter as tk
import openai
import random

# 🔑 Set your OpenAI API key

# Global state
question_pool = []
bingo_card = []
buttons = []
current_question = None
asked_answers = set()

# 🧠 Generate a single vocabulary question using OpenAI
def generate_vocabulary_question():
    prompt = (
        "Generate a simple English vocabulary quiz item. Format:\n"
        "Question: What is a synonym for 'happy'?\n"
        "Answer: joyful"
    )
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content.strip()
        if "Question:" in content and "Answer:" in content:
            question = content.split("Question:")[1].split("Answer:")[0].strip()
            answer = content.split("Answer:")[1].strip()
            return {"question": question, "answer": answer}
    except Exception as e:
        print(f"OpenAI Error: {e}")
    return None

# 📦 Generate a list of unique vocabulary Q&A pairs
def generate_question_set(n=25):
    questions = []
    seen_answers = set()
    #3. Generate Unique Vocabulary Questions



# 🎮 Start game and draw the Bingo grid
def start_game():
    global question_pool, bingo_card, buttons, asked_answers
    asked_answers = set()
    question_pool = generate_question_set(30)
    bingo_card = random.sample(question_pool, 25)

    #4:Remove all previous buttons from the grid frame


    #1. Create the 5×5 Grid of Buttons (Nested Loop)

    

    ask_next_question()

# ❓ Show the next question
def ask_next_question():
    global current_question
    

    #2. Filter Out Used Questions
    
    if not remaining:
        question_label.config(text="All questions asked.")
        return

    current_question = random.choice(remaining)
    asked_answers.add(current_question['answer'].lower())
    question_label.config(text=f"Question: {current_question['question']}")

# ✅ Mark answer as correct (green) or incorrect (red)
def mark_word(i, j):
    selected_word = buttons[i][j].cget("text")
    if current_question and selected_word.lower() == current_question["answer"].lower():
        buttons[i][j].config(bg="lightgreen", relief=tk.SUNKEN, state="disabled", font=("Helvetica", 10, "bold"))
    else:
        buttons[i][j].config(bg="lightcoral", relief=tk.SUNKEN, state="disabled", font=("Helvetica", 10, "bold"))

# 🖼️ Setup GUI
root = tk.Tk()
root.title("AI Vocabulary Bingo")
root.geometry("800x600")

question_label = tk.Label(root, text="Press 'Start Game' to begin!", font=("Helvetica", 16))
question_label.pack(pady=10)

start_button = tk.Button(root, text="Start Game", font=("Helvetica", 14), command=start_game)
start_button.pack(pady=10)

next_button = tk.Button(root, text="Next Question", font=("Helvetica", 12), command=ask_next_question)
next_button.pack(pady=5)

grid_frame = tk.Frame(root)
grid_frame.pack(pady=20)

root.mainloop()