import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p_control = x_success / x_cnt
    p_test = y_success / y_cnt

    expected = [p_control * y_cnt, (1 - p_control) * y_cnt,
    p_test * y_cnt, (1 - p_test) * y_cnt]

    observed = [x_success, x_cnt - x_success,
    y_success, y_cnt - y_success]

    chi2, p_value = stats.chisquare(observed, expected)

    return p_value < 0.08
