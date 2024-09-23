import matplotlib.pyplot as plt
import numpy as np

def plot_polygon_with_arrows():
    # Кількість вершин
    num_sides = 16
    # Кут між вершинами
    theta = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
    # Координати вершин
    x = np.cos(theta)
    y = np.sin(theta)

    # Додавання фігури на графік
    fig, ax = plt.subplots()
    ax.fill(x, y, color='lightblue', alpha=0.5)  # Заповнена кольором фігура

    # Додавання стрілок на контурі
    for i in range(num_sides):
        ax.quiver(x[i], y[i], x[(i + 1) % num_sides] - x[i], y[(i + 1) % num_sides] - y[i],
                   angles='xy', scale_units='xy', scale=1, color='orange', linewidth=1.5)

    # Додавання тексту в центрі
    ax.text(0, 0, '16-багатокутник', horizontalalignment='center',
            verticalalignment='center', fontsize=12, color='black', fontweight='bold')

    # Налаштування графіку
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')  # Вимкнення осей
    ax.set_title('16-багатокутник з контуром та текстом')

    # Показати графік
    plt.show()

# Виклик функції для малювання 16-багатокутника
plot_polygon_with_arrows()
