import matplotlib.pyplot as plt
import numpy as np

orbitSize = 7000

def sphere(ax):
    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = 9.5 * np.outer(np.cos(u), np.sin(v))
    y = 9.5 * np.outer(np.sin(u), np.sin(v))
    z = 9.5 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z)

def plotData(data,plotSphere,windowName,topLabel):
    fig = plt.figure(windowName)
    ax = fig.add_subplot(111, projection='3d')
    plt.title(topLabel)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])
    if plotSphere:
        sphere(ax)
    numSC = int(np.size(data, 1) / 5)
    xs = []
    ys = []
    zs = []
    for entry in range(0,np.size(data,0)):
        for lowerSC in range(0,int(numSC/2)):
            for upperSC in range(0,int(numSC/2)):
                if abs((data[entry,lowerSC*5])-(data[entry,((numSC*5)-(5*((int(numSC/2))-upperSC)))])) <= 0.5  and abs((data[entry,(1+(5*lowerSC))])-(data[entry,(((numSC*5)-(5*((int(numSC/2))-upperSC)))+1)])) <= 0.5:
                    xs.append(10*(data[entry,(lowerSC*5)+2]/orbitSize))
                    ys.append(10*(data[entry,(lowerSC*5)+3]/orbitSize))
                    zs.append(10*(data[entry,(lowerSC*5)+4]/orbitSize))
    ax.scatter(xs, ys, zs, c='red')

data = np.loadtxt('Polar8SatResults.txt',skiprows=1,dtype=float)
plotData(data,True,'8 Satellite Polar Orbits','Points of head-on passage for 8 satellites')

data = np.loadtxt('Polar6SatResults.txt',skiprows=1,dtype=float)
plotData(data,True,'6 Satellite Polar Orbits','Points of head-on passage for 6 satellites')

data = np.loadtxt('Polar4SatResults.txt',skiprows=1,dtype=float)
plotData(data,True,'4 Satellite Polar Orbits','Points of head-on passage for 4 satellites')

data = np.loadtxt('Polar2SatResults.txt',skiprows=1,dtype=float)
plotData(data,True,'2 Satellite Polar Orbits','Points of head-on passage for 2 satellites')

plt.show()