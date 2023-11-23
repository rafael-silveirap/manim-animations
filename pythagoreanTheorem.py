from manim import *
import math

class Video(Scene):
  def construct(self):
    #criando o título
    title = Text('Proof').scale(1.3)
    of = Text('of').scale(1.3)
    subject = Text('Pythagorean theorem',t2c={'[:1]': WHITE, '[1:3]': PINK,'[3:4]': WHITE, '[4:5]': BLUE,'[5:7]': WHITE, '[7:8]': PINK, '[8:9]': WHITE, '[9:11]': BLUE}).scale(1.3)
    subject.set_y(-1.5)
    title.set_y(1.5)
    #mostrando o título
    self.play(FadeIn(title))
    self.play(FadeIn(of))
    self.play(Write(subject))

    group1 = Group(title, of, subject)

    self.wait()
    self.play(FadeOut(group1))

    #mostrando o triangulo
    START_A = (-1.5,-2.5,0)
    END_A = (0.5,-2.5,0)
    ladoA = Line(START_A,END_A, color = BLUE);
    END_B = (-1.5,0,0)
    ladoB = Line(START_A, END_B)
    ladoC = Line(END_B, END_A, color = PINK)
    self.play(FadeIn(ladoA))
    self.play(FadeIn(ladoB))
    self.play(FadeIn(ladoC))

    angulo_reto = RightAngle(ladoA, ladoB, color = PINK)
    self.play(FadeIn(angulo_reto))
    triangulo = Group(ladoA, ladoB, ladoC, angulo_reto)
    triangulo_Vt = VGroup(ladoA, ladoB, ladoC)

    #OUTRO TRIANGULO
    FIM_NOVO_A = (-1.5, 2, 0)
    FIM_NOVO_B = (1, 2, 0)
    NOVO_A = Line(END_B, FIM_NOVO_A, color = BLUE)
    NOVO_B = Line(FIM_NOVO_A, FIM_NOVO_B)
    NOVO_C = Line(END_B, FIM_NOVO_B, color = PINK)
    NOVO_TRIANGULO = VGroup(NOVO_A, NOVO_B, NOVO_C)

    self.play(FadeIn(NOVO_A))
    self.play(FadeIn(NOVO_B))
    self.play(FadeIn(NOVO_C))

    alfa = Angle(ladoC, ladoA, radius = 0.6, quadrant=(-1,-1), color = RED)
    beta = Angle(ladoB, ladoC, radius = 0.6, quadrant=(-1,1), color = YELLOW)

    self.play(FadeIn(alfa, beta))
    self.wait()
    self.play(FadeOut(alfa))

    alfa = Angle(NOVO_C, NOVO_A, radius = 0.6, quadrant=(1,1), color = RED)

    self.play(FadeIn(alfa))

    RETO = RightAngle(NOVO_C, ladoC, color = PINK)

    self.play(FadeIn(RETO))
    self.wait()

    juntar = Line(END_A, FIM_NOVO_B, color = GREEN)
    self.play(Write(juntar))
    self.wait()

    TRAPEZIO = Group(triangulo, NOVO_TRIANGULO, alfa, beta, RETO, juntar)

    self.play(TRAPEZIO.animate.shift(LEFT*4))

    a = Text("a", color = PINK).scale(0.7)
    a.set_x(-4.3)
    a.set_y(-1.1)
    a_novo = Text("a", color = PINK).scale(0.7)
    a_novo.set_x(-4.3)
    a_novo.set_y(0.7)
    b = Text("b").scale(0.7)
    b.set_x(-5.8)
    b.set_y(-1.1)
    b_novo = Text("b").scale(0.7)
    b_novo.set_x(-4.5)
    b_novo.set_y(2.3)
    c = Text("c", color = BLUE).scale(0.7)
    c_novo = Text("c", color = BLUE).scale(0.7)
    c.set_x(-4.5)
    c.set_y(-2.8)
    c_novo.set_x(-5.8)
    c_novo.set_y(1.2)

    self.play(Write(a))
    self.play(Write(b))
    self.play(Write(c))
    self.play(Write(a_novo))
    self.play(Write(b_novo))
    self.play(Write(c_novo))
    self.wait()

    inicio = Text("We can calculate this total area in two ways:").scale(0.6)
    forma1 = Text("Calculate the area of each triangle and sum them up").scale(0.5)
    forma2 = Text("or calculate the trapezoid area").scale(0.5)
    inicio.set_x(2)
    forma1.set_x(2)
    forma2.set_x(2)

    self.play(Write(inicio))
    self.play(inicio.animate.shift(UP*3))
    self.play(Write(forma1))
    self.play(forma1.animate.shift(UP*2))
    self.play(Write(forma2))
    self.play(forma2.animate.shift(UP*1))
    self.wait()

    texto1 = Text("First way:").scale(0.5)
    texto1.set_x(-1.5)

    self.play(Write(texto1))
    self.wait()

    contas_triangulos1 = MathTex(r"\frac{2cb}{2} + \frac{aa}{2}").scale(0.8)
    contas_triangulos1.set_x(-1)
    contas_triangulos1.set_y(-0.7)

    self.play(Write(contas_triangulos1))

    V_t = VGroup(triangulo_Vt, NOVO_TRIANGULO)
    isosceles = VGroup(ladoC, NOVO_C, juntar)
    rect_red = Rectangle(height= 1,width=0.8,color=RED)
    rect_red.set_x(-1.5)
    rect_red.set_y(-0.7)

    self.play(Write(rect_red))
    self.wait(0.5)
    self.play(Write(V_t.set_color(RED)))

    rect_blue = Rectangle(height= 1, width = 0.8, color=BLUE)
    rect_blue.set_x(-0.4)
    rect_blue.set_y(-0.7)

    self.play(Write(rect_blue))
    self.wait(0.5)
    self.play(Write(isosceles.set_color(BLUE)))
    self.wait()
    self.play(FadeOut(rect_red, rect_blue))
    
    texto2 = Text("Second way:").scale(0.5)
    texto2.set_x(2.5)
    contas_trapezio1 = MathTex(r"\frac{(b + c)(b + c)}{2}").scale(0.8)
    contas_trapezio1.set_x(3)
    contas_trapezio1.set_y(-0.7)

    self.play(Write(texto2))
    self.play(Write(contas_trapezio1))

    rect_yellow = Rectangle(height=1, width = 2.5, color = YELLOW)
    rect_yellow.set_x(3.0)
    rect_yellow.set_y(-0.7)
    retangulo_amarelo = VGroup(juntar, ladoA, NOVO_A, NOVO_B, ladoB)

    self.play(Write(rect_yellow))
    self.wait(0.5)
    self.play(Write(retangulo_amarelo.set_color(YELLOW)))
    self.wait(0.5)
    self.play(FadeOut(rect_yellow))

    equal = Text("Equaling them").scale(0.6)
    equal.set_x(1)
    equal.set_y(-2)

    self.play(Write(equal))
    self.wait()

    textos = VGroup(inicio, forma1, forma2, texto1, texto2, contas_triangulos1, contas_trapezio1, equal)

    self.play(Unwrite(textos))

    final1 = MathTex(r"\frac{2cb}{2} + \frac{aa}{2} = \frac{(b + c)(b + c)}{2}").scale(1)
    final1.set_x(1.5)
    final1.set_y(2.7)

    self.play(Write(final1))
    self.wait(0.5)

    final2 = MathTex(r"2cb + a^2 = (b + c)^2")
    final2.set_x(1.5)
    final2.set_y(1.3)

    self.play(Write(final2))
    self.wait(0.5)

    final3 = MathTex(r"2cb + a^2 = b^2 + 2cb + c^2")
    final3.set_x(1.5)
    final3.set_y(0.3)

    self.play(Write(final3))
    self.wait(0.5)

    final4 = MathTex(r"a^2 = b^2 + c^2")
    final4.set_x(1.5)
    final4.set_y(-0.9)

    self.play(Write(final4))
    self.wait(0.5)

    final_rect = Rectangle(height = 0.7, width = 3, color = RED)
    final_rect.set_x(1.5)
    final_rect.set_y(-0.9)

    self.play(FadeIn(final_rect))
    self.wait()

    grupo_limpar_tela = Group(NOVO_TRIANGULO, triangulo, a_novo, b_novo, c_novo, juntar, alfa, beta, RETO, final1, final2, final3, a, b, c)
    self.play(FadeOut(grupo_limpar_tela))

    finalV = VGroup(triangulo_Vt, a, b, c)
    finalV.set_x(-2)
    finalV.set_y(0)

    self.play(Write(finalV.set_color(WHITE)))
 
    self.wait(2)

    circ = Circle(color=WHITE, radius=1.2)
    y = Tex(r"$\mathbb{Y}$", color=RED).scale(5)
    triangle = Triangle(color=BLUE, fill_opacity=1).scale(0.3)
    square = Square(color=GREEN, fill_opacity=1).scale(0.2)
    square.set_x(-0.83)
    square.set_y(0.15)
    triangle.set_x(0.8)
    triangle.set_y(0.15)
    circ.set_y(0.1)
    group_intro = Group(y, triangle, square)
    final_group = Group(final_rect, finalV, final4)

    self.play(ReplacementTransform(final_group, circ))
    self.play(FadeIn(group_intro))
      
    self.wait()