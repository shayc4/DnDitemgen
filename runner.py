from Tkinter import *
from item import create
root = Tk()


def create_item():
    item_display_list.insert(INSERT,
                             "For a player of %s level:\n" %
                             player_level_scale.get())
    item = create()
    item_display_list.insert(INSERT,"%s \n" % item['name'])
    return 1

root.minsize(300, 300)
root.geometry("500x500")


m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
left = PanedWindow(orient=VERTICAL, bd=4)
right = PanedWindow(orient=VERTICAL, bd=4)
m1.add(left)
m1.add(right)

#Item display
item_display_list = Text(right)
item_display_list.pack()

#Level Slider
var = IntVar()
player_level_scale = Scale(left, variable=var, from_=1,
                           to=60, orient=HORIZONTAL)
player_level_scale.pack()

#Generate Button
generate_button = Button(left, text="Generate Item", command=create_item)
generate_button.pack()
root.mainloop()
