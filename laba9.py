import numpy as np
import matplotlib.pyplot as plt

def plot_fourier_transform(func, a, b, x_min, x_max, num_points):
    x = np.linspace(x_min, x_max, num_points)
    y = func(x, a, b)
    
    # Применение Фурье-преобразования
    fourier_transform = np.fft.fft(y)
    frequencies = np.fft.fftfreq(num_points, d=(x_max - x_min) / num_points)
    
    # Построение графика вещественной и мнимой частей Фурье-образов
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.plot(frequencies, np.real(fourier_transform))
    ax1.set_ylabel('Real part')
    ax1.set_title('Fourier image')

    ax2.plot(frequencies, np.imag(fourier_transform))
    ax2.set_xlabel('Frequency')
    ax2.set_ylabel('Imaginary part')
    
    plt.show()

def func1(x, a, b):
    return np.exp(-(a**2)*(x**2))

def func2(x, a, b):
    return 1 / (1 + (b**2)*(x**2))

def func3(x, a, b):
    return np.sin(a*x) / (1 + b*(x**2))

# Параметры функций
a1 = 1
a2 = 2
a3 = 3
b1 = 0.5
b2 = 1
b3 = 2

# Границы построения графиков
x_min = -10
x_max = 10

# Количество точек для расчета
num_points = 1000

# Построение графиков Фурье-образов
plot_fourier_transform(func1, a1, b1, x_min, x_max, num_points)
plot_fourier_transform(func2, a2, b2, x_min, x_max, num_points)
plot_fourier_transform(func3, a3, b3, x_min, x_max, num_points)
