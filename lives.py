from turtle import Turtle

try:
    with open("records.txt", mode="r") as file:
        lines = file.readlines()
except FileNotFoundError:
    with open("records.txt", mode="w") as data:
        data.write("0")
        score = 0
else:
    score = lines[0]


class Lives(Turtle):
    def __init__(self):
        super(Lives, self).__init__()
        self.penup()
        self.goto(x=-200, y=240)
        self.pendown()
        self.pencolor("white")
        self.hideturtle()
        self.high_score = int(score)
        self.score = 0
        self.trials = "🧡🧡🧡🧡🧡"
        self.write(f"Score: {self.score}\nTrials: {self.trials}\nHigh Score: {self.high_score}",
                   font=("Calibri", 12, 'bold'))

    def clear_write(self):
        self.clear()
        self.write(f"Score: {self.score}\nTrials: {self.trials}\nHighest Score: {self.high_score}",
                   font=("Calibri", 12, 'bold'))

    def check_trials(self):
        self.trials = self.trials.removesuffix(self.trials[-1])
        self.clear_write()

    def check_score(self):
        self.score += 1
        self.clear_write()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over.", font=("Calibri", 16, "italic"))