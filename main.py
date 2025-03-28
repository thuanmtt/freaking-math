import tkinter as tk
import random
from time import time


class FreakingMathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Freaking Math")
        self.score = 0

        # Giao diện chính
        self.label_question = tk.Label(root, text="", font=("Arial", 24))
        self.label_question.pack(pady=20)

        self.label_score = tk.Label(
            root, text=f"Score: {self.score}", font=("Arial", 16)
        )
        self.label_score.pack(pady=10)

        self.button_true = tk.Button(
            root,
            text="ĐÚNG",
            command=lambda: self.check_answer(True),
            font=("Arial", 18),
            fg="green",
        )
        self.button_true.pack(side=tk.LEFT, padx=20, pady=20)

        self.button_false = tk.Button(
            root,
            text="SAI",
            command=lambda: self.check_answer(False),
            font=("Arial", 18),
            fg="red",
        )
        self.button_false.pack(side=tk.RIGHT, padx=20, pady=20)

        self.button_restart = tk.Button(
            root,
            text="Chơi lại",
            command=self.restart_game,
            font=("Arial", 18),
            bg="blue",
            fg="white",
        )
        self.button_restart.pack(pady=20)
        self.button_restart.pack_forget()

        # Khởi động trò chơi
        self.next_question()

    def next_question(self):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.correct_answer = self.num1 + self.num2

        # Xác định kết quả hiển thị (có thể đúng hoặc sai)
        correct = random.choice([True, False])
        if correct:
            self.display_answer = self.correct_answer
        else:
            self.display_answer = self.correct_answer + random.randint(-3, 3)

        self.label_question.config(
            text=f"{self.num1} + {self.num2} = {self.display_answer}"
        )

    def check_answer(self, user_answer):
        is_correct = self.display_answer == self.correct_answer

        if user_answer == is_correct:
            self.score += 1
            self.label_score.config(text=f"Score: {self.score}")
            self.next_question()
        else:
            self.game_over()

    def game_over(self):
        self.label_question.config(text="Game Over!")
        self.button_true.config(state=tk.DISABLED)
        self.button_false.config(state=tk.DISABLED)
        self.button_restart.pack(pady=20)

    def restart_game(self):
        self.score = 0
        self.label_score.config(text=f"Score: {self.score}")
        self.button_true.config(state=tk.NORMAL)
        self.button_false.config(state=tk.NORMAL)
        self.button_restart.pack_forget()
        self.next_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = FreakingMathApp(root)
    root.mainloop()
