import math

import pygame
import random
import numpy as np

pygame.init()

e_coeff = 0.8
density = 1
my = 1

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

width = 800
height = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dynamics Simulation")
active = True
clock = pygame.time.Clock()


class ball:
    def __init__(self, mass, color, pos_x, pos_y, diameter, move_x, move_y):
        self.color = color
        self.mass = mass
        self.pos_vec = np.array([pos_x, pos_y])
        self.diameter = diameter
        self.mov_vec = np.array([move_x, move_y])


balls = []
for i in range(10):
    diameter = random.randint(25, 55)
    V = (4 / 3) * math.pi * math.pow((diameter / 2), 3)
    mass = density * V
    balls.append(
        ball(mass, white, 60.0 * i + 100.0, 60.0 * i + 100.0, diameter, random.randint(-4, 4),
             random.randint(-9, 9)))

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    screen.fill(black)

    E_sum = 0

    for i in range(len(balls)):
        pygame.draw.circle(screen, balls[i].color, [balls[i].pos_vec[0], balls[i].pos_vec[1]], balls[i].diameter / 2)

        balls[i].pos_vec += balls[i].mov_vec

        E = (1/2)*balls[i].mass*math.pow((np.linalg.norm(balls[i].mov_vec)), 2)
        E_sum += E

        if balls[i].pos_vec[1] >= height - balls[i].diameter / 2:
            balls[i].mov_vec[1] *= -1
            balls[i].pos_vec[1] -= 1
        if balls[i].pos_vec[1] <= balls[i].diameter / 2:
            balls[i].mov_vec[1] *= -1
            balls[i].pos_vec[1] += 1
        if balls[i].pos_vec[0] >= width - balls[i].diameter / 2:
            balls[i].mov_vec[0] *= -1
            balls[i].pos_vec[0] -= 1
        if balls[i].pos_vec[0] <= balls[i].diameter / 2:
            balls[i].mov_vec[0] *= -1
            balls[i].pos_vec[0] += 1

        for j in range(len(balls)):
            if i != j:

                if np.linalg.norm((balls[i].pos_vec - balls[j].pos_vec)) <= (
                        balls[i].diameter / 2 + balls[j].diameter / 2):
                    if np.linalg.norm(np.subtract(balls[i].pos_vec, balls[j].pos_vec)) != 0:
                        normal = np.subtract(balls[i].pos_vec, balls[j].pos_vec) * (
                                1 / np.linalg.norm(np.subtract(balls[i].pos_vec, balls[j].pos_vec)))
                    else:
                        normal = [0, 0]

                    vnj = np.dot(balls[j].mov_vec, normal) * normal
                    vtj = np.subtract(balls[j].mov_vec, vnj)

                    if np.linalg.norm(vtj) != 0:
                        tangent = vtj * (1 / np.linalg.norm(vtj))
                    else:
                        tangent = [0, 0]

                    vni = np.dot(balls[i].mov_vec, -normal) * (-normal)
                    vti = np.subtract(balls[i].mov_vec, vni)

                    save = vnj
                    vnj = (balls[i].mass * vni + balls[j].mass * vnj + e_coeff * balls[i].mass * (vni - vnj)) / (
                            balls[i].mass + balls[j].mass)
                    vni = (balls[i].mass * vni + balls[j].mass * save + e_coeff * balls[j].mass * (save - vni)) / (
                            balls[i].mass + balls[j].mass)

                    vi = vni + vti
                    vj = vtj + vnj

                    balls[j].mov_vec = vj
                    balls[i].mov_vec = vi
                    balls[j].pos_vec -= normal * 2
                    balls[i].pos_vec += normal * 2

                    balls[i].color = (28 * random.randint(3, 9), 28 * random.randint(3, 9), 28 * random.randint(3, 9))
                    balls[j].color = (28 * random.randint(3, 9), 28 * random.randint(3, 9), 28 * random.randint(3, 9))
    print("Total kinetik energy: " , E_sum)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()
