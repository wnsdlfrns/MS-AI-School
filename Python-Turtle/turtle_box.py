import turtle as Tur
import random as Rand
import matplotlib.colors as Mcolors


class Tools:

    def __init__(self):
        pass

    # hex color - string
    def gen_hex_color(self):
        colors = dict(Mcolors.BASE_COLORS, ** Mcolors.CSS4_COLORS)
        color_names = list(colors.keys())
        color_names.remove('w')
        color_names.remove('k')
        color_name = Rand.choice(color_names)
        return Mcolors.to_hex(colors[color_name])


class TurtleBoxMake(Tools):

    def __init__(self, get_x=0, get_y=0):
        self.x = get_x
        self.y = get_y
        self.window = Tur.Screen()


    def loop(self):
        self.window.mainloop()


    def move_turtle(self, turtle, length, turn=0, rotate=90):
        if turn:
            turtle.left(rotate)
        else:
            turtle.right(rotate)

        turtle.forward(length)


    def make_box(self, x, y):

        each_clone = Tur.Turtle().clone()
        each_clone.teleport(x, y)


        each_clone.shape('turtle')


        length = [Rand.randint(45, 300), Rand.randint(45, 300)]
        hex1, hex2 = self.gen_hex_color(), self.gen_hex_color()
        turn, filled, rotate = Rand.randint(0, 1), Rand.randint(0, 1), Rand.randint(0, 90)

        each_clone.color(hex1, hex2)
        each_clone.pensize(Rand.randint(4, 12))
        each_clone.pencolor(hex1)


        # 거북이 진행 방향
        if turn:
            each_clone.right(rotate)
        else:
            each_clone.left(rotate)


        # 상자 만들기
        if filled:
            each_clone.begin_fill()

        # 굳이 사용하지 않는 변수는 언더바(_) 사용하는게 좋아보임! → 혼돈 방지
        for _ in range(2):
            self.move_turtle(each_clone, length[0], turn)
            self.move_turtle(each_clone, length[1], turn)

        if filled:
            each_clone.end_fill()



# 터틀 불러오기 함수: Tur.Screen().onscreenclick(함수명, 버튼, True) 의 사용 특성으로 인한 함수 정의
def call_turtle(x, y):
    tur_creation = TurtleBoxMake()
    tur_creation.make_box(x, y)



# 터틀 창 크기 설정 + 타이틀 변경
Tur.setup(1000, 1000)
Tur.title('거부기야 거부기야 네가 좋아하는 상자를 알려주렴!')


# 터틀 창 - 클릭 이벤트 관련
sc = Tur.Screen()
sc.onscreenclick(call_turtle, 1, True)
sc.listen()


# 터틀 창 - 꺼짐 방지
tur_creation = TurtleBoxMake()
tur_creation.loop()




