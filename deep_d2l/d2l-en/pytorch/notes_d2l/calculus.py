"""
Derivatives - Rate of change in a fctn w.r.t changes in its arguments
    - Tell us how rapidly a loss function would increase or decrease each parameters
      by an infinitesimally small amount

"""
# u = f(x) = 10x^3 - 4x^2 + 3x + 1

#%%
import numpy as np
# from scipy.misc import derivative
import matplotlib.pyplot as plt
import torch

def f(x):
    return x**3 - (1/x)
"""
def f_2(x):
    return 10 * x **3 - 4 * x **2 + 3 * x + 1

def deriv(x):
    return derivative (f, x)
#def use_svg_display(): #@save 
    # Use the svg format to display a plot in Jupyter.
    # backend_inline.set_matplotlib_formats('svg')

def set_figsize(figsize=(3.5, 2.5)): 
    # Set the fiture size for matplot.
    use_svg_display()
    d2l.plt.rcParams['figure.figsize'] = figsize


def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):
    # Set the axes for matplotlib.
    axes.set_xlabel(xlabel), axes.set_ylabel(ylabel)
    axes.set_xscale(xscale), axes.set_yscale(yscale)
    axes.set_xlim(xlim),     axes.set_ylim(ylim)
    if legend:
        axes.legend(legend)
    axes.grid()

"""
# x-axis intervals
y = [1,3,2,4,5,6,2]
x = [1,2,3,4,5,6,7]
# Plotting the function
plt.plot(x, y)

# Plotting its derivative
#plt.plot(y, deriv(y), color="blue", label="Derivative")

# Formatting
#plt.legend(loc='upper left')
plt.grid(True)
plt.savefig
plt.show()
"""
    def plot(X, Y=None, xlabel=None, ylabel=None, legend=[], xlim=None,
            ylim=None, xscale='linear', yscale='linear',
            fmts=('-', 'm--', 'g-.', 'r:'), figsize=(3.5, 2.5), axes=None):
        Plot data points
        
        def has_one_axis
# for h in 10.0**np.arange(-1, -6, -1):
#   print(f'h={h:.5f}, numerical limit={(f(1+h)-f(1))/h:.5f}')
"""
