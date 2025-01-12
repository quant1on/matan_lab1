import main
import functions as fnc
import numpy as np
import matplotlib.pyplot as plt

def find_average_error():
    true_roots = [-3, 0, 1]
    roots = main.find_root_advanced(a=-5, b=3, f=fnc.func_deviation_test, err=10e-7)
    errors = []
    for i in range(3): errors.append(abs(true_roots[i] - roots[i]))
    mean_err = np.std(errors)
    return mean_err

def draw_plot_prediction(a: float, b: float, func):
    points = []
    with open('test.txt', 'r') as file:
        for line in file:
            x, y = map(float, line.split(','))
            points.append((x, y))

    x_points, y_points = zip(*points)

    x = np.linspace(int(a) - 1, int(b) + 2, 1000)
    y = func(x)

    plt.plot(x, y, label='y = x^2')

    plt.scatter(x_points, y_points, color='red', label='')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('')

    plt.show()

def dichotomy_pred(a: float, b: float, f, err):
    file = open("test.txt", 'w')
    epsilon = err / 2
    while (b - a) / 2 > err:
        file.write(f"{(a + b)/2}, {f((a+b)/2)} \n")
        y_k = (a + b - epsilon) / 2
        z_k = (a + b + epsilon) / 2
        if f(y_k) <= f(z_k):
            b = z_k
        else:
            a = y_k
    file.close()

def dichotomy_iteration(a: float, b: float, f, err):
    epsilon = err / 2
    count = 0
    while (b - a) / 2 > err:
        count += 1
        y_k = (a + b - epsilon) / 2
        z_k = (a + b + epsilon) / 2
        if f(y_k) <= f(z_k):
            b = z_k
        else:
            a = y_k
    return count

def draw_plot_correlation():

    points = []
    with open('test.txt', 'r') as file:
        for line in file:
            x, y = map(float, line.split(','))
            points.append((x, y))

    x_points, y_points = zip(*points)

    plt.scatter(x_points, y_points, color='blue', label='')

    # Настройка графика
    plt.xlabel('Ширина диапазона')
    plt.ylabel('Кол-во операций')
    plt.legend()
    plt.title('Plot of Correlation')

    # Показ графика
    plt.show()

if __name__ == "__main__":
    # dichotomy_pred(a=-2, b=1, f=fnc.func_plot, err=10e-7)
    # draw_plot_prediction(a=-2, b=1, func=fnc.func_plot)
    file = open("test.txt", 'w')
    for i in range(1000):
        file.write(f"{i/2 + 1}, {dichotomy_iteration(a=-0.5, b=0.5 + i/2, f=fnc.func_plot, err=10e-7)} \n")
    file.close()
    draw_plot_correlation()
