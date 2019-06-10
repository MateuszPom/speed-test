import pygame, sys


class Main:
    def __init__(self):
        pygame.init()

        # tworzenie okna gry
        self.screen = pygame.display.set_mode((1000, 500))
        pygame.display.set_caption('Tester szybkości pisania')


        #operacje na tekscie
        self.my_font = pygame.font.SysFont("comicsansms", 30, True)
        self.file = open("text.txt", "r")
        self.line = self.file.readline()[:-1]
        self.text = ''
        self.mistakes = [0]

        self.clock = pygame.time.Clock()  # zegarek do mierzenia czasu dla mechanizmu odwiezania programu
        self.delta_tps = 0.0  # zmienna do pamietania czasu
        self.max_tps = 60  # czestotliwosc odswiezania programu [1/s]


        self.switch = True


        #mechanika gry
    def tick(self):
        if self.switch:
            if self.text == self.line:
                self.new_line()

        #generowanie tekstu w oknie gry
    def draw(self):
        if self.line == '':
            self.switch = False
            self.draw_table()
        else:
            label1 = self.my_font.render("{}".format(str(self.line)), 1, (255, 255, 255))  # etykieta, ktora przechowuje w sobie obraz ciagu znakow
            label2 = self.my_font.render("{}".format(str(self.text)), 1, (255, 255, 255))  # self.my_font jest zdefiniowany w konstruktorzrt]e
            label4 = self.my_font.render("Bledy: {}".format(str(self.mistakes[-1])), 1, (255, 255, 255))
            self.screen.blit(label1, (10, 10))
            self.screen.blit(label2, (10, 40))
            self.screen.blit(label4, (800, 40))


        #funkcja do wywolywania nowej linii
    def new_line(self):
        self.line = self.file.readline()[:-1]
        self.text = ''
        if self.line != '':
            self.mistakes.append(0)


        #rysowanie tabelki z wynikami
    def draw_table(self):
        label = self.my_font.render("Czy chcesz sprobowac ponownie? [y]-tak [n]-nie", 1, (255, 255, 255))
        self.screen.blit(label, (10, 10))
        for i in range(len(self.mistakes)):
            label = self.my_font.render("Zdanie {} Błędy: {}".format(i+1, self.mistakes[i]), 1, (255, 255, 255))


        #glowna funkcja programu w nieskonczonej petli
    def run(self):
        while True:

            # pobieranie znakow z klawiatury
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif event.key == pygame.K_n and not self.switch:
                        sys.exit(0)
                    elif event.key == pygame.K_y and not self.switch:
                        self.time = [0]
                        self.mistakes = [0]
                        self.switch = True
                        self.file = open("text.txt", "r")
                        self.text = ''
                        self.line = self.file.readline()[:-1]

                    else:
                        self.text += event.unicode
                        if len(self.text) != 0:
                            if len(self.text) > len(self.line) or self.text[-1] != self.line[len(self.text) -1]:
                                self.mistakes[-1] += 1

            self.tick()
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.update()

Main().run()