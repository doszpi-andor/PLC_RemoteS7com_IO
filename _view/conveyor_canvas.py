from math import tan, atan, atan2, degrees
from tkinter import Canvas, Tk, CENTER


class ConveyorCanvas(Canvas):
    CONVEYOR_WIDTH = 50
    CONVEYOR_NAME_FONT_SIZE = 12
    CONVEYOR_CIRCLE_FONT_SIZE = 10

    def create_conveyor(self, x_position, y_position, length, name='', conveyor_color='light gray', name_color='black',
                        circle1_name='', circle1_color='gray', circle2_name='', circle2_color='gray'):

        self.create_rectangle(x_position + self.CONVEYOR_WIDTH // 2,
                              y_position,
                              x_position + length - self.CONVEYOR_WIDTH // 2,
                              y_position + self.CONVEYOR_WIDTH,
                              fill=conveyor_color)

        text_id = self.create_text(x_position + length // 2,
                                   y_position + self.CONVEYOR_WIDTH // 2,
                                   font=("Arial", self.CONVEYOR_NAME_FONT_SIZE),
                                   text=name, fill=name_color)
        self.create_oval(x_position,
                         y_position,
                         x_position + self.CONVEYOR_WIDTH,
                         y_position + self.CONVEYOR_WIDTH,
                         fill=circle1_color)
        self.create_text(x_position + self.CONVEYOR_WIDTH // 2,
                         y_position + self.CONVEYOR_WIDTH // 2,
                         font=("Arial", self.CONVEYOR_CIRCLE_FONT_SIZE),
                         justify=CENTER, text=circle1_name)
        self.create_oval(x_position + length - self.CONVEYOR_WIDTH,
                         y_position,
                         x_position + length,
                         y_position + self.CONVEYOR_WIDTH,
                         fill=circle2_color)
        self.create_text(x_position + length - self.CONVEYOR_WIDTH // 2,
                         y_position + self.CONVEYOR_WIDTH // 2,
                         font=("Arial", self.CONVEYOR_CIRCLE_FONT_SIZE),
                         justify=CENTER, text=circle2_name)

        return text_id


class ScrewCanvas(Canvas):
    SCREW_WIDTH = 30
    SCREW_NAME_FONT_SIZE = 12
    SCREW_ELEMENT_FONT_SIZE = 10

    def create_screw(self, x_lower_position, y_lower_position, x_upper_position, y_upper_position,
                     name='', name_color='black', screw_color='light gray',
                     lower_mane='', lower_color='gray', upper_name='', upper_color='gray'):

        self.create_rectangle(x_lower_position,
                              y_lower_position,
                              x_lower_position + self.SCREW_WIDTH,
                              y_lower_position + self.SCREW_WIDTH,
                              fill=lower_color)
        self.create_text(x_lower_position + self.SCREW_WIDTH // 2,
                         y_lower_position + self.SCREW_WIDTH // 2,
                         font=("Arial", self.SCREW_ELEMENT_FONT_SIZE),
                         justify=CENTER, text=lower_mane)

        self.create_rectangle(x_upper_position,
                              y_upper_position,
                              x_upper_position + self.SCREW_WIDTH,
                              y_upper_position + self.SCREW_WIDTH,
                              fill=upper_color)
        self.create_text(x_upper_position + self.SCREW_WIDTH // 2,
                         y_upper_position + self.SCREW_WIDTH // 2,
                         font=("Arial", self.SCREW_ELEMENT_FONT_SIZE),
                         justify=CENTER, text=upper_name)

        if x_lower_position < x_upper_position:
            name_degrees = degrees(
                atan2((y_lower_position - y_upper_position), (x_upper_position - x_lower_position - self.SCREW_WIDTH))
            )
            self.create_polygon(x_lower_position + self.SCREW_WIDTH,
                                y_lower_position,
                                x_upper_position,
                                y_upper_position,
                                x_upper_position,
                                y_upper_position + self.SCREW_WIDTH,
                                x_lower_position + self.SCREW_WIDTH,
                                y_lower_position + self.SCREW_WIDTH,
                                fill=screw_color, outline='black')

        else:
            name_degrees = degrees(
                atan2((y_lower_position - y_upper_position), (x_upper_position - x_lower_position + self.SCREW_WIDTH))
            ) - 180
            self.create_polygon(x_lower_position,
                                y_lower_position,
                                x_upper_position + self.SCREW_WIDTH,
                                y_upper_position,
                                x_upper_position + self.SCREW_WIDTH,
                                y_upper_position + self.SCREW_WIDTH,
                                x_lower_position,
                                y_lower_position + self.SCREW_WIDTH,
                                fill=screw_color, outline='black')

        # noinspection PyArgumentList
        text_id = self.create_text(x_lower_position + (x_upper_position - x_lower_position) // 2 + self.SCREW_WIDTH // 2,
                                   y_lower_position + (y_upper_position - y_lower_position) // 2 + self.SCREW_WIDTH // 2,
                                   font=("Arial", self.SCREW_NAME_FONT_SIZE),
                                   angle=name_degrees, text=name, fill=name_color)

        return text_id


if __name__ == "__main__":
    root = Tk()

    # silo = ConveyorCanvas(root)
    # noinspection SpellCheckingInspection
    # silo.create_conveyor(5, 5, length=300, name='Szalag 1', circle1_name='M1\n[Q0.0]', circle2_name='S1\n[I0.0]')
    # silo.pack()

    screw1 = ScrewCanvas(root)
    screw1.create_screw(x_lower_position=5, y_lower_position=105, x_upper_position=155, y_upper_position=5,
                        name='Csiga 1', lower_mane='M1', upper_name='S1')
    screw2 = ScrewCanvas(root)
    screw2.create_screw(x_lower_position=155, y_lower_position=105, x_upper_position=5, y_upper_position=5,
                        name='Csiga 2', lower_mane='M2', upper_name='S2')
    screw1.pack()
    screw2.pack()

    root.mainloop()
