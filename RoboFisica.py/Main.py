import matplotlib.pyplot as plt
from math import *
import numpy as np

def calc_difx(x):
    return xf - x

def calc_dify(y):
    return yf - y

def calc_teta(dy,dx):
   if dx == 0:
       return 90
   elif dy == 0:
       return 0
   else:
       return np.arctan(dy/dx)

def calc_ax (tet, tet2):

    ace = cos(tet) * 2.8
    
    verif = verif_vel(vel_y[-1], vel_x[-1])
    if verif >= 2.8 and tet2 == tet:
        ace = 0
    
    if tet == radians(90):
        ace = 0
    elif tet == radians(0):
        ace = 2.8

    ace_x.append(ace)

    return ace

def calc_ay (tet, tet2):

    ace = sin(tet) * 2.8
    
    verif = verif_vel(vel_y[-1], vel_x[-1])
    if verif >= 2.8 and tet2 == tet:
        ace = 0
    
    if tet == radians(90):
        ace = 2.8
    elif tet == radians(0):
        ace = 0


    ace_y.append(ace)

    return ace

def calc_vx (t, tet, tet2):
    ax = calc_ax(tet, tet2)

    if tet == radians(90):
        velo = 0

    elif ax != 0:
        velo = ax * t

    else: 
        velo = vel_x[-1]
    
    if velo > 2.8:
        velo = 2.8

    vel_x.append(velo)

    return velo
    
def calc_vy (t, tet, tet2):
    ay = calc_ay(tet, tet2)

    if tet == radians(0):
        velo = 0

    elif ay != 0:
        velo = ay * t
    else: 
        velo = vel_y[-1]
    
    if velo > 2.8:
        velo = 2.8

    vel_y.append(velo)

    return velo

def verif_vel(vy, vx):
    return sqrt(vy**2 + vx**2)

def verif_dist(x1,y1,x2,y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


# Equação para a trajetória da bola
def equacao_bola(x):
  return 0.0139 * x**3 - 0.2837 * x**2 + 2.4326 * x - 1.6791

def pos_x(t):
    return 0.005 * t**3 + 1E-14 * t**2 + 0.5 * t + 1

def pos_y(t):
    return -0.02 * t**2 + 0.9 * t + 0.5

def velocidade_x(t):
    return -3E-15*pow(t,3) + 0.015*pow(t,2) - 0.0003*t + 0.5

def velocidade_y(t):
    return -0.04*t + 0.9004

def aceleracao_x(t):
    return 0.03*t - 0.0006

def aceleracao_y():
    return -0.04




x0 = float(input("Digite a posição inicial x do robo: "))
y0 = float(input("Digite a posição inicial y do robo: "))
xf = 3.32
yf = 3.78

a = 2.8

tx_tempo = 0.02


posicoes_x = [x0]
posicoes_y = [y0]
ace_x = [0]
ace_y = [0]
vel_x = [0]
vel_y = [0]

# Posição inicial da bola
inicio_x_bola = 1
inicio_y_bola = 0.5

velocidade_x_bola = [0.5]
velocidade_y_bola = [0.9004]

aceleracao_x_bola = [-0.0006,0]
aceleracao_y_bola = [-0.04,-0.04]

posicoes_x_bola = [inicio_x_bola]  # Posição inicial da bola em x
posicoes_y_bola = [inicio_y_bola]  # Posição inicial da bola em y

distancias = [verif_dist(posicoes_x[-1],posicoes_y[-1],posicoes_x_bola[-1],posicoes_y_bola[-1])]

incremento = 0

tempos = [tx_tempo]

difx = calc_difx(posicoes_x[-1])
dify = calc_dify(posicoes_y[-1])

teta_at = calc_teta(dify, difx)

while posicoes_x[-1] != xf and posicoes_y[-1] != yf:

    tempos.append(tempos[-1] + tx_tempo)

    
    posicoes_x_bola.append(pos_x(tempos[-1]))
    posicoes_y_bola.append(pos_y(tempos[-1]))

    
    velocidade_x_bola.append(velocidade_x(tempos[-1]))
    velocidade_y_bola.append(velocidade_y(tempos[-1]))

    if incremento >= 1:
        aceleracao_x_bola.append(aceleracao_x(tempos[-1]))
        aceleracao_y_bola.append(aceleracao_y())

    distancia = verif_dist(posicoes_x[-1],posicoes_y[-1],posicoes_x_bola[-1],posicoes_y_bola[-1])   

    if distancia < 0.5:

        difx = calc_difx(posicoes_x[-1])
        dify = calc_dify(posicoes_y[-1])

        if difx < dify:
            teta_at = radians(0)

        else:
            teta_at = radians(90)
    
    elif distancia > 0.9:

        difx = calc_difx(posicoes_x[-1])
        dify = calc_dify(posicoes_y[-1])

        teta_at = calc_teta(dify, difx)

        


    
    if incremento == 0:
        teta_pas = teta_at

    vey = calc_vy(tempos[-1], teta_at, teta_pas)
    vex = calc_vx(tempos[-1], teta_at, teta_pas)

    teta_pas = teta_at

    posicoes_x.append(min(posicoes_x[-1] + vex * tx_tempo, xf))
    posicoes_y.append(min(posicoes_y[-1] + vey * tx_tempo,yf))

    incremento += 1

    distancias.append(distancia)

    if distancia <= 0.112:
        print("O robô interceptou a trajetória da bola. Parando o movimento.")
        break
tempo2 = 4

while distancia > 0.5:
    
    tempos.append(tempos[-1] + tx_tempo)
    tempo2 -= 0.02

    
    posicoes_x_bola.append(pos_x(tempos[-1]))
    posicoes_y_bola.append(pos_y(tempos[-1]))

    
    velocidade_x_bola.append(velocidade_x(tempos[-1]))
    velocidade_y_bola.append(velocidade_y(tempos[-1]))

    
    aceleracao_x_bola.append(aceleracao_x(tempos[-1]))
    aceleracao_y_bola.append(aceleracao_y())

     
    velocidade_atual_x_robo = velocidade_x(tempo2)
    deslocamento_x_robo = velocidade_atual_x_robo * 0.02
    posicoes_x.append( posicoes_x[-1] - deslocamento_x_robo)

    posicoes_y.append(equacao_bola(posicoes_x[-1]))

    
    vel_x.append(velocidade_x(tempos[-1]))
    vel_y.append(velocidade_y(tempos[-1]))

    
    ace_x.append(aceleracao_x(tempos[-1]))
    ace_y.append(aceleracao_y())
    
    
    distancia = verif_dist(posicoes_x[-1],posicoes_y[-1],posicoes_x_bola[-1],posicoes_y_bola[-1])
    distancias.append(distancia)

    if distancia <= 0.112:
        print("O robô interceptou a trajetória da bola. Parando o movimento.")
        break

tempo2 = tempos[-1]

while distancia >  0.112:
    
    tempos.append(tempos[-1] + tx_tempo)
    tempo2 += 0.02

    
    posicoes_x_bola.append(pos_x(tempos[-1]))
    posicoes_y_bola.append(pos_y(tempos[-1]))

    
    velocidade_x_bola.append(velocidade_x(tempos[-1]))
    velocidade_y_bola.append(velocidade_y(tempos[-1]))

    
    aceleracao_x_bola.append(aceleracao_x(tempos[-1]))
    aceleracao_y_bola.append(aceleracao_y())



   
    velocidade_atual_x_robo = velocidade_x(tempo2) / 1.35
    deslocamento_x_robo = velocidade_atual_x_robo * 0.02
    posicoes_x.append( posicoes_x[-1] + deslocamento_x_robo)

    posicoes_y.append(equacao_bola(posicoes_x[-1]))

    
    vel_x.append(velocidade_x(tempos[-1]) / 1.35)
    vel_y.append(velocidade_y(tempos[-1]) / 1.35)

    
    ace_x.append(aceleracao_x(tempos[-1]) / 1.35)
    ace_y.append(aceleracao_y() * 1.35)
    


    
    
    distancia = verif_dist(posicoes_x[-1],posicoes_y[-1],posicoes_x_bola[-1],posicoes_y_bola[-1])
    distancias.append(distancia)

    if distancia <= 0.112:
        print("O robô interceptou a trajetória da bola. Parando o movimento.")
        break

  

while True:

    print("1 - Trajetorias em um plano xy")
    print("2 - Coordenadas x,y em funcao de t")
    print("3 - Componentes vx, vy em funcao do tempo")
    print("4 - Componentes ax, ay em funcao do tempo")
    print("5 - Distancia entre a bola e o robo")
    print("0 - Sair")
    print()
    stch = int(input("Digite a opcao de grafico desejada: "))

    plt.figure(figsize=(12, 5))

    if stch==1:



        plt.plot(posicoes_x, posicoes_y, label='xy robo')
        plt.plot(posicoes_x_bola, posicoes_y_bola, label='xy bola')
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Trajetória do robô e bola')
        plt.legend()

        
    elif stch==2:

        plt.plot(tempos, posicoes_x, label='x robo')
        plt.plot(tempos, posicoes_y, label='y robo')
        plt.plot(tempos, posicoes_x_bola, label='x bola')
        plt.plot(tempos, posicoes_y_bola, label='y bola')
        plt.xlabel('Tempo (s)')
        plt.ylabel('x e y (m)')
        plt.title('Coordenadas x e y do robô em função do tempo')
        plt.legend()

    

    elif stch==3:


        plt.subplot(2, 2, 1)
        plt.plot(tempos, vel_x, label='vx robo')
        plt.plot(tempos, vel_y, label='vy robo')
        plt.xlabel('Tempo (s)')
        plt.ylabel('vx e vy (m/s)')
        plt.title('Componentes vx e vy do robô em função do tempo')
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(tempos, velocidade_x_bola, label='vx bola')
        plt.plot(tempos, velocidade_y_bola, label='vy bola')
        plt.xlabel('Tempo (s)')
        plt.ylabel('vx e vy (m/s)')
        plt.title('Componentes vx e vy da bola em função do tempo')
        plt.legend()

    elif stch==4:


        plt.subplot(2, 2, 1)
        plt.plot(tempos, ace_x, label='ax robo')
        plt.plot(tempos, ace_y, label='ay robo')
        plt.xlabel('Tempo (s)')
        plt.ylabel('ax e ay (m/s^2)')
        plt.title('Componentes ax e ay do robô em função do tempo')
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(tempos, aceleracao_x_bola, label='ax bola')
        plt.plot(tempos, aceleracao_y_bola, label='ay bola')
        plt.xlabel('Tempo (s)')
        plt.ylabel('ax e ay (m/s^2)')
        plt.title('Componentes ax e ay da bola em função do tempo')
        plt.legend()

    elif stch==5:
        plt.plot(tempos, distancias, label='ax por t',linestyle='--')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Distancia relativa (m)')
        plt.title('Distancia relativa entre o robo e a bola')
        plt.legend()

    if stch == 0:
        break

    elif stch >= 1 or stch <= 5:

        plt.tight_layout()
        plt.show()


    else:

        print("Digite uma opcao valida :")