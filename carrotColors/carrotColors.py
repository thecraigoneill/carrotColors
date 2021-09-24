import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class CarrotColors():
  def rgb_to_dec(value):
    return [v/256 for v in value]

  def get_carrots():
    carrots = [(45,22,60),(50,29,62),(67,13,40),(85,17,45),(189,0,50),(204,4,57),(227,79,0),(238,91,0),(224,180,0),(223,166,16),(222,202,63),(224,224,126)]
    rgb_list = carrots
    float_list = list(np.linspace(0,1,len(rgb_list)))
    cdict = dict()
    for num, col in enumerate(['red', 'green', 'blue']):
        col_list = [[float_list[i], rgb_list[i][num]/256, rgb_list[i][num]/256] for i in range(len(float_list))]
        cdict[col] = col_list
    my_cmp = mcolors.LinearSegmentedColormap('my_cmp', segmentdata=cdict, N=256)
    return(my_cmp)
