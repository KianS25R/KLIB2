"""part of klib2 script for weather formulars and simulation"""
from vector import *
from kmath import *
import agurk as pickle




def d_dx(F, i, j, dx):
    return (F[i+1][j] - F[i-1][j]) / (2 * dx)


def d_dy(F, i, j, dx):
    return (F[i][j+1] - F[i][j-1]) / (2 * dx)


def laplacian(F, i, j, dx):
    return (
        F[i+1][j] + F[i-1][j] +
        F[i][j+1] + F[i][j-1] -
        4 * F[i][j]
    ) / (dx * dx)


class simulate():
    def __init__(self, sizex=64, sizey=64):
        super().__init__()
        self.cells = []
        self.sx = sizex
        self.sy = sizey
        self.dx = 1000.0
        self.dt = 1.0
        self.T = [[280.0 for _ in range(self.sy)] for _ in range(self.sx)]
        self.H = [[0.5 for _ in range(self.sy)] for _ in range(self.sx)]
        self.u = [[0.0 for _ in range(self.sy)] for _ in range(self.sx)]
        self.v = [[0.0 for _ in range(self.sy)] for _ in range(self.sx)]
        self.k_T = 10.0
        self.k_H = 10.0
        self.a_P = 2.0
        self.alpha = 1 * (10**(-4))
        self.Running = False


    def run(self):
        self.Running = True
        self.runa()


    def runa(self):
        self.P = [[self.a_P * self.T[i][j] for j in range(self.sy)] for i in range(self.sx)]
        new_u = [[0.0 for _ in range(self.sy)] for _ in range(self.sx)]
        new_v = [[0.0 for _ in range(self.sy)] for _ in range(self.sx)]
        new_T = [[0.0 for _ in range(self.sy)] for _ in range(self.sx)]
        new_H = [[0.0 for _ in range(self.sy)] for _ in range(self.sx)]

        for i in range(1, self.sx-1):
            for j in range(1, self.sy-1):
                dPdx = d_dx(self.P, i, j, self.dx)
                dPdy = d_dy(self.P, i, j, self.dx)

                new_u[i][j] = self.u[i][j] - self.alpha * dPdx * self.dt
                new_v[i][j] = self.v[i][j] - self.alpha * dPdy * self.dt
                dTdx = d_dx(self.T, i, j, self.dx)
                dTdy = d_dy(self.T, i, j, self.dx)
                lapT = laplacian(self.T, i, j, self.dx)


                new_T[i][j] = (self.T[i][j] - self.u[i][j] * dTdx * self.dt - self.v[i][j] * dTdy * self.dt + self.k_T * lapT * self.dt)

                dHdx = d_dx(self.H, i, j, self.dx)
                dHdy = d_dy(self.H, i, j, self.dx)
                lapH = laplacian(self.H, i, j, self.dx)

                new_H[i][j] = (
                    self.H[i][j]
                    - self.u[i][j] * dHdx * self.dt
                    - self.v[i][j] * dHdy * self.dt
                    + self.k_H * lapH * self.dt
                )

        self.u, self.v = new_u, new_v
        self.T, self.H = new_T, new_H
        lista = []
        for x in range(self.sx):
            for y in range(self.sy):
                cell_temp = self.T[x][y]
                cell_hum = self.H[x][y]
                cell_u = self.u[x][y]
                cell_v = self.v[x][y]

                lista.append([cell_temp, cell_hum, cell_u, cell_v])
        pickle.write(*lista, file="save.txt")
                
        print("steppa donna")
        if self.Running == True:
            self.runa()

    def stop(self):
        self.Running = False