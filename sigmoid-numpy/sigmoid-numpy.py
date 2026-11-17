import numpy as np 
def sigmoid(x: list | float) -> np.ndarray | float:
    arr = np.array(x,dtype=float)
    res = 1/(1+np.exp(-arr))
    if np.isscalar(x):
        res=float(res)

    return res
        