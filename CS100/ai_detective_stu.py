import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import openai 

# For AI hints (you can plug in your OpenAI key and code here)
openai.api_key = 'your-api-key'  # <--- Replace with your OpenAI API key!

def generate_ai_hint():
    # TODO: Implement AI call here or use a fixed hint for now
    # Hint: Use OpenAI API to generate a hint based on current game state
    prompt = (
       #write the appropriate prompt for this section
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if available
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=60,
    )
    
    return response.choices[0].message.content.strip()



root = tk.Tk()
root.title("AI Escape Room: Detective’s Office")
root.geometry("800x600")

bg_image = Image.open("detective_office_placeholder.jpeg")  # Replace with real image
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0)

computer_unlocked = False
box_unlocked = False

# --- Filing Cabinet (static hint) ---
def open_filing_cabinet():
    messagebox.showinfo("Filing Cabinet", "You find a crumpled note: 'Time is the key...'")

cabinet_btn = tk.Button(root, text="", command=open_filing_cabinet)
cabinet_btn.place(x=, y=, width=, height=)
cabinet_btn.config(bg="gray", activebackground="darkgray", borderwidth=0)

# --- Locked Box Interaction ---
def try_open_box():
    def check_code():
        user_code = code_entry.get()

        # TODO: Fill in the code below to check if user_code is correct code "314"
        # Hint 1: Use if statement to compare user_code to "314"
        # Hint 2: If correct, update box_unlocked and computer_unlocked to True and show success message
        # Hint 3: Else, show warning message for wrong code
        
        # YOUR CODE HERE
        # Example:
        # if ... :
        #     ...
        # else:
        #     ...
        
    box_window = tk.Toplevel(root)
    box_window.title("Locked Box")
    box_window.geometry("300x150")

    tk.Label(box_window, text="Enter the 3-digit code:").pack(pady=10)
    code_entry = tk.Entry(box_window, width=10)
    code_entry.pack()

    submit_btn = tk.Button(box_window, text="Submit", command=check_code)
    submit_btn.pack(pady=10)

box_btn = tk.Button(root, text="", command=try_open_box)
box_btn.place(x=, y=, width=, height=)
box_btn.config(bg="gray", activebackground="darkgray", borderwidth=0)

# --- Computer Interaction ---
def read_computer_message():
    comp_window = tk.Toplevel(root)
    comp_window.title("Detective’s Computer")
    comp_window.geometry("400x250")

    # Clock hint always visible
    clock_label = tk.Label(comp_window, text="🕒 System Time: 3:14", font=("Arial", 12, "bold"))
    clock_label.pack(pady=(10, 5))

    # TODO: Write if/else logic here
    # Hint 1: If box_unlocked is False, show locked message
    # Hint 2: Else, show the detective's log message
    # YOUR CODE HERE
    # Example:
    # if ...:
    #     ...
    # else:
    #     ...

computer_btn = tk.Button(root, text="", command=read_computer_message)
computer_btn.place(x=, y=, width=, height=)
computer_btn.config(bg="gray", activebackground="darkgray", borderwidth=0)

# --- AI Hint Button ---
def show_hint():
    # TODO: Use generate_ai_hint() or call OpenAI API here
    hint = generate_ai_hint()
    messagebox.showinfo("AI Hint", hint)

hint_btn = tk.Button(root, text="Get AI Hint", command=show_hint)
hint_btn.place(x=, y=, width=, height=)

# --- Door Escape Check ---
def try_to_escape():
    # TODO: Complete logic to check if box and computer are unlocked
    # Hint: Use an if statement to check box_unlocked and computer_unlocked
    # If both True, show success message
    # Else, show warning message
    # YOUR CODE HERE
    # Example:
    # if ...:
    #     ...
    # else:
    #     ...

door_btn = tk.Button(root, text="", command=try_to_escape)
door_btn.place(x=700, y=550, width=80, height=100)
door_btn.config(bg="gray", activebackground="darkgray", borderwidth=0)

root.mainloop()