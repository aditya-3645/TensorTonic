import numpy as np

def relu(x) -> np.ndarray:
    arr=np.array(x, dtype=float)
    res=np.maximum(0,x)

    # if np.isscalar(x):
    #     res=float(res)
    return res