from tkinter import Canvas, Tk, W, RIGHT


class IndicatorCanvas(Canvas):
    INDICATOR_WIDTH = 20
    INDICATOR_TEXT_SHIFT = 5
    INDICATOR_FONT_SIZE = 10

    def create_square_indicator(self, x_position, y_position, name='', color='gray', name_x_shift=INDICATOR_TEXT_SHIFT):

        self.create_rectangle(x_position,
                              y_position,
                              x_position + self.INDICATOR_WIDTH,
                              y_position + self.INDICATOR_WIDTH,
                              fill=color)
        self.create_text(x_position + self.INDICATOR_WIDTH + name_x_shift,
                         y_position + self.INDICATOR_WIDTH // 2,
                         font=("Arial", self.INDICATOR_FONT_SIZE),
                         anchor=W, text=name)

    def create_circle_indicator(self, x_position, y_position, name='', color='gray', name_x_shift=INDICATOR_TEXT_SHIFT):

        self.create_oval(x_position,
                         y_position,
                         x_position + self.INDICATOR_WIDTH,
                         y_position + self.INDICATOR_WIDTH,
                         fill=color)
        self.create_text(x_position + self.INDICATOR_WIDTH + name_x_shift,
                         y_position + self.INDICATOR_WIDTH // 2,
                         font=("Arial", self.INDICATOR_FONT_SIZE),
                         anchor=W, text=name)

    def create_delta_indicator(self, x_position, y_position, name='', direction='right', color='gray'):
        if direction == 'right':
            name_text = self.create_text(x_position,
                                         y_position + self.INDICATOR_WIDTH // 2,
                                         font=("Arial", self.INDICATOR_FONT_SIZE),
                                         justify=RIGHT,
                                         anchor=W, text=name)
            text_x_end = self.bbox(name_text)[2]
            self.create_polygon(text_x_end + self.INDICATOR_TEXT_SHIFT,
                                y_position,
                                text_x_end + self.INDICATOR_TEXT_SHIFT,
                                y_position + self.INDICATOR_WIDTH,
                                text_x_end + self.INDICATOR_TEXT_SHIFT + self.INDICATOR_WIDTH,
                                y_position + self.INDICATOR_WIDTH // 2,
                                fill=color, outline='black')
        elif direction == 'left':
            self.create_polygon(x_position + self.INDICATOR_WIDTH,
                                y_position,
                                x_position + self.INDICATOR_WIDTH,
                                y_position + self.INDICATOR_WIDTH,
                                x_position,
                                y_position + self.INDICATOR_WIDTH // 2,
                                fill=color, outline='black')
            self.create_text(x_position + self.INDICATOR_WIDTH + self.INDICATOR_TEXT_SHIFT,
                             y_position + self.INDICATOR_WIDTH // 2,
                             font=("Arial", self.INDICATOR_FONT_SIZE),
                             anchor=W, text=name)
        elif direction == 'up':
            self.create_polygon(x_position + self.INDICATOR_WIDTH // 2,
                                y_position,
                                x_position,
                                y_position + self.INDICATOR_WIDTH,
                                x_position + self.INDICATOR_WIDTH,
                                y_position + self.INDICATOR_WIDTH,
                                fill=color, outline='black')
            self.create_text(x_position + self.INDICATOR_WIDTH + self.INDICATOR_TEXT_SHIFT,
                             y_position + self.INDICATOR_WIDTH // 2,
                             font=("Arial", self.INDICATOR_FONT_SIZE),
                             anchor=W, text=name)
        elif direction == 'down':
            self.create_polygon(x_position,
                                y_position,
                                x_position + self.INDICATOR_WIDTH,
                                y_position,
                                x_position + self.INDICATOR_WIDTH // 2,
                                y_position + self.INDICATOR_WIDTH,
                                fill=color, outline='black')
            self.create_text(x_position + self.INDICATOR_WIDTH + self.INDICATOR_TEXT_SHIFT,
                             y_position + self.INDICATOR_WIDTH // 2,
                             font=("Arial", self.INDICATOR_FONT_SIZE),
                             anchor=W, text=name)


if __name__ == "__main__":
    root = Tk()

    indicators = IndicatorCanvas(root)
    indicators.create_square_indicator(55, 5, name='Start', color='green')
    indicators.create_circle_indicator(55, 30, name='Error', color='red', name_x_shift=-55)
    indicators.create_delta_indicator(55, 60, direction='left')
    indicators.create_delta_indicator(80, 60, direction='right')
    indicators.pack()

    root.mainloop()
