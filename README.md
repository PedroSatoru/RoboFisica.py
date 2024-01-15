# RoboFisica.py
Nesse projeto de fisica proposto pela FEI, criamos um algoritmo de um robo que deve interceptar uma bola com a trajetória fixa.
O nosso robo sempre ira para um ponto especifico do campo, que no caso é x=3.32 e y=3.78, aproximadamente no meio da trajetoria da bola.
Como aprofundamento decidimos fazer com que a interceptação seja mais realista, assim fazemos com que o robo ao chegar no ponto pre-determinado começe a seguir a trajetoria inversa da bola,
ao chegar em um raio de aproximadamente 1 metro da bola, ele inverterá sua trajetoria novamente para acompanhar a trajetoria da bola, porem utilizando metade da velocidade da mesma, assim proporcionando
uma interceptação mais realista.
