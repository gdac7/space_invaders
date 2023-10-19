from menu import Menu, PLAY, RANKING, EXIT, DIFFICULT_EASY, DIFFICULT_MEDIUM, DIFFICULT_HARD
from ship import Ship
from PPlay.window import Window
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse

BG_COLOR = (199, 165, 156)


class Game:
    def __init__(self):
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.screen = Window(800, 600)
        self.screen.set_title("space invaders")
        self.game_on = True
        self.is_showing_menu = True
        self.menu = Menu(self.screen)
        self.ship = Ship(self.screen)
        self.difficult = 0

    def show_menu(self):
        self.screen.set_background_color(BG_COLOR)
        self.menu.draw_menu()
        btn_clicked = self.menu.check_btn_state(self.mouse)
        if btn_clicked == PLAY:
            self.is_showing_menu = False
        elif btn_clicked == RANKING:
            pass
        elif btn_clicked == DIFFICULT_EASY:
            self.difficult = 1
        elif btn_clicked == DIFFICULT_MEDIUM:
            self.difficult = 2
        elif btn_clicked == DIFFICULT_HARD:
            self.difficult = 3
        elif btn_clicked == EXIT:
            self.game_on = False

    def run(self):
        while self.game_on:
            if self.is_showing_menu:
                self.show_menu()
            if not self.is_showing_menu:
                self.screen.set_background_color((0, 0, 0))
                if self.keyboard.key_pressed("ESC"):
                    self.is_showing_menu = True
                # Se o usuário estiver pressionando espaço, atira
                # Mas se ele continuar pressionando, desativa a possibilidade de atirar
                # Pois, se estiver habilitado, basta o usuário pressionar espaço
                # Para atirar infinitamente, ou seja, o jogo ficará apenas na movimentação
                # Já que o tiro será "automático"
                if self.keyboard.key_pressed("SPACE"):
                    self.ship.shoot()
                    self.ship.can_shoot = False
                else:
                    self.ship.can_shoot = True
                self.ship.draw()
                self.ship.move(self.keyboard, self.screen)
                self.ship.check_shot_particles(self.screen)
            self.screen.update()

