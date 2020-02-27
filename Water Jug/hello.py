# # # Python and Tkinter: Creating the Canvas and Adding Shapes
# # from tkinter import *
# # import waterJugvtwo
# # import time

# # root = Tk()
# # path = waterJugvtwo.WaterJug(4, 3, 2)

# # root.geometry('500x500')


# # def line():
# #     return c.create_line(
# #         path[val][0]*50, path[val][1]*50, 20, 20, width=10)


# # c = Canvas(root, height=250, width=300, bg="blue")
# # for val in range(len(path)):
# #     # c = Canvas(root, height=250, width=300, bg="blue")
# #     # line =
# #     root.after(2000, line)
# # c.pack()


# # if __name__ == "__main__":
# #     # start main loop
# #     root.mainloop()


# # # print(path)


# from PIL import ImageTk, Image
# from tkinter import *


# def display_loop(data, index=0):
#     display_item = data[index]
#     delay, text = display_item
#     test_label.configure(text=text)
#     # test_label.configure(image=text)
#     # test_label.image_names('ball.png')
#     index += 1
#     if index == len(data):
#         return

#     main_win.after(delay, display_loop, data, index)


# main_win = Tk()
# main_win.title("Delay Test")
# main_win.geometry('500x500')
# #


# #

# test_label = Label(main_win, font=('Helvetica', 20, 'bold'))
# # test_label.grid(column=0, row=0)
# canvas = Canvas(main_win, width=300, height=300)
# canvas.pack()


# data = [[2000, 'A.png'], [2000, 'B'], [0, 'C']]
# display_loop(data)

# main_win.mainloop()


# # img = ImageTk.PhotoImage(Image.open("ball.png"))
# # canvas.create_image(20, 20, anchor=NW, image=img)

t = ((4, 4), (34, 2))
x = list(t)
print(type(x))
