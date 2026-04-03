from ..three_body import three_body
import numpy as np

def test_three_body():
    x_arr, y_arr = three_body(-1, 0, 1, 0, 0, 0, 0, 1, 0, -1, 0, 0)
    assert x_arr[2] == y_arr[2]