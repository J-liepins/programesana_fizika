from screen import Screen

class PhysicsObject:
    r = 20
    ey = -1.5
    ex = -1
    g = 9.81
    # # f is proportional to rho and proportional to v^2
    rho = 10
    const = 0.06
    f = const * rho

    def __init__(self, sx=Screen.SCR_WIDTH/2, sy=Screen.SCR_HEIGHT/2, svx=100, svy=0):
        self.x = sx
        self.y=sy
        self.vx=svx
        self.vy = svy
        self.physics = True
    
    def physics_update(self):
        if self.physics:
            # Apply vx and vy
            self.x += self.vx
            self.y += self.vy

            # Gravitational acceleration 
            self.vy+=Screen.FRAME_TIME * PhysicsObject.g

            # Collision resolution
            if (self.y + PhysicsObject.r >= Screen.SCR_HEIGHT and self.vy>0) or (self.y - PhysicsObject.r <= 0 and self.vy<0):
                self.vy /= PhysicsObject.ey
            if (self.x + PhysicsObject.r >= Screen.SCR_WIDTH and self.vx>0) or (self.x - PhysicsObject.r <= 0 and self.vx<0):
                self.vx /= PhysicsObject.ex
            
            # Drag
            if (abs(self.vx) > 0.01):
                sign = self.vx/abs(self.vx)
                diff = abs(PhysicsObject.f*self.vx) * Screen.FRAME_TIME
                res = abs(self.vx) - diff
                self.vx = sign * res
            if (abs(self.vy) > 0.01):
                sign = self.vy/abs(self.vy)
                diff = abs(PhysicsObject.f*self.vy) * Screen.FRAME_TIME
                res = abs(self.vy) - diff
                self.vy = sign * res
            
            # Ground friction
            if (abs(self.vy) < 0.01):
                self.vx *= 0.99
                self.vy = 0
            if (abs(self.vx) < 0.01):
                self.vx = 0