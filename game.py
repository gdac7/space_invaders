from menu import Menu, PLAY, RANKING, EXIT, DIFFICULT_EASY, DIFFICULT_MEDIUM, DIFFICULT_HARD
from ship import Ship
from enemy import ControlEnemys
from PPlay.window import Window
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
import pygame
BG_COLOR = (199, 165, 156)


class Game:
    def __init__(self):
        self.mouse = Mouse()
        self.keyboard = Keyboard()
        self.screen = Window(800, 600)
        self.screen.set_title("space invaders")
        self.game_on = True
        self.clock = pygame.time.Clock()
        self.is_showing_menu = True
        self.menu = Menu(self.screen)
        self.ship = Ship(self.screen)
        self.enemies = ControlEnemys(self.screen)
        self.difficult = 0
        self.points = 0

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
        delay_shoot = 0.25
        tick_shoot = delay_shoot
        while self.game_on:
            if self.is_showing_menu:
                self.show_menu()
            if not self.is_showing_menu:
                self.screen.set_background_color((0, 0, 0))
                if self.keyboard.key_pressed("ESC"):
                    self.is_showing_menu = True
                tick_shoot += self.screen.delta_time()
                if self.keyboard.key_pressed("SPACE"):
                    if tick_shoot > delay_shoot:
                        self.ship.shoot()
                        tick_shoot = 0
                else:
                    self.ship.can_shoot = True
                
                self.ship.draw()
                self.enemies.draw_enemies()
                self.ship.move(self.keyboard, self.screen)
                self.enemies.move_enemies()
                self.ship.check_shot_particles(self.screen)
                self.points = self.enemies.check_shot_collision(self.ship.shot_particles, self.points)
                if self.enemies.check_game_over(self.ship.y):
                    break
            self.clock.tick()
            self.screen.draw_text(f"{int(self.clock.get_fps())}", 20, 500, 15, (255, 255, 255))
            self.screen.draw_text(f"{self.points}", 750, 500, 15, (255, 0, 0))
            self.screen.update()

