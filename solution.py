import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha=0.08
    control_conv = x_success / x_cnt
    test_conv = y_success / y_cnt
    t_stat, p_value = ttest_ind(control_conv, test_conv, equal_var=False)
    return p_value < alpha
