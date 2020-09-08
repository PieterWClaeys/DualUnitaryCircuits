import matplotlib.pyplot as plt

#Aesthetics
fig_size =  [10, 6]
params = {'backend': 'ps',
      'axes.labelsize': 14,
      'font.size': 14,
      'legend.fontsize': 13,
      'axes.titlesize' : 12,
      'xtick.labelsize': 12,
      'ytick.labelsize': 12,
      'xtick.direction': 'in',
      'ytick.direction': 'in',
      'xtick.top' : True,
      'ytick.right' : True,
      'legend.frameon' : False,
      'axes.linewidth' : 1.,
      'axes.linewidth' : 1.,
      'lines.linewidth' : 1.5,
      'text.usetex': True,
      'figure.figsize': fig_size}
plt.rcParams.update(params)
