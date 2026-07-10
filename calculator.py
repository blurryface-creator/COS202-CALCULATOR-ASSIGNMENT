import tkinter as tk
from tkinter import messagebox

class MathematicalCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Mathematical Calculator")
        self.root.geometry("360x520")
        self.root.configure(bg="#1e1e24")
        self.root.resizable(False, False)

        # Stores the current mathematical expression
        self.expression = ""
        
        # Initialize UI Components
        self.create_display()
        self.create_buttons()

    def create_display(self):
        """Creates the interactive screen display area."""
        self.display_frame = tk.Frame(self.root, bg="#1e1e24")
        self.display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.display_label = tk.Label(
            self.display_frame,
            text="0",
            anchor="e",
            bg="#2a2a35",
            fg="#ffffff",
            padx=15,
            font=("Arial", 28, "bold"),
            height=2
        )
        self.display_label.pack(expand=True, fill="both")

    def create_buttons(self):
        """Creates and maps the calculator button grid."""
        self.buttons_frame = tk.Frame(self.root, bg="#1e1e24")
        self.buttons_frame.pack(expand=True, fill="both", padx=10, pady=(0, 10))

        # Layout grids configuration
        for i in range(6):
            self.buttons_frame.rowconfigure(i, weight=1)
        for j in range(4):
            self.buttons_frame.columnconfigure(j, weight=1)

        # Layout map using safe raw strings to prevent syntax flags
        button_layout = [
            ('OFF', 0, 0, '#d9534f'), ('C', 0, 1, '#f0ad4e'), ('%', 0, 2, '#5bc0de'), ('^', 0, 3, '#5bc0de'),
            ('7', 1, 0, '#3a3a4a'),   ('8', 1, 1, '#3a3a4a'),   ('9', 1, 2, '#3a3a4a'),   ('/', 1, 3, '#5bc0de'),
            ('4', 2, 0, '#3a3a4a'),   ('5', 2, 1, '#3a3a4a'),   ('6', 2, 2, '#3a3a4a'),   ('*', 2, 3, '#5bc0de'),
            ('1', 3, 0, '#3a3a4a'),   ('2', 3, 1, '#3a3a4a'),   ('3', 3, 2, '#3a3a4a'),   ('-', 3, 3, '#5bc0de'),
            ('0', 4, 0, '#3a3a4a'),   ('.', 4, 1, '#3a3a4a'),   (r'\', 4, 2, '#5bc0de'),  ('+', 4, 3, '#5bc0de'),
            ('=', 5, 0, '#5cb85c') 
        ]

        for text, row, col, bg_color in button_layout:
            if text == '=':
                btn = tk.Button(
                    self.buttons_frame, text=text, bg=bg_color, fg="#ffffff",
                    font=("Arial", 20, "bold"), borderwidth=0, activebackground="#4cae4c",
                    activeforeground="#ffffff", command=self.evaluate_expression
                )
                btn.grid(row=row, column=col, columnspan=4, sticky="nsew", padx=3, pady=3)
            else:
                btn = tk.Button(
                    self.buttons_frame, text=text, bg=bg_color, fg="#ffffff",
                    font=("Arial", 16, "bold"), borderwidth=0, activebackground="#a0a0a0",
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

    def on_button_click(self, char):
        """Manages keyboard and click interactions."""
        if char == 'OFF':
            self.root.destroy()
        elif char == 'C':
            self.expression = ""
            self.update_display("0")
        else:
            # Check edge cases for operators typed on empty screens
            if self.expression == "" and char in ['+', '*', '/', r'\', '^', '%', '.']:
                return
            
            self.expression += str(char)
            self.update_display(self.expression)

    def update_display(self, text):
        """Updates display text and handles character truncation."""
        if len(text) > 14:
            text = text[-14:]
        self.display_label.config(text=text)

    def evaluate_expression(self):
        """Translates custom operators and runs calculations safely."""
        try:
            sanitized_expr = self.expression
            
            # Map visual operators to actual Python math operators
            sanitized_expr = sanitized_expr.replace('^', '**')   
            sanitized_expr = sanitized_expr.replace(r'\', '//') 

            # Catch zero division bugs before engine execution
            if '/0' in sanitized_expr or '//0' in sanitized_expr or '%0' in sanitized_expr:
                raise ZeroDivisionError

            # Compute formula safely
            result = eval(sanitized_expr)
            
            # Strip redundant decimal values if integer
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.expression = str(result)
            self.update_display(self.expression)
            
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
            self.expression = ""
            self.update_display("Error")
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.expression = ""
            self.update_display("Error")

if __name__ == "__main__":
    window = tk.Tk()
    app = MathematicalCalculator(window)
    window.mainloop()
