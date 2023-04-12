import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha=0.08
    ctrl_conv_rate = x_success / x_cnt
    test_conv_rate = y_success / y_cnt

    t_stat, p_val = ttest_ind([ctrl_conv_rate], [test_conv_rate])

    if p_val < alpha:
        return True
    else:
        return False
