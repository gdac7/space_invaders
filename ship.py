from PPlay.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen):
        super().__init__("imgs/ship.png")
        self.set_position(screen.width/2 - self.width, screen.height - 2 * self.height)
        self.speed = 150
        self.shot_speed = 500
        self.shot_particles = []

    def move(self, keyboard, screen):
        if keyboard.key_pressed("left") and self.x > 0:
            self.x -= self.speed * screen.delta_time()
        if keyboard.key_pressed("right") and self.x < screen.width - self.width:
            self.x += self.speed * screen.delta_time()

    def shoot(self):
        shot_particle = Sprite("imgs/shot.png")
        shot_particle.set_position(self.x + self.width/2, self.y)
        self.shot_particles.append(shot_particle)
       

    def check_shot_particles(self, screen):
        for sp in self.shot_particles:
            sp.draw()
            if sp.y > - 10:
                sp.y -= self.shot_speed * screen.delta_time()
            else:
                del self.shot_particles[self.shot_particles.index(sp)]
   





