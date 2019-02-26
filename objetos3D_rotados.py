# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:03:16 2019
based in https://stackoverflow.com/questions/44881885/python-draw-3d-cube
@author: Ariel Paz
"""

import numpy as np
import matplotlib.pyplot as plt
import math
#from mpl_toolkits.mplot3d import Axes3D
#from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def plot_cube(cube_definition):
    cube_definition_array = [
        np.array(list(item))
        for item in cube_definition
    ]

    points = []
    points += cube_definition_array
    vectors = [
        cube_definition_array[1] - cube_definition_array[0],
        cube_definition_array[2] - cube_definition_array[0],
        cube_definition_array[3] - cube_definition_array[0]
    ]

    points += [cube_definition_array[0] + vectors[0] + vectors[1]]
    points += [cube_definition_array[0] + vectors[0] + vectors[2]]
    points += [cube_definition_array[0] + vectors[1] + vectors[2]]
    points += [cube_definition_array[0] + vectors[0] + vectors[1] + vectors[2]]

    points = np.array(points)

    edges = [
        [points[0], points[3], points[5], points[1]],
        [points[1], points[5], points[7], points[4]],
        [points[4], points[2], points[6], points[7]],
        [points[2], points[6], points[3], points[0]],
        [points[0], points[2], points[4], points[1]],
        [points[3], points[6], points[7], points[5]]
    ]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    faces = Poly3DCollection(edges, linewidths=1, edgecolors='k')
    faces.set_facecolor((0,0,1,0.1))

    ax.add_collection3d(faces)

    # Plot the points themselves to force the scaling of the axes
    ax.scatter(points[:,0], points[:,1], points[:,2], s=0)

    #ax.set_aspect('equal')


def rotateX(objeto3D, angle):
    """ Rotates the point around the X axis by the given angle in degrees. """
    objeto_rotado = []
    
    rad = angle * math.pi / 180    
    cosa = math.cos(rad)
    sina = math.sin(rad)
    
    for i in cube_definition:  
        x, y, z = i
        puntoX = x
        puntoY = y   * cosa - z * sina
        puntoZ = y * sina + z * cosa         
        objeto_rotado.append((puntoX, puntoY, puntoZ))
    return objeto_rotado

def rotateY(objeto3D, angle):
    """ Rotates the point around the X axis by the given angle in degrees. """
    objeto_rotado = []
    
    rad = angle * math.pi / 180    
    cosa = math.cos(rad)
    sina = math.sin(rad)
    
    for i in cube_definition:        
        x, y, z = i
        puntoY = y
        puntoZ = z * cosa - x * sina
        puntoX = z * sina + x * cosa         
        objeto_rotado.append((puntoX, puntoY, puntoZ))
    return objeto_rotado        

def rotateZ(objeto3D, angle):
    """ Rotates the point around the X axis by the given angle in degrees. """
    objeto_rotado = []
    
    rad = angle * math.pi / 180    
    cosa = math.cos(rad)
    sina = math.sin(rad)
    
    for i in cube_definition:        
        x, y, z = i
        puntoZ = z
        puntoY = x * cosa - y * sina
        puntoX = x * sina + y * cosa         
        objeto_rotado.append((puntoX, puntoY, puntoZ))
    return objeto_rotado        

#fin definicion de funciones 
    
#definicion del cubo, deben ser 8 puntos, pero se hace la proyeccion
cube_definition = [(0,0,0), (0,14.8,0), (0,0,6), (7.15,0,0)]

rotateX(cube_definition, -90)

plot_cube(cube_definition)    
plot_cube(rotateX(cube_definition, 45))
plot_cube(rotateZ(cube_definition, 45))
plot_cube(rotateY(cube_definition, -15))    

plot_cube(rotateX(cube_definition, 90))    

 

 
