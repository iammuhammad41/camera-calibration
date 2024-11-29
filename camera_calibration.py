import numpy as np


# Write your code here for camera calibration (lab)
# def camera_calibration(pt_3d, matches):
def camera_calibration(pt_3d, pt_2d):
    """
    write your code to compute camera matrix
    """
    #pt_3d: points location in 3d, np array with size: k x 3. [x,y,z].
    #k is the 3d points number.
    #3: 3 dimension: [x,y,z]

    #matches: np array with size: (k,4). 
    #k is the match pairs number. 
    #4 is location in each match pair:[x_axis_img1, y_axis_img1, x_axis_img2, y_axis_img2]

    #return P: project matrix: np array (3,4)
    #return K: fundamental matrix, np array (3,3)
    #return R: rotation matrix, np array (3,3)
    #return c: camera center, np array (4,)

    
    # <YOUR CODE>
    k = len(pt_3d)
    P = np.zeros((k * 2, 12))
    x, y, z = pt_3d[:, 0], pt_3d[:, 1], pt_3d[:, 2]
    u, v = pt_2d[:, 0], pt_2d[:, 1]
    #
    for i in range(k):
        P[2 * i, :] = x[i], y[i], z[i], 1, 0, 0, 0, 0, -u[i] * x[i], -u[i] * y[i], -u[i] * z[i], -u[i]
        P[2 * i + 1, :] = 0, 0, 0, 0, x[i], y[i], z[i], 1, -v[i] * x[i], -v[i] * y[i], -v[i] * z[i], -v[i]
#
    _, _, Vh = np.linalg.svd(P)
    P = Vh[Vh.shape[0]-1, :].reshape(3, 4)

    _, _, Vh = np.linalg.svd(P)
    c = Vh[Vh.shape[0] - 1, :]

    M = P[:, 0:3]
    K, R = np.linalg.qr(M)

    return P, K, R, c
