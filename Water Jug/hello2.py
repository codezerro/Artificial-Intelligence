from tkinter import *

main_win = Tk()
main_win.title("Delay Test")
main_win.geometry('500x500')


def display_loop(data, index=0):
    # canvas.delete()
    display_item = data[index]
    delay, text = display_item
    # canvas.configure(text=text)
    c = canvas.create_line(10*index+100, 10*index+100, 240, 340, width=5)
    print(c)
    # test_label.configure(image=text)
    # test_label.image_names('ball.png')
    index += 1
    if index == (len(data)):
        return
    canvas.delete(c, END)
    main_win.after(delay, display_loop, data, index)


canvas = Canvas(main_win, width=300, height=300)
canvas.pack()


data = [[2000, 'Aa.png'], [2000, 'Aaa.png'], [2000, 'Aaaa.png'], [
    2000, 'Accc.png'], [2000, 'A.ccpng'], [2000, 'B'], [0, 'Ca']]
for i in range(3):
    display_loop(data)


main_win.mainloop()
