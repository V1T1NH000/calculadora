import customtkinter as ct
from PIL import Image

# App appearance mode, settings & more
ct.set_appearance_mode("System")
app = ct.CTk(fg_color="black")
app.title("pyCalculator")
app.geometry(f"{425}x{680}")
app.resizable(False, False)

# Fonts & Colors
monst = ct.CTkFont(family="Montserrat", size=80, weight="bold")
monst2 = ct.CTkFont(family="Montserrat", size=20, weight="bold")
dark_grey = "#454545"
light_grey = "#999999"
lighter = "#AFAABB"
darker = "#696379"
orange = "#DA971A"
mid = "#7965B0"
result_color = "#F4F3F5"

# App Frames
frame1 = ct.CTkFrame(app, fg_color="black")
frame1.pack(side="top", expand=True, fill="both", padx=5, pady=5)

frame2 = ct.CTkFrame(app, fg_color="black")
frame2.pack(side="bottom", expand=True, fill="both", padx=5, pady=5)

# Entry/title/Logo
Image_Label = ct.CTkLabel(master=frame1,
                          text="",
                          font=monst,
                          text_color="white",
                          width=425, height=90
                          )
Image_Label.pack(expand=True, fill="both", side="top")

entry = ct.CTkEntry(master=frame1,
                    justify="right",
                    state="normal",
                    height=150,
                    fg_color="black",
                    font=monst,
                    border_color="black",
                    text_color=result_color  # Cor do resultado
                    )
entry.pack(expand=True, fill="both", side="bottom", pady=5, padx=5)

# --- FUNCTIONS ---

expression = ""
results = ""

# Function ---> update AC button and command
def update_All_Clear_Btn():
    global expression, results
    if not expression or results:
        All_Clear_Btn.configure(text="AC", command=all_clear)
    else:
        All_Clear_Btn.configure(text="C", command=all_clear)

# Function ---> Pressed button
def pressed(char):
    global expression

    # Grab button values, & extend cursor
    current_entry = entry.get()
    new_entry = current_entry + char
    entry.delete(0, ct.END)
    entry.insert(0, new_entry)
    expression = new_entry
    entry.xview_moveto(1.0)
    entry.icursor(len(new_entry))
    update_All_Clear_Btn()

# Function ---> All Clear (AC)
def all_clear():
    global expression, results
    entry.delete(0, ct.END)
    expression = ""
    update_All_Clear_Btn()

# Function ---> Delete last character
def delete_last():
    global expression
    current_entry = entry.get()
    if current_entry:
        new_entry = current_entry[:-1]
        entry.delete(0, ct.END)
        entry.insert(0, new_entry)
        expression = new_entry
    update_All_Clear_Btn()

# Function ---> Equals
def equals():
    global expression, results

    # Replace customs, eval & Update entry
    try:
        expression = expression.replace("÷", "/").replace("x", "*").replace("−", "-").replace("%", "/100")
        results = str(eval(expression))
        entry.delete(0, ct.END)
        entry.insert(0, results)
        expression = results
        entry.xview_moveto(1.0)
        entry.icursor(len(results))
        update_All_Clear_Btn()
        expression = ""
        results = ""
        adjust_font_size(entry)

    # Handle errors
    except Exception as e:
        handle_error()

# Function ---> Error Handling & Update AC       
def handle_error():
    global expression, results
    entry.delete(0, ct.END)
    entry.insert(0, "Error")
    expression = ""
    results = ""
    update_All_Clear_Btn()

# Function ---> Adjust results to fit dynamically
def adjust_font_size(widget):
    max_font_size = 80
    min_font_size = 20
    max_width = widget.winfo_width() - 20
    text = widget.get()

    # Calculate font_size based on text length & entry width
    font_size = max(min_font_size, min(max_font_size, int(max_width / len(text))))

    # Configure to Montserrat
    widget.configure(font=("Montserrat", font_size, "bold"))

# --- OTHER WIDGETS---

# Buttons /1
All_Clear_Btn = ct.CTkButton(master=frame2, text="AC",
                             corner_radius=50,
                             width=93.75, height=68,
                             font=monst2,
                             fg_color=light_grey,
                             hover_color=lighter,
                             command=all_clear)
All_Clear_Btn.grid(row=0, column=0, sticky="nswe", pady=5, padx=5)

delete_Btn = ct.CTkButton(master=frame2, text="Del",
                          corner_radius=50,
                          width=93.75, height=68,
                          font=monst2,
                          fg_color=light_grey,
                          hover_color=lighter,
                          command=delete_last)
delete_Btn.grid(row=0, column=1, sticky="nswe", pady=5, padx=5)

Btn_7 = ct.CTkButton(master=frame2, text="7",
                     corner_radius=50, width=93.75, height=68,
                     font=monst2,
                     fg_color=dark_grey,
                     hover_color=darker,
                     command=lambda: pressed("7"))
Btn_7.grid(row=1, column=0, sticky="nswe", pady=5, padx=5)

Btn_4 = ct.CTkButton(master=frame2, text="4",
                     corner_radius=50,
                     width=93.75, height=68,
                     font=monst2,
                     fg_color=dark_grey,
                     hover_color=darker,
                     command=lambda: pressed("4"))
Btn_4.grid(row=2, column=0, sticky="nswe", pady=5, padx=5)

Btn_1 = ct.CTkButton(master=frame2, text="1",
                     corner_radius=50,
                     width=93.75, height=68,
                     font=monst2,
                     fg_color=dark_grey,
                     hover_color=darker,
                     command=lambda: pressed("1"))
Btn_1.grid(row=3, column=0, sticky="nswe", pady=5, padx=5)

Btn_0 = ct.CTkButton(master=frame2, text="0",
                     corner_radius=50,
                     width=93.75, height=68,
                     font=monst2,
                     anchor="w",
                     fg_color=dark_grey,
                     hover_color=darker,
                     command=lambda: pressed("0"))
Btn_0.grid(row=4, column=0, sticky="nswe", pady=5, columnspan=2, padx=5)

# Buttons /2
percent_Btn = ct.CTkButton(master=frame2, text="%",
                           corner_radius=50,
                           width=93.75, height=68,
                           font=monst2,
                           fg_color=light_grey,
                           hover_color=lighter,
                           command=lambda: pressed("%"))
percent_Btn.grid(row=0, column=2, sticky="nswe", pady=5, padx=5)

Btn_8 = ct.CTkButton(master=frame2, text="8",
                     corner_radius=50,
                     width=93.75, height=68,
                     font=monst2,
                     fg_color=dark_grey,
                     hover_color=darker,
                     command=lambda: pressed("8"))
Btn_8.grid(row=1, column=1, sticky="nswe", pady=5, padx=5)

Btn_5 = ct.CTkButton(master=frame2, text="5",
                     corner_radius=50,
                     width=93.75, height=68,
                     font=monst2,
                     fg_color=dark_grey,
                     hover_color=darker,
                     command=lambda: pressed("5"))
Btn_5.grid(row=2, column=1, sticky="nswe", pady=5, padx=5)

Btn_2 = ct.CTkButton(master=frame2, text="2",
                     corner_radius=50,
                     width=93.75, height=68,
                     font=monst2,
                     fg_color=dark_grey,
                     hover_color=darker,
                     command=lambda: pressed("2"))
Btn_2.grid(row=3, column=1, sticky="nswe", pady=5, padx=5)

point_Btn = ct.CTkButton(master=frame2, text=".",
                         corner_radius=50,
                         width=93.75, height=68,
                         font=monst2,
                         fg_color=dark_grey,
                         hover_color=darker,
                         command=lambda: pressed("."))
point_Btn.grid(row=4, column=2, sticky="nswe", pady=5, padx=5)

# Buttons /3
Btn_9 = ct.CTkButton(master=frame2, text="9",
                     corner_radius=50,
                     width=93.75, height=68,
                     font=monst2,
                     fg_color=dark_grey,
                     hover_color=darker,
                     command=lambda: pressed("9"))
Btn_9.grid(row=1, column=2, sticky="nswe", pady=5, padx=5)

Btn_6 = ct.CTkButton(master=frame2, text="6",
                     corner_radius=50,
                     width=93.75, height=68,
                     font=monst2,
                     fg_color=dark_grey,
                     hover_color=darker,
                     command=lambda: pressed("6"))
Btn_6.grid(row=2, column=2, sticky="nswe", pady=5, padx=5)

Btn_3 = ct.CTkButton(master=frame2, text="3",
                     corner_radius=50,
                     width=93.75, height=68,
                     font=monst2,
                     fg_color=dark_grey,
                     hover_color=darker,
                     command=lambda: pressed("3"))
Btn_3.grid(row=3, column=2, sticky="nswe", pady=5, padx=5)

# Buttons /4
div_Btn = ct.CTkButton(master=frame2, text="÷",
                       corner_radius=50,
                       width=93.75, height=68,
                       font=monst2,
                       fg_color=orange,
                       hover_color=mid,
                       command=lambda: pressed("÷"))
div_Btn.grid(row=0, column=3, sticky="nswe", pady=5, padx=5)

mul_Btn = ct.CTkButton(master=frame2, text="x",
                       corner_radius=50,
                       width=93.75, height=68,
                       font=monst2,
                       fg_color=orange,
                       hover_color=mid,
                       command=lambda: pressed("x"))
mul_Btn.grid(row=1, column=3, sticky="nswe", pady=5, padx=5)

minus_Btn = ct.CTkButton(master=frame2, text="−",
                         corner_radius=50,
                         width=93.75, height=68,
                         font=monst2,
                         fg_color=orange,
                         hover_color=mid,
                         command=lambda: pressed("−"))
minus_Btn.grid(row=2, column=3, sticky="nswe", pady=5, padx=5)

add_Btn = ct.CTkButton(master=frame2, text="+",
                       corner_radius=50,
                       width=93.75, height=68,
                       font=monst2,
                       fg_color=orange,
                       hover_color=mid,
                       command=lambda: pressed("+"))
add_Btn.grid(row=3, column=3, sticky="nswe", pady=5, padx=5)

equal_Btn = ct.CTkButton(master=frame2, text="=",
                         corner_radius=50,
                         width=93.75, height=68,
                         font=monst2,
                         fg_color=orange,
                         hover_color=mid,
                         command=equals)
equal_Btn.grid(row=4, column=3, sticky="nswe", pady=5, padx=5)

# Run app (as admin😁)
app.mainloop()
