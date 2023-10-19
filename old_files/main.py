from PPlay.window import Window
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from menu import put_buttons_in_place_and_check_state


def game():
    screen = Window(1280, 720)
    screen.set_title("space invaders")

    ms_input = Mouse()
    kb_input = Keyboard()

    game_on = True
    start = True
    game_dif = 1
    
    while game_on:
        # Show menu 
        if start:
            screen.set_background_color((199, 165, 156))
            state =  False
            while not state:
                screen.update()
                state =  put_buttons_in_place_and_check_state(ms_input, screen)
                if state == 1 or state == 2 or state == 3:
                    game_dif = state
            if state == "exit":
                game_on = False
            start = False

        screen.set_background_color((0, 0, 0))
        screen.update()
        # Show menu now only if player press ESC
        if kb_input.key_pressed("ESC"):
            screen.set_background_color((199, 165, 156))
            state =  False
            while not state:
                screen.update()
                state =  put_buttons_in_place_and_check_state(ms_input, screen)
                if state == 1 or state == 2 or state == 3:
                    game_dif = state
            if state == "exit":
                game_on = False
            
                    
                
            

            
                

if __name__ == "__main__":
    game()
    
