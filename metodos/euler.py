import matplotlib.pyplot as plt
from utils.parse import parse_local_t as pt


class AlgoritmoEuler:

    def __init__(self, f_x, x0, b, n):
        self.f = pt(f_x)
        self.x0 = x0
        self.b = b
        self.n = n
        self.ptos_calculados = [(0, x0)]

    def calcular(self):
        h = (self.b / self.n)
        for i in range(1, self.n + 1):
            coord_t_ant, coord_x_ant = self.ptos_calculados[i - 1]
            x_n = coord_x_ant + (h * self.f(coord_x_ant, coord_t_ant))
            self.ptos_calculados.append((i * h, x_n))
        return self.ptos_calculados[-1][1]

    def graficar(self):

        plt.close(None)
        fig, ax = plt.subplots()

        plt.xlabel('t')
        plt.ylabel('x(t)')
        plt.title('PVI - Euler')

        x_plot, y_plot = zip(*self.ptos_calculados)
        scatter = plt.scatter(x_plot, y_plot, label="puntos calculados", c="red")
        plt.plot(x_plot, y_plot, c="green")

        plt.legend(loc="best")

        annotation = ax.annotate(
            text='',
            xy=(0, 0),
            xytext=(15, 15),  # distance from x, y
            textcoords='offset points',
            bbox={'boxstyle': 'round', 'fc': 'w'},
            arrowprops={'arrowstyle': '->'}
        )
        annotation.set_visible(False)

        # Step 3. Implement the hover event to display annotations
        def motion_hover(event):
            annotation_visbility = annotation.get_visible()
            if event.inaxes == ax:
                is_contained, annotation_index = scatter.contains(event)
                if is_contained:
                    data_point_location = scatter.get_offsets()[annotation_index['ind'][0]]
                    annotation.xy = data_point_location

                    text_label = '({0:.2f}, {1:.2f})'.format(data_point_location[0], data_point_location[1])
                    annotation.set_text(text_label)

                    annotation.set_alpha(1)

                    annotation.set_visible(True)
                    fig.canvas.draw_idle()
                else:
                    if annotation_visbility:
                        annotation.set_visible(False)
                        fig.canvas.draw_idle()

        fig.canvas.mpl_connect('motion_notify_event', motion_hover)

        plt.show()

    def punto(self, t):
        if 0 <= t <= len(self.ptos_calculados):
            return self.ptos_calculados[t][1]
