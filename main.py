import math, pygame, time
screenwidth=1000
screenheight=700
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.init()
angle = 5
flenx = 100
fleny = 100

pi = math.pi
sin = math.sin
cos = math.cos
tan = math.tan
sqrt = math.sqrt
atan2 = math.atan2

def sit(x1, y1, z1, t, t1, t2, x2, y2, z2):
    B = y1-tan(t1)*x1
    B2 = z1-tan(t2)*(x1/cos(t1))
    D = tan(t1)
    C = tan(t2)*(1/cos(t1))
    n = z1-x1*tan(t2)*(1/cos(t1))
    X = (x2 - D*B + D*y2 - C*n + C*z2)/(1+D**2+C**2)
    Y = tan(t1)*X + B
    Z = tan(t2)*(X/cos(t1)) + B2
    
    a = atan2(sin(t2), cos(t1)*cos(t2))
    m2 = -1/(tan(t2)/cos(t1))
    b = -m2*X + Z
    xp = (x2 + m2*(z2-b))/(1+m2**2)
    zp = (b + m2*x2 + m2**2*z2)/(1+m2**2)
    dx, dy, dz = x2-xp, y2-Y, z2-zp
    dx2, dz2 = xp-X, zp-Z
    vx = -sin(t1)*cos(a)**2 
    vy = cos(t1)
    vz = -sin(t1)*cos(a)*sin(a)
    u = (dx*vx + dy*vy + dz*vz)/sqrt(vx**2 + vy**2 + vz**2)
    vx2 = cos(a+pi/2)
    vz2 = sin(a+pi/2)
    u2 = (dx2*vx2 + dz2*vz2)/sqrt(vx2**2 + vz2**2)
    
    s = abs(cos(t1))/cos(t1)
    vX = u*cos(s*t-pi/2) - u2*sin(s*t-pi/2)
    vY = u2*cos(s*t-pi/2) + u*sin(s*t-pi/2)
    wX = vX*cos(a+pi/2)
    wZ = vX*sin(a+pi/2)
    v = atan2(sin(t1)*cos(a), cos(t1))
    x_f = vY*cos(a)*cos(v-pi/2) + wX + X
    y_f = vY*sin(v-pi/2) + Y
    z_f = vY*sin(a)*cos(v-pi/2) + wZ + Z
    #print(x_f, y_f, z_f)
    if(z_f!=0):
        x = screenwidth/2 + flenx * x_f/z_f
        y = screenheight/2 + fleny * y_f/z_f
        pygame.draw.circle(screen, "red", (x, y), 10)

def sitb(x1, y1, z1, t, t1, t2, x2, y2, z2):
    kx = math.cos(t2) * math.cos(t1)
    ky = math.cos(t2) * math.sin(t1)
    kz = math.sin(t2)

    # Vector from rotation center
    px, py, pz = x2 - x1, y2 - y1, z2 - z1

    c = math.cos(t)
    s = math.sin(t)

    # Rodrigues’ rotation
    x_f = x1 + px*c + (ky*pz - kz*py)*s + kx*(kx*px + ky*py + kz*pz)*(1-c)
    y_f = y1 + py*c + (kz*px - kx*pz)*s + ky*(kx*px + ky*py + kz*pz)*(1-c)
    z_f = z1 + pz*c + (kx*py - ky*px)*s + kz*(kx*px + ky*py + kz*pz)*(1-c)

    if(z_f!=0):
        x = screenwidth/2 + flenx * x_f/z_f
        y = screenheight/2 + fleny * y_f/z_f
        #print(x, y)
        pygame.draw.circle(screen, "blue", (x, y), 15)

def sitv2(x1, y1, z1, t, t1, t2, x2, y2, z2):
    pi = math.pi
    s = (x2-x1)*math.cos(t2)*math.cos(t1)+(y2-y1)*math.cos(t2)*math.sin(t1)+(z2-z1)*math.sin(t2)
    X = x1+s*math.cos(t2)*math.cos(t1)
    Y = y1+s*math.cos(t2)*math.sin(t1)
    Z = z1+s*math.sin(t2)

    a = math.atan2(math.sin(t2), math.cos(t1)*math.cos(t2))
    a2 = a+pi/2
    xp = (x2*cos(a2)**2) + (z2*sin(a2)*cos(a2)) + (X*sin(a2)**2) - (Z*sin(a2)*cos(a2))
    zp = (x2*sin(a2)*cos(a2)) + (z2*sin(a2)**2) - (X*sin(a2)*cos(a2)) + (Z*cos(a2)**2)
    dx, dy, dz = x2-xp, y2-Y, z2-zp
    dx2, dz2 = xp-X, zp-Z
    vx = -math.sin(t1)*math.cos(a)**2 
    vy = math.cos(t1)
    vz = -math.sin(t1)*math.cos(a)*math.sin(a)
    u = (dx*vx + dy*vy + dz*vz)/math.sqrt(vx**2 + vy**2 + vz**2)
    vx2 = math.cos(a+pi/2)
    vz2 = math.sin(a+pi/2)
    u2 = (dx2*vx2 + dz2*vz2)/math.sqrt(vx2**2 + vz2**2)

    o=-pi/2
    s = abs(math.cos(t1))/math.cos(t1)
    vX = u*math.cos(s*t+o) - u2*math.sin(s*t+o)
    vY = u2*math.cos(s*t+o) + u*math.sin(s*t+o)
    wX = vX*math.cos(a+pi/2)
    wZ = vX*math.sin(a+pi/2)
    v = math.atan2(math.sin(t1)*(math.cos(a)), math.cos(t1))
    x_f = vY*math.cos(a)*math.cos(v-pi/2) + wX + X
    y_f = vY*math.sin(v-pi/2) + Y
    z_f = vY*math.sin(a)*math.cos(v-pi/2) + wZ + Z
    if(z_f!=0):
        x = screenwidth/2 + flenx * x_f/z_f
        y = screenheight/2 + fleny * y_f/z_f
        #print(x, y)
        pygame.draw.circle(screen, "green", (x, y), 5)    

time.sleep(1)
while True:
    sitb(-15, 40, 5, angle, math.radians(80), math.radians(130), 20, 70, 50)
    sit(-15, 40, 5, angle, math.radians(80), math.radians(130), 20, 70, 50)
    sitv2(-15, 40, 5, angle, math.radians(80), math.radians(130), 20, 70, 50)

    sitb(-15, 40, 5, angle, math.radians(230), math.radians(15), 20, 70, 50)
    sit(-15, 40, 5, angle, math.radians(230), math.radians(15), 20, 70, 50)
    sitv2(-15, 40, 5, angle, math.radians(230), math.radians(15), 20, 70, 50)
    
    sitb(-15, 40, 5, angle, math.radians(150), math.radians(15), 20, 70, 50)
    sit(-15, 40, 5, angle, math.radians(150), math.radians(15), 20, 70, 50)
    sitv2(-15, 40, 5, angle, math.radians(150), math.radians(15), 20, 70, 50)
    
    sitb(-15, 40, 5, angle, math.radians(220), math.radians(-15), 20, 70, 50)
    sit(-15, 40, 5, angle, math.radians(220), math.radians(-15), 20, 70, 50)
    sitv2(-15, 40, 5, angle, math.radians(220), math.radians(-15), 20, 70, 50)
    
    sitb(-15, 40, 5, angle, math.radians(30), math.radians(260), 20, 70, 50)
    sit(-15, 40, 5, angle, math.radians(30), math.radians(260), 20, 70, 50)
    sitv2(-15, 40, 5, angle, math.radians(30), math.radians(260), 20, 70, 50)
    
    sitb(-15, 40, 5, angle, math.radians(-80), math.radians(85), 20, 70, 50)
    sit(-15, 40, 5, angle, math.radians(-80), math.radians(85), 20, 70, 50)
    sitv2(-15, 40, 5, angle, math.radians(-80), math.radians(85), 20, 70, 50)
    
    sitb(-15, 40, 5, angle, math.radians(130), math.radians(110), 20, 80, -50)
    sit(-15, 40, 5, angle, math.radians(130), math.radians(110), 20, 80, -50)
    sitv2(-15, 40, 5, angle, math.radians(130), math.radians(110), 20, 80, -50)
    
    sitb(-15, 40, 5, angle, math.radians(-20), math.radians(123), 20, 30, 50)
    sit(-15, 40, 5, angle, math.radians(-20), math.radians(123), 20, 30, 50)
    sitv2(-15, 40, 5, angle, math.radians(-20), math.radians(123), 20, 30, 50)
    
    sitb(-15, 40, 5, angle, math.radians(20), math.radians(10), 20, 70, 50)
    sit(-15, 40, 5, angle, math.radians(20), math.radians(10), 20, 70, 50)
    sitv2(-15, 40, 5, angle, math.radians(20), math.radians(10), 20, 70, 50)

    pygame.display.update()
    time.sleep(0.05)
    screen.fill((0, 0, 0))
    angle+=math.radians(5)
