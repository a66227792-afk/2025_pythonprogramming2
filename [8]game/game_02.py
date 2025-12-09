from tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

score = 0

# 점수 표시 텍스트
score_text = canvas.create_text(
    450, 20,
    text="Score: 0",
    font=("Arial", 14, "bold"),
    fill="black"
)

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.paddle = paddle
        self.canvas.move(self.id, 245, 100)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False
        self.last_hit = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        global score
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        if not self.hit_bottom:
            if self.hit_paddle(pos):
                if not self.last_hit:
                    score += 1
                    canvas.itemconfig(score_text, text=f"Score: {score}")
                self.y = -3
                self.last_hit = True
            else:
                self.last_hit = False

        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)

        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0


paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

def restart():
    global ball, paddle, game_over_text, restart_button, score, score_text
    canvas.delete("all")

    score_text = canvas.create_text(
        450, 20,
        text=f"Score: {score}",
        font=("Arial", 14, "bold"),
        fill="black"
    )

    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')

    if game_over_text:
        canvas.delete(game_over_text)
    if restart_button:
        restart_button.destroy()

    game_over_text = None
    restart_button = None
    tk.update()


game_over_text = None
restart_button = None

def on_close():
    global running
    running = False
    tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_close)
running = True

while running:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    else:
        if game_over_text is None:
            score -= 1
            canvas.itemconfig(score_text, text=f"Score: {score}")

            game_over_text = canvas.create_text(
                250, 200,
                text="GAME OVER",
                font=("Arial", 30, "bold"),
                fill="red"
            )
            restart_button = Button(
                tk, text="Restart", font=("Arial", 14),
                command=restart
            )
            restart_button.place(x=210, y=250)

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
