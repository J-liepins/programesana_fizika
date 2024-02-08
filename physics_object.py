import numpy as np
from screen import Screen
class PhysicsObject:
    ey = -1.5
    ex = -1
    g = 5
    # # f is proportional to rho and proportional to v^2
    rho = 10
    const = 0.06
    f = const * rho
    

   
    
    def __init__(self, sx=Screen.SCR_WIDTH/2, sy=Screen.SCR_HEIGHT/2, svx=100, svy=0, sr = 20, sm = 1):
        self.x = sx
        self.y=sy
        self.vx= svx
        self.vy = svy
        self.r = sr
        self.physics = True
        self.m=sm 
    
    def physics_update(self, objs):
        if self.physics:
            # Apply vx and vy
            self.x += self.vx
            self.y += self.vy

            # Gravitational acceleration 
            self.vy+=Screen.FRAME_TIME * PhysicsObject.g

            # Collision resolution
            if (self.y + self.r >= Screen.SCR_HEIGHT and self.vy>0) or (self.y - self.r <= 0 and self.vy<0):
                self.vy /= PhysicsObject.ey
            if (self.x + self.r >= Screen.SCR_WIDTH and self.vx>0) or (self.x - self.r <= 0 and self.vx<0):
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
                other_obj.m=1
                self.m=3
                dx = self.x - other_obj.x
                dy =self.y- other_obj.y
                dist = (self.r+ other_obj.r)**2
                if (dx**2+dy**2<dist):
                    self.vx = other_obj.vx(2*other_obj.m/(self.m+ other_obj.m))+self.vx(self.m-other_obj.m)/(self.m+other_obj.m)
                    self.vy = other_obj.vy(2*other_obj.m/(self.m+ other_obj.m))+self.vy(self.m-other_obj.m)/(self.m+other_obj.m)
                    other_obj.vx = other_obj.vx((self.m-other_obj.m)/(self.m-other_obj.m))+ self.vx((2*self.m/(self.m+ other_obj.m)))
                    other_obj.vy = other_obj.vx((self.m-other_obj.m)/(self.m-other_obj.m))+ self.vx((2*self.m/(self.m+ other_obj.m)))
                    # self.vx, other_obj.vx = other_obj.vx * 0.8, self.vx * 0.8
                    # self.vy, other_obj.vy = other_obj.vy * 0.8, self.vy * 0.8
            # drag drop physics