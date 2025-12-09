#Bouncing Ball Game(패배조건 만들기)
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
window_closed = False


def on_close():
    global window_closed
    window_closed = True
    tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_close)

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

        self.hit_bottom = False  #바닥에 닿았는지 여부를 저장하는 변수

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id) 

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]: 
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)      
        print(self.canvas.coords(self.id))

        if pos[1] <= 0:
            self.y = 3 
        if pos[3] >= self.canvas_height:  
            self.hit_bottom = True #바닥에 닿았을 경우 hit_bottom=True

        #이미 바닥에 부딪혔다면 더이상 충돌 체크 안해도 됨
        if not self.hit_bottom:
            if self.hit_paddle(pos) == True:# 패들과 부딪혔는지 검사
                self.y = -3  

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
    global ball, paddle, game_over_text, restart_button

    canvas.delete("all")   # 화면 초기화

    # paddle, ball 다시 생성
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')

    # GAME OVER 텍스트와 버튼 제거
    if game_over_text:
        canvas.delete(game_over_text)
    if restart_button:
        restart_button.destroy()
    game_over_text = None
    restart_button = None
    tk.update()


game_over_text = None
restart_button = None
while True:
    if window_closed:   # 창 닫히면 즉시 종료
        break

    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        if game_over_text is None:  # 한 번만 생성
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


tk.mainloop()
