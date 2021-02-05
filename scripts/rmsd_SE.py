#!/usr/bin/env python3.8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import scipy.stats
import math
import string
import sys
import argparse
############################################################
parser = argparse.ArgumentParser(
    description='Plot Average RMSD with Std. Error!')
parser.add_argument("-x",
                    "--x",
                    type=int,
                    required=False,
                    default=0,
                    help="This is the 'xmin' variable : default = %(default)s")
parser.add_argument("-X",
                    "--X",
                    type=int,
                    required=True,
                    default=25,
                    help="This is the 'xmax' variable : default = %(default)s")
parser.add_argument("-y",
                    "--y",
                    type=int,
                    required=False,
                    default=0,
                    help="This is the 'ymin' variable : default = %(default)s")
parser.add_argument("-Y",
                    "--Y",
                    type=int,
                    required=True,
                    default=10,
                    help="This is the 'Ymax' variable : default = %(default)s")
parser.add_argument(
    "-f1",
    "--f1",
    required=True,
    help="Input RMSD data file name for multiple trajectory data.")
parser.add_argument("-t", "--t", required=True, help="Graph Title")
parser.add_argument("-o",
                    "--o",
                    required=True,
                    help="Name of output file name (output.png)")
args = parser.parse_args()
############################################################
inp_nameGlob = args.f1
inp_data = np.loadtxt(inp_nameGlob, comments=['#', '@', '&'])[0:]

time = inp_data[:, 0]
trajOne = inp_data[:, 1] * 10
trajTwo = inp_data[:, 3] * 10
trajThree = inp_data[:, 5] * 10
trajFour = inp_data[:, 7] * 10
trajFive = inp_data[:, 9] * 10

globAvg = (trajOne + trajTwo + trajThree + trajFour + trajFive) / 5

def movingaverage(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')

############### Global setting ##############
SMALL_SIZE = 8
MEDIUM_SIZE = 8
#BIGGER_SIZE = 5
FONT_WEIGHT = "bold"
plt.rc('font', size=SMALL_SIZE,
       weight=FONT_WEIGHT)  # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE,
       labelweight=FONT_WEIGHT)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
plt.rcParams['figure.figsize'] = [7, 4.0]  #Figure size
###############################################
xmin = args.x
xmax = args.X
ymin = args.y
ymax = args.Y

xinterval = 10
yinterval = 1

plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
alpha1 = 1.0
alpha2 = 1.0
alpha3 = 0.2
x_ticks = np.arange(xmin, xmax + 1, xinterval)
y_ticks = np.arange(ymin, ymax + 1, yinterval)
plt.title(args.t, fontsize=10, weight=900)
plt.xlabel('time(ns)')
plt.ylabel('RMSD (\305)')
plt.xticks(x_ticks)
plt.yticks(y_ticks)

time_av = movingaverage(time, 10)
y_av = movingaverage(trajOne, 10)
plt.plot(time_av[0:-4],
         y_av[:-4],
         label="Traj1",
         color="purple",
         linewidth=2,
         alpha=alpha2)

y_av = movingaverage(trajTwo, 10)
plt.plot(time_av[0:-4],
         y_av[:-4],
         label="Traj2",
         color="magenta",
         linewidth=2,
         alpha=alpha2)

y_av = movingaverage(trajThree, 10)
plt.plot(time_av[0:-4],
         y_av[:-4],
         label="Traj3",
         color="blue",
         linewidth=2,
         alpha=alpha2)

y_av = movingaverage(trajFour, 10)
plt.plot(time_av[0:-4],
         y_av[:-4],
         label="Traj4",
         color="green",
         linewidth=2,
         alpha=alpha2)

y_av = movingaverage(trajFive, 10)
plt.plot(time_av[0:-4],
         y_av[:-4],
         label="Traj5",
         color="orange",
         linewidth=2,
         alpha=alpha2)

rmsd_std = np.std([trajOne, trajTwo, trajThree, trajFour, trajFive], axis=0)
rmsd_err = rmsd_std / np.sqrt(5)
print(rmsd_err)
rmsd_err_av = movingaverage(rmsd_err, 10)
y_av = movingaverage(globAvg, 10)
plt.errorbar(time_av[0:-4],
             y_av[:-4],
             rmsd_err_av[:-4],
             linewidth=1.0,
             color="r",
             label="RMSD-SE",
             alpha=alpha3)

plt.plot(time_av[0:-4],
         y_av[:-4],
         label="Avg",
         color="k",
         linewidth=2,
         alpha=alpha1)

plt.legend(frameon=False, loc=0)
plt.savefig(args.o)
