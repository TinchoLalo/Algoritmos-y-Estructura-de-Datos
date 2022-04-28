import matplotlib.pyplot as plt
import numpy as np


# vector de variable independiene
x = np.linspace(-4,4,500)

# vector a graficar
y=x*np.exp(-x)/(1-x**2)

# comando para graficar
plt.plot(x,y)


