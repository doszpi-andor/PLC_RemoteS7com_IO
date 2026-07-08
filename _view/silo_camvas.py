from tkinter import Canvas, Tk


class SiloCanvas(Canvas):
    SILO_WIDTH = 100
    SILO_HEIGHT = 160
    SILO_NAME_FONT_SIZE = 12
    SILO_MOTOR_FONT_SIZE = 10

    def create_silo(self, x_position, y_position, silo_name='', silo_color='light gray', motor_name='', motor_color='gray'):
        self.create_rectangle(x_position,
                              y_position + self.SILO_HEIGHT * 1 // 10,
                              x_position + self.SILO_WIDTH,
                              y_position + self.SILO_HEIGHT * 4 // 5,
                              fill=silo_color, outline=silo_color)
        self.create_polygon(x_position,
                            y_position + self.SILO_HEIGHT * 4 // 5,
                            x_position + self.SILO_WIDTH,
                            y_position + self.SILO_HEIGHT * 4 // 5,
                            x_position + self.SILO_WIDTH * 3 // 5,
                            y_position + self.SILO_HEIGHT,
                            x_position + self.SILO_WIDTH * 2 // 5,
                            y_position + self.SILO_HEIGHT,
                            fill=silo_color, outline=silo_color)

        self.create_line(x_position,
                         y_position + self.SILO_HEIGHT * 1 // 10,
                         x_position + self.SILO_WIDTH,
                         y_position + self.SILO_HEIGHT * 1 // 10)
        self.create_line(x_position,
                         y_position + self.SILO_HEIGHT * 1 // 10,
                         x_position,
                         y_position + self.SILO_HEIGHT * 4 // 5)
        self.create_line(x_position,
                         y_position + self.SILO_HEIGHT * 4 // 5,
                         x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT)
        self.create_line(x_position + self.SILO_WIDTH,
                         y_position + self.SILO_HEIGHT * 1 // 10,
                         x_position + self.SILO_WIDTH,
                         y_position + self.SILO_HEIGHT * 4 // 5)
        self.create_line(x_position + self.SILO_WIDTH,
                         y_position + self.SILO_HEIGHT * 4 // 5,
                         x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT)

        self.create_rectangle(x_position + self.SILO_WIDTH * 1 // 5,
                              y_position,
                              x_position + self.SILO_WIDTH * 4 // 5,
                              y_position + self.SILO_HEIGHT * 1 // 10,
                              fill=motor_color)
        self.create_text(x_position + self.SILO_WIDTH * 5 // 10,
                         y_position + self.SILO_HEIGHT * 1 // 20,
                         font=("Arial", self.SILO_MOTOR_FONT_SIZE),
                         text=motor_name)

        self.create_line(x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 1 // 10,
                         x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 2 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 2 // 10,
                         x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 3 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 3 // 10,
                         x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 4 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 4 // 10,
                         x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 5 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 5 // 10,
                         x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 6 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 6 // 10,
                         x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 7 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 7 // 10,
                         x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 8 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 8 // 10,
                         x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 9 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 9 // 10,
                         x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT)
        self.create_line(x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 1 // 10,
                         x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 2 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 2 // 10,
                         x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 3 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 3 // 10,
                         x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 4 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 4 // 10,
                         x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 5 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 5 // 10,
                         x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 6 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 6 // 10,
                         x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 7 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 7 // 10,
                         x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 8 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT * 8 // 10,
                         x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 9 // 10)
        self.create_line(x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT * 9 // 10,
                         x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT)
        self.create_line(x_position + self.SILO_WIDTH * 2 // 5,
                         y_position + self.SILO_HEIGHT,
                         x_position + self.SILO_WIDTH * 3 // 5,
                         y_position + self.SILO_HEIGHT)
        # noinspection PyArgumentList
        self.create_text(x_position + self.SILO_WIDTH // 5,
                         y_position + self.SILO_HEIGHT // 2,
                         font=("Arial", self.SILO_NAME_FONT_SIZE),
                         angle=90, text=silo_name)


if __name__ == "__main__":
    root = Tk()

    silo = SiloCanvas(root)
    silo.create_silo(5, 5, silo_name='Silo 1', motor_name='M1[Q0.0]', motor_color='red')
    silo.pack()

    root.mainloop()
