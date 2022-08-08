from numpy import array, diag, zeros
from scipy.linalg import svd
from PIL import Image

img = Image.open("test.png").convert('L')

while True:
    value = int(input('A: '))

    # convert image to array
    A = array(img)

    # calculate svd
    U, S, V = svd(A)

    # create m x n Sigma matrix
    Sigma = zeros((A.shape[0], A.shape[1]))

    # populate Sigma with n x n diagonal matrix
    Sigma[:A.shape[0], :A.shape[0]] = diag(S)

    # select value
    Sigma = Sigma[:, :value]
    V = V[:value, :]

    # reconstruct
    B = U.dot(Sigma.dot(V))
    
    format = Image.fromarray(B)
    
    # format.save("save.png", format="png")

    format.show()
