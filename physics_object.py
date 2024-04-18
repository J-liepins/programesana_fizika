import math
import numpy as np
from screen import Screen
class PhysicsObject:
    ey = 0
    ex = 0
    g = 0
    gf = 0
    f = 0   
    eb = 0
    epsilon = 0.0001
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
            if (self.y + self.r >= Screen.SCR_HEIGHT):
                self.y = Screen.SCR_HEIGHT-self.r
                self.vy *= PhysicsObject.ey
            else:
                if(self.y - self.r <= 0):
                    self.y = self.r
                    self.vy *= PhysicsObject.ey

            if (self.x + self.r >= Screen.SCR_WIDTH):
                self.x = Screen.SCR_WIDTH-self.r
                self.vx *= PhysicsObject.ex
            else:
                if(self.x - self.r <= 0):
                    self.x = self.r
                    self.vx *= PhysicsObject.ex 
            if (self.y> Screen.SCR_HEIGHT-self.r-1 and self.vy<0.2*PhysicsObject.g and self.vy>-0.2*PhysicsObject.g and PhysicsObject.g !=0 ):
               self.vy=0

            
            
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
               
            
            for other_obj in objs:
                # If self, continue
                if self == other_obj: continue
                
                # If not colliding, continue
                dx = other_obj.x - self.x
                dy = other_obj.y - self.y
                dist = math.sqrt(dx**2 + dy**2)+PhysicsObject.epsilon
                if (dist > (self.r + other_obj.r)): continue

                normal = np.array([dx / dist, dy / dist]) 
                tangent = np.array([normal[1] * -1, normal[0]])

                # Calculate overlap
                overlap = (self.r + other_obj.r) - dist

                # Adjust positions to separate objects
                self.x -= normal[0] * overlap / 2
                self.y -= normal[1] * overlap / 2
                other_obj.x += normal[0] * overlap / 2
                other_obj.y += normal[1] * overlap / 2

                v1 = np.array([self.vx, self.vy])
                v2 = np.array([other_obj.vx, other_obj.vy])
              

                scalar1norm = np.dot(normal, v1)
                scalar2norm = np.dot(normal, v2)
                scalar1tan = np.dot(tangent, v1)
                scalar2tan = np.dot(tangent, v2)

                scalar1norm_after = (scalar1norm * (self.m - other_obj.m) + 2 * other_obj.m * scalar2norm) / (self.m + other_obj.m)
                scalar2norm_after = (scalar2norm * (other_obj.m - self.m) + 2 * self.m * scalar1norm) / (self.m + other_obj.m)
                    
                vector1norm_after = normal * scalar1norm_after
                vector2norm_after = normal * scalar2norm_after
                vector1norm = tangent * scalar1tan
                vector2norm = tangent * scalar2tan

                v1_after = vector1norm + vector1norm_after
                v2_after = vector2norm + vector2norm_after
                self.vx = PhysicsObject.eb * v1_after[0]
                self.vy = PhysicsObject.eb * v1_after[1]
                other_obj.vx = PhysicsObject.eb * v2_after[0]
                other_obj.vy = PhysicsObject.eb * v2_after[1]
