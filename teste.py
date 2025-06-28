from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        self.results = ""

        # Main layout
        main_layout = BoxLayout(orientation='vertical')

        # Top frame (for image and title)
        top_frame = BoxLayout(orientation='vertical', size_hint=(1, 0.2))

        # Image (not implemented in this example)
        # You can add an Image widget here if needed

        # Title label
        title_label = Label(text="pyCalculator",
                            font_name='Montserrat',
                            font_size=80,
                            color=(1, 1, 1, 1),
                            size_hint=(1, None),
                            height=90,
                            valign='middle',
                            halign='center')
        top_frame.add_widget(title_label)

        main_layout.add_widget(top_frame)

        # Middle frame (for entry and buttons)
        middle_frame = BoxLayout(orientation='vertical', size_hint=(1, 0.6))

        # Entry
        self.entry = TextInput(text="",
                               font_name='Montserrat',
                               font_size=80,
                               readonly=True,
                               multiline=False,
                               background_color=(1, 1, 1, 1),
                               cursor_color=(0, 0, 0, 1),
                               cursor_width=2,
                               cursor_blink=True,
                               foreground_color=(0, 0, 0, 1),
                               height=150,
                               size_hint=(1, None),
                               valign='middle',
                               halign='right')
        middle_frame.add_widget(self.entry)

        main_layout.add_widget(middle_frame)

        # Bottom frame (for buttons)
        bottom_frame = BoxLayout(orientation='horizontal', size_hint=(1, 0.8))

        # Button grid layout
        button_grid = BoxLayout(orientation='vertical', spacing=5)

        # Row 1: AC, Del, ÷
        row1 = BoxLayout(spacing=5)
        ac_button = Button(text='AC',
                           font_name='Montserrat',
                           font_size=20,
                           size_hint=(None, None),
                           width=93.75,
                           height=68,
                           background_color=(0.27, 0.27, 0.27, 1),
                           on_press=lambda instance: self.button_pressed("AC"))
        row1.add_widget(ac_button)

        del_button = Button(text='Del',
                            font_name='Montserrat',
                            font_size=20,
                            size_hint=(None, None),
                            width=93.75,
                            height=68,
                            background_color=(0.27, 0.27, 0.27, 1),
                            on_press=lambda instance: self.button_pressed("Del"))
        row1.add_widget(del_button)

        divide_button = Button(text='÷',
                               font_name='Montserrat',
                               font_size=20,
                               size_hint=(None, None),
                               width=93.75,
                               height=68,
                               background_color=(0.85, 0.59, 0.1, 1),
                               on_press=lambda instance: self.button_pressed("÷"))
        row1.add_widget(divide_button)

        button_grid.add_widget(row1)

        # Row 2: 7, 8, 9, x
        row2 = BoxLayout(spacing=5)
        for num in ['7', '8', '9', 'x']:
            button = Button(text=num,
                            font_name='Montserrat',
                            font_size=20,
                            size_hint=(None, None),
                            width=93.75,
                            height=68,
                            background_color=(0.27, 0.27, 0.27, 1),
                            on_press=lambda instance, num=num: self.button_pressed(num))
            row2.add_widget(button)
        button_grid.add_widget(row2)

        # Row 3: 4, 5, 6, -
        row3 = BoxLayout(spacing=5)
        for num in ['4', '5', '6', '−']:
            button = Button(text=num,
                            font_name='Montserrat',
                            font_size=20,
                            size_hint=(None, None),
                            width=93.75,
                            height=68,
                            background_color=(0.27, 0.27, 0.27, 1),
                            on_press=lambda instance, num=num: self.button_pressed(num))
            row3.add_widget(button)
        button_grid.add_widget(row3)

        # Row 4: 1, 2, 3, +
        row4 = BoxLayout(spacing=5)
        for num in ['1', '2', '3', '+']:
            button = Button(text=num,
                            font_name='Montserrat',
                            font_size=20,
                            size_hint=(None, None),
                            width=93.75,
                            height=68,
                            background_color=(0.27, 0.27, 0.27, 1),
                            on_press=lambda instance, num=num: self.button_pressed(num))
            row4.add_widget(button)
        button_grid.add_widget(row4)

        # Row 5: 0, ., =
        row5 = BoxLayout(spacing=5)
        for num in ['0', '.', '=']:
            button = Button(text=num,
                            font_name='Montserrat',
                            font_size=20,
                            size_hint=(None, None),
                            width=93.75 if num != '=' else 281.25,
                            height=68,
                            background_color=(0.27, 0.27, 0.27, 1),
                            on_press=lambda instance, num=num: self.button_pressed(num))
            row5.add_widget(button)
        button_grid.add_widget(row5)

        bottom_frame.add_widget(button_grid)
        main_layout.add_widget(bottom_frame)

        return main_layout

    def button_pressed(self, char):
        if char == 'AC':
            self.all_clear()
        elif char == 'Del':
            self.delete_last()
        elif char == '=':
            self.equals()
        else:
            self.pressed(char)

    def pressed(self, char):
        self.expression += char
        self.entry.text = self.expression

    def all_clear(self):
        self.expression = ""
        self.entry.text = ""

    def delete_last(self):
        if self.expression:
            self.expression = self.expression[:-1]
            self.entry.text = self.expression

    def equals(self):
        try:
            self.expression = self.expression.replace('÷', '/').replace('x', '*').replace('−', '-').replace('%', '/100')
            self.results = str(eval(self.expression))
            self.entry.text = self.results
            self.expression = ""
        except:
            self.entry.text = "Error"
            self.expression = ""

if __name__ == '__main__':
    CalculatorApp().run()
