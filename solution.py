import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 573772382 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    
    return -loc / norm.ppf(1 - alpha / 2)/50, \
           -loc / norm.ppf(alpha / 2)/50

