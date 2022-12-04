import tkinter as tk
import tkinter.messagebox as msgbox

window = tk.Tk()
window.geometry("300x200")
window.configure(bg="#ff8164")

def MsgBox():
    q1 = msgbox.askquestion("Trivia Question ( yes / no )", "The star is the most common symbol used in all national flags around the world.")
    if q1 == "yes":
        msgbox.showinfo("Congratulations!", "Your Answer is Correct!!")
        window.quit()
    else:
        msgbox.showinfo("Better Luck Next Time!", "Your Answer is Incorrect!!")
        window.quit()

btn = tk.Button(
    window, 
    text="Trivia", 
    bg="#f7f5bc",
    fg="#4b6043",
    activebackground="#85A77C", 
    activeforeground="#C42D2D", 
    bd=1,
    relief="raised",
    command=MsgBox
)
btn.pack(expand=True)

window.mainloop()