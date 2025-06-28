from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class CalculatorApp(App):
    display_text = StringProperty('')
    
    def build(self):
        return CalculatorLayout()
    
    def pressed(self, char):
        self.root.ids.input_field.text += char
    
    def all_clear(self):
        self.root.ids.input_field.text = ''
    
    def delete_last(self):
        current_text = self.root.ids.input_field.text
        self.root.ids.input_field.text = current_text[:-1]
    
    def equals(self):
        try:
            expression = self.root.ids.input_field.text
            expression = expression.replace('÷', '/').replace('x', '*').replace('−', '-').replace('%', '/100')
            result = str(eval(expression))
            self.root.ids.input_field.text = result
        except:
            self.root.ids.input_field.text = 'Error'

class CalculatorLayout(BoxLayout):
    pass

if __name__ == '__main__':
    CalculatorApp().run()
