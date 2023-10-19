from PPlay.gameimage import GameImage


PLAY = 1
RANKING = 3
EXIT = 4
DIFFICULT_EASY = 5
DIFFICULT_MEDIUM = 6
DIFFICULT_HARD = 7
BACK = 8

BG_COLOR = (199, 165, 156)


def btn_start_point(btn):
    """Return start point of button"""
    return btn.x, btn.y


def btn_end_point(btn):
    """Return end point of menu button"""
    return btn.x + btn.width, btn.y + btn.height


class Menu:
    def __init__(self, screen):
        self.screen = screen
        # Criando tudo que o menu vai ter
        self.bg = GameImage("imgs/menu_bg.png")
        self.bg.set_position(
            screen.width/2 - self.bg.width/2,
            screen.height/2 - self.bg.height/2)
        self.play_btn = GameImage("imgs/btn/jogar_button.png")
        self.difficult_btn = GameImage("imgs/btn/diff_button.png")
        self.ranking_btn = GameImage("imgs/btn/ranking_button.png")
        self.exit_btn = GameImage("imgs/btn/sair_button.png")
        # Botões do menu de dificuldade
        self.dif1_btn = GameImage("imgs/btn/dif1_button.png")
        self.dif2_btn = GameImage("imgs/btn/dif2_button.png")
        self.dif3_btn = GameImage("imgs/btn/dif3_button.png")
        self.back_btn = GameImage("imgs/btn/voltar_btn.png")

        # Botando os botões em suas posições
        self.play_btn.set_position(self.bg.x + self.bg.width/2 - self.play_btn.width/2, self.bg.y + self.play_btn.height)
        self.difficult_btn.set_position(self.bg.x + self.bg.width/2 - self.difficult_btn.width/2, self.bg.y + 3 * self.play_btn.height)
        self.ranking_btn.set_position(self.bg.x + self.bg.width/2 - self.ranking_btn.width/2, self.bg.y + 5*self.play_btn.height)
        self.exit_btn.set_position(self.bg.x + self.bg.width/2 - self.exit_btn.width/2, self.bg.y + 8 * self.play_btn.height)
        # Botões do menu de dificuldade
        self.dif1_btn.set_position(self.bg.x + self.bg.width/5 - self.dif1_btn.width/2, self.bg.y + self.dif1_btn.height)
        self.dif2_btn.set_position(self.bg.x + self.bg.width/5 - self.dif2_btn.width/2, self.bg.y + 3 * self.dif1_btn.height)
        self.dif3_btn.set_position(self.bg.x + self.bg.width/5 - self.dif3_btn.width/2, self.bg.y + 5 * self.dif1_btn.height)
        self.back_btn.set_position(self.bg.x + self.bg.width/5 - self.back_btn.width/2, self.bg.y + 8 * self.dif1_btn.height)

    def draw_menu(self):
        self.bg.draw()
        self.play_btn.draw()
        self.difficult_btn.draw()
        self.ranking_btn.draw()
        self.exit_btn.draw()

    def check_btn_state(self, mouse):
        """Verifica se o usuário clicou no botão"""
        if mouse.is_button_pressed(1):
            if mouse.is_over_area(btn_start_point(self.play_btn), btn_end_point(self.play_btn)):
                return PLAY
            if mouse.is_over_area(btn_start_point(self.difficult_btn), btn_end_point(self.difficult_btn)):
                return self.show_diff_menu(mouse)
            if mouse.is_over_area(btn_start_point(self.ranking_btn), btn_end_point(self.ranking_btn)):
                return RANKING
            if mouse.is_over_area(btn_start_point(self.exit_btn), btn_end_point(self.exit_btn)):
                return EXIT

    def show_diff_menu(self, mouse):
        btn_clicked = False
        while not btn_clicked:
            self.screen.set_background_color(BG_COLOR)
            self.bg.draw()
            self.screen.draw_text("FÁCIL", self.bg.x + self.bg.width/2, self.bg.y + 1.4 * self.dif1_btn.height, 20)
            self.screen.draw_text("MÉDIO", self.bg.x + self.bg.width/2, self.bg.y + 3.4 * self.dif1_btn.height, 20)
            self.screen.draw_text("DIFÍCIL", self.bg.x + self.bg.width/2, self.bg.y + 5.4 * self.dif1_btn.height, 20)
            self.screen.draw_text("VOLTAR", self.bg.x + self.bg.width/2, self.bg.y + 8.4 * self.dif1_btn.height, 20)
            self.dif1_btn.draw()
            self.dif2_btn.draw()
            self.dif3_btn.draw()
            self.back_btn.draw()
            if mouse.is_button_pressed(1):
                if mouse.is_over_area(btn_start_point(self.dif1_btn), btn_end_point(self.dif1_btn)):
                    btn_clicked = DIFFICULT_EASY
                if mouse.is_over_area(btn_start_point(self.dif2_btn), btn_end_point(self.dif2_btn)):
                    btn_clicked = DIFFICULT_MEDIUM
                if mouse.is_over_area(btn_start_point(self.dif3_btn), btn_end_point(self.dif3_btn)):
                    btn_clicked = DIFFICULT_HARD
                if mouse.is_over_area(btn_start_point(self.back_btn), btn_end_point(self.back_btn)):
                    btn_clicked = BACK
            self.screen.update()

        return btn_clicked

