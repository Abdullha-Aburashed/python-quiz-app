questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0  
    },
    {
        "topic": "Lists",
        "question": "Which method adds an element to the end of a list?",
        "code": "my_list = [1, 2, 3]",
        "options": ["append()", "insert()", "extend()", "add()"],
        "answer": 0
    },
    {
        "topic": "Strings",
        "question": "What will be the output of 'hello'.upper()?",
        "code": "print('hello'.upper())",
        "options": ["HELLO", "hello", "Hello", "hELLO"],
        "answer": 0
    }
] 

import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Generator")
        self.root.geometry("500x400")

        # Input Field for Topic
        self.topic_label = tk.Label(root, text="Enter Python Topic:")
        self.topic_label.pack(pady=10)
        self.topic_entry = tk.Entry(root, width=40)
        self.topic_entry.pack(pady=5)

        # Generate Question Button
        self.generate_button = tk.Button(root, text="Generate Python Question", command=self.generate_question)
        self.generate_button.pack(pady=10)

        # Display Section
        self.question_label = tk.Label(root, text="", wraplength=450)
        self.question_label.pack(pady=10)
        self.code_label = tk.Label(root, text="", font=("Courier", 10))
        self.code_label.pack(pady=5)

        # Radio Buttons for Options
        self.option_var = tk.IntVar()
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(root, text="", variable=self.option_var, value=i)
            button.pack(anchor="w", padx=20)
            self.option_buttons.append(button)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        # Feedback Area
        self.feedback_label = tk.Label(root, text="", fg="blue")
        self.feedback_label.pack(pady=10)

        # Store the current question
        self.current_question = None

    def generate_question(self):
        topic = self.topic_entry.get().strip()
        if not topic:
            messagebox.showwarning("Input Error", "Please enter a topic.")
            return

        # Filter questions by topic
        filtered_questions = [q for q in questions if q["topic"].lower() == topic.lower()]
        if not filtered_questions:
            messagebox.showinfo("No Questions", f"No questions found for topic: {topic}")
            return

        # Select the first matching question
        self.current_question = filtered_questions[0]

        # Update the GUI
        self.question_label.config(text=self.current_question["question"])
        self.code_label.config(text=self.current_question["code"])

        # Update the options
        for i, option in enumerate(self.current_question["options"]):
            self.option_buttons[i].config(text=option)

    def check_answer(self):
        if self.current_question is None:
            messagebox.showwarning("No Question", "Please generate a question first.")
            return

        selected_option = self.option_var.get()
        if selected_option == self.current_question["answer"]:
            self.feedback_label.config(text="Correct! Well done!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. Try again.", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()