import pandas as pd
import numpy as np


chat_id = 690310158 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    import numpy as np
    from scipy.optimize import minimize
    
    def objective(a: float, x: np.array) -> float:
        t = 21
        s_estimated = a * (t**2) / 2
        return np.sum(np.abs(s_estimated - x))
    
    result = minimize(objective, 0, args=(x), method="L-BFGS-B")
    return result.x[0]
