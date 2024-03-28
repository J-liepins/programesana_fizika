import math
import numpy as np
from screen import Screen
class PhysicsObject:
    ey = 0
    ex = 0
    g = 0
    gf = 0
    f = 0
    

   
    
    def __init__(self, sx=Screen.SCR_WIDTH/2, sy=Screen.SCR_HEIGHT/2, svx=100, svy=0, sr = 20, sm = 1):
        self.x = sx
        self.y=sy
        self.vx= svx
        self.vy = svy
        self.r = sr
        self.physics = True
        self.m = sm 
    
    def physics_update(self, objs):
        if self.physics:
            # Apply vx and vy
            self.x += self.vx
            self.y += self.vy

            # Gravitational acceleration 
            self.vy+=Screen.FRAME_TIME * PhysicsObject.g

            # Collision resolution(wall)
            if (self.y + self.r >= Screen.SCR_HEIGHT and self.vy>0) or (self.y - self.r <= 0 and self.vy<0):
                self.vy *= PhysicsObject.ey
            if (self.x + self.r >= Screen.SCR_WIDTH and self.vx>0) or (self.x - self.r <= 0 and self.vx<0):
                self.vx *= PhysicsObject.ex
            
            # Drag un friction
            if (abs(self.vx) >= 0.01):
                sign = self.vx/abs(self.vx)
                diff = abs(PhysicsObject.f*self.vx) * Screen.FRAME_TIME
                res = abs(self.vx) - diff
                self.vx = sign * res
            else:
                 self.vx = 0
            if (abs(self.vy) >= 0.01):
                sign = self.vy/abs(self.vy)
                diff = abs(PhysicsObject.f*self.vy) * Screen.FRAME_TIME
                res = abs(self.vy) - diff
                self.vy = sign * res
            else:
                self.vx *= PhysicsObject.gf
                self.vy = 0
               
            
            # Collision with other physics objects
            for other_obj in objs:
                dx = self.x - other_obj.x
                dy = self.y- other_obj.y
                dist = (self.r+ other_obj.r)**2
                if (dx**2+dy**2<=dist):
                    if(dx!=0):
                        theta = math.atan(dy/dx)
                        vxorg=self.vx
                        vyorg=self.vy
                        othervxorg=other_obj.vx
                        othervyorg=other_obj.vy
                        
                        vx1= vxorg*math.cos(theta)+vyorg*math.sin(theta)
                        vy1= vxorg*math.sin(theta)+vyorg*math.cos(theta)
                        othervx1= othervxorg*math.cos(theta)+othervyorg*math.sin(theta)
                        othervy1= othervxorg*math.sin(theta)+othervyorg*math.cos(theta)
                        
                        vx2 = othervx1*(2*other_obj.m/(self.m+ other_obj.m))+vx1*(self.m-other_obj.m)/(self.m+other_obj.m)
                        othervx2 = othervx1*((other_obj.m-self.m)/(self.m+other_obj.m))+ vx1*((2*self.m/(self.m+ other_obj.m)))
                        # self.vx=vx2*math.cos(theta)
                        # other_obj.vx=othervx2*math.cos(theta)
                        self.vx=vx2
                        other_obj.vx=othervx2
                        
                        vy2 = othervy1*(2*other_obj.m/(self.m+ other_obj.m))+vy1*(self.m-other_obj.m)/(self.m+other_obj.m)
                        othervy2 = othervy1*((other_obj.m-self.m)/(self.m+other_obj.m))+ vy1*((2*self.m/(self.m+ other_obj.m)))
                        # self.vy=vy2*math.sin(theta)
                        # other_obj.vy=othervy2*math.sin(theta)
                        self.vy=vy2
                        other_obj.vy=othervy2
                        
                    #other_obj.vy = othervyorg*((other_obj.m-self.m)/(self.m+other_obj.m))+ vyorg*((2*self.m/(self.m+ other_obj.m)))
            # drag drop physics