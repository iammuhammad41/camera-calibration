import numpy as np
import pdb


# write your code here for part estimating fundamental matrix
def fit_fundamental(matches):
    """
    Solves for the fundamental matrix using the matches.
    """
    #matches: np array with size: (k, 4). 
    #k is the match pairs number. 
    #4 is location in each match pair:[x_axis_img1, y_axis_img1, x_axis_img2, y_axis_img2]

    #return F: fundamental matrix, np array (3,3)
    # <YOUR CODE>
    k = matches.shape[0]
    #
    x1, y1, x2, y2 = matches[:, 0], matches[:, 1], matches[:, 2], matches[:, 3]
    A = np.zeros((k, 9))
    A[:, 0], A[:, 1], A[:, 2], A[:, 3], A[:, 4], A[:, 5], A[:, 6], A[:, 7], A[:, 8] = \
        x1 * x2, x2 * y1, x2, x1 * y2, y1 * y2, y2, x1, y1, np.ones(k)
    _, _, Vh = np.linalg.svd(A)
#
    f = Vh[Vh.shape[0] - 1, :]

    F = f.reshape(3, 3)

    U, sigma, Vh = np.linalg.svd(F)

    sigma_ = np.array([[sigma[0], 0, 0], [0, sigma[1], 0], [0, 0, 0]])
    F = U.dot(sigma_.dot(Vh))


    return F


# def plot_fundamental(ax, ...):
def plot_fundamental(ax, point, F, I, flag):
    """
    function to  plot epipolar line function
    """
    # <YOUR CODE>
    k = len(point)
    #
    point = np.column_stack((point, np.ones(k))).transpose()
    # L = Fp, p'T * Fp = 0,It can be seen that the original f matrix is only suitable for drawing polar lines on Figure 2 with the points of Figure 1, which can be obtained by transposingpT * FTp'=0, L' = FTp'
    if not flag:
        F = F.transpose()
    l = F.dot(point)
    x = np.linspace(0, 1072, 1072)
    y = np.zeros((k, 1072))
    for i in range(k):
        y[i, :] = -l[0, i] / l[1, i] * x - l[2, i] / l[1, i]
        ax.plot(x, y[i, :])
    ax.imshow(np.array(I).astype(np.uint8))


    # pass