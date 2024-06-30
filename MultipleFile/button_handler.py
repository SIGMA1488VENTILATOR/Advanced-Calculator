# button_handler.py

def handle_button_click(calculator, button_text):
    if button_text == "C":
        calculator.current_expression = ""
        calculator.resultDisplay.setText(calculator.current_expression)
    elif button_text == "=":
        try:
            result = str(eval(calculator.current_expression))
            calculator.resultDisplay.setText(result)
            calculator.current_expression = result
        except Exception as e:
            calculator.resultDisplay.setText("Error")
            calculator.current_expression = ""
    else:
        calculator.current_expression += button_text
        calculator.resultDisplay.setText(calculator.current_expression)
