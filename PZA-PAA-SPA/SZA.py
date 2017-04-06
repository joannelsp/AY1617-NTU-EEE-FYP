import numpy as np
import cv2
import datetime
import ephem

def cam2world(m, imager):
        
    if imager == 'wahrsis1' or imager == 'wahrsis3':
        c0 = 1724
        c1 = 2592
        rad = 1470
    elif imager == 'wahrsis4':
        c0 = 2000
        c1 = 2975
        rad = 1665

    m1 = m[0,:] - c0
    m2 = m[1,:] - c1
    azimuth = np.arctan2(m2, m1)

    r = np.sqrt(np.power(m1,2) + np.power(m2,2))
    theta = np.pi/2 - 2*np.arcsin(r/(rad/np.sin(np.pi/4)))

    M1 = m1
    M2 = m2
    M3 = r*np.tan(-theta)
    norm = np.sqrt(np.power(M1, 2) + np.power(M2, 2) + np.power(M3, 2))

    return [azimuth, theta, np.column_stack((M1/norm, M2/norm, M3/norm)).T]


def rotation_matrix(a,b):
    
    x = np.array([[a[1]*b[2] - b[1]*a[2]], [a[2]*b[0] - b[2]*a[0]], [a[0]*b[1] - b[0]*a[1]]])
    x = x/np.linalg.norm(x);
    theta = np.arccos(np.dot(a.T, b)/(np.linalg.norm(a) * np.linalg.norm(b)))
    A = np.array([[0, -x[2], x[1]], [x[2], 0, -x[0]], [-x[1], x[0], 0]])
    R = np.eye(3) + np.sin(theta) * A + (1 - np.cos(theta)) * np.power(A,2)
    
    return R


def computeSZA(dt, imager):
    
    if imager == 'wahrsis3':
        size_img = np.array([5184, 3456])
    elif imager == 'wahrsis4':
        size_img = np.array([6000, 4000])
        
    coords = [1.343237, 103.680448]
    
    img_coords = np.meshgrid(np.arange(size_img[0]), np.arange(size_img[1]))
    coordsImg = np.column_stack([img_coords[1].flatten(), img_coords[0].flatten()]).T
    [coordsAz, coordsElev, cartesian] = cam2world(coordsImg, imager)
    
    elevationsZenith = np.pi/2 - coordsElev.reshape([size_img[1], size_img[0]])
    d = dt - datetime.timedelta(hours = 8) # To UTC
    
    obs = ephem.Observer()
    obs.lon = '103:40:49.9'
    obs.lat = '1:20:35'
    obs.elevation = 0
    obs.date = d

    sun = ephem.Sun(obs)
    sunElev = np.pi/2 - float(sun.alt)
    sunAz = float(sun.az) + np.pi

    
    P = np.array([0,0,1])
    Q = np.array([np.cos(sunAz)*np.sin(sunElev), np.sin(sunAz)*np.sin(sunElev), np.cos(sunElev)])
    M = rotation_matrix(P,Q)
    w = np.dot(cartesian.T, M)

    r = np.sqrt(np.power(w[:,0], 2) + np.power(w[:,1], 2) + np.power(w[:,2], 2))
    thetas = np.arccos(w[:,2]/r)

    elevationsSun = np.pi/2 - (thetas.reshape([size_img[1], size_img[0]]) - np.pi/2)
    elevationsSun[elevationsZenith > np.pi/2] = np.nan
    
    return elevationsSun
    
    
