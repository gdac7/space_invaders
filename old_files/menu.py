import pygame
from PPlay.gameimage import GameImage
from PPlay.window import Window



def create_menu(s):
    menu = GameImage("../imgs/menu_bg.png")
    menu.set_position(s.width/2 - menu.width/2, s.height/2 - menu.height/2)
    return menu



def put_buttons_in_place_and_check_state(ms, screen):
    menu = create_menu(screen)
    menu_txt = GameImage("../imgs/menu_txt.png")
    menu.draw()
    # Set buttons and positions
    play = GameImage("../imgs/btn/jogar_button.png")
    difficult = GameImage("../imgs/btn/diff_button.png")
    ranking = GameImage("../imgs/btn/ranking_button.png")
    exit = GameImage("../imgs/btn/sair_button.png")
    
    
    menu_txt.set_position(menu.x + menu.width/2 - menu_txt.width/2, menu.y - menu_txt.height)
    play.set_position(menu.x + menu.width/2 - play.width/2, menu.y + play.height)
    difficult.set_position(menu.x + menu.width/2 - difficult.width/2, menu.y + 3*play.height)
    ranking.set_position(menu.x + menu.width/2 - ranking.width/2, menu.y + 5*play.height)
    exit.set_position(menu.x + menu.width/2 - exit.width/2, menu.y + 8*play.height)

    menu_txt.draw()
    play.draw()
    difficult.draw()
    ranking.draw()
    exit.draw()

    # Check click on buttons
    if ms.is_button_pressed(1):
        # Play btn
        if ms.is_over_area((play.x, play.y), (play.x + play.width, play.y + play.height)):
            return 1
        # Diff btn
        if ms.is_over_area((difficult.x, difficult.y), (difficult.x + difficult.width, difficult.y + difficult.height)):
            state = False
            while not state:
                state = game_levels(menu, ms, screen)
                screen.update()
            if state == 1:
                return 1
            if state == 2:
                return 2
            if state == 3:
                return 3
            if state == 4:
                return False
        # Ranking btn
        if ms.is_over_area((ranking.x, ranking.y), (ranking.x + ranking.width, ranking.y + ranking.height)):
            pass
        # Exit btn
        if ms.is_over_area((exit.x, exit.y), (exit.x + exit.width, exit.y + exit.height)):
           return 'exit'

    return False

def game_levels(menu, ms, s: Window):
    menu = create_menu(s)
    menu.draw()

   
    
    dif1_btn =  GameImage("../imgs/btn/dif1_button.png")
    dif2_btn = GameImage("../imgs/btn/dif2_button.png")
    dif3_btn = GameImage("../imgs/btn/dif3_button.png")
    voltar_btn = GameImage("../imgs/btn/voltar_btn.png")

    dif1_btn.set_position(menu.x + menu.width/5 - dif1_btn.width/2, menu.y + dif1_btn.height)
    dif2_btn.set_position(menu.x + menu.width/5 - dif2_btn.width/2, menu.y + 3 * dif1_btn.height)
    dif3_btn.set_position(menu.x + menu.width/5 - dif3_btn.width/2, menu.y + 5 * dif1_btn.height)
    voltar_btn.set_position(menu.x + menu.width/5 - voltar_btn.width/2, menu.y + 8 * dif1_btn.height)

    s.draw_text("FÁCIL", menu.x + menu.width/2, menu.y + 1.4 * dif1_btn.height, 20)
    s.draw_text("MÉDIO", menu.x + menu.width/2, menu.y + 3.4 * dif1_btn.height, 20)
    s.draw_text("DIFÍCIL", menu.x + menu.width/2, menu.y +  5.4 *dif1_btn.height, 20)
    s.draw_text("VOLTAR", menu.x + menu.width/2, menu.y +  8 *dif1_btn.height, 20)

 


    dif1_btn.draw()
    dif2_btn.draw()
    dif3_btn.draw()
    voltar_btn.draw()
    
    # Check click on buttons
    
    if ms.is_button_pressed(1):
        if ms.is_over_area((dif1_btn.x, dif1_btn.y), (dif1_btn.x + dif1_btn.width, dif1_btn.y + dif1_btn.height)):
            return 1
        if ms.is_over_area((dif2_btn.x, dif2_btn.y), (dif2_btn.x + dif2_btn.width, dif2_btn.y + dif2_btn.height)):
            return 2
        if ms.is_over_area((dif3_btn.x, dif3_btn.y), (dif3_btn.x + dif3_btn.width, dif3_btn.y + dif3_btn.height)):
            return 3
        if ms.is_over_area((voltar_btn.x, voltar_btn.y), (voltar_btn.x + voltar_btn.width, voltar_btn.y + voltar_btn.height)):
            return 4

    return False


    






    
