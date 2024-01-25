import numpy as np
from screen import Screen
class PhysicsObject:
    r = 20
    ey = -1.5
    ex = -1
    g = 5
    # # f is proportional to rho and proportional to v^2
    rho = 10
    const = 0.06
    f = const * rho

    global x_value
    global y_value
    x_value=0
    y_value=0
    def __init__(self, sx=Screen.SCR_WIDTH/2, sy=Screen.SCR_HEIGHT/2, svx=100, svy=0):
        self.x = sx
        self.y=sy
        self.vx=x_value
        self.vy = y_value
        self.physics = True
    
    def physics_update(self, objs):
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
                self.vx *= 0.9
                self.vy = 0
            if (abs(self.vx) < 0.01):
                self.vx = 0
            
            # Collision with other physics objects
            for other_obj in objs:
                dx = self.x - other_obj.x
                dy =self.y- other_obj.y
                dist = (self.r+ other_obj.r)**2
                if (dx**2+dy**2<dist):
                    ox = dist - dx**2
                    oy = dist - dy**2 
                    self.vx += np.sign(dx) * ox * 0.001
                    self.vy += np.sign(dy) * oy * 0.001
                    other_obj.vx -= np.sign(dx) * ox * 0.001
                    other_obj.vy -= np.sign(dy) * oy * 0.001
                    # self.vx, other_obj.vx = other_obj.vx * 0.8, self.vx * 0.8
                    # self.vy, other_obj.vy = other_obj.vy * 0.8, self.vy * 0.8
            # drag drop physics