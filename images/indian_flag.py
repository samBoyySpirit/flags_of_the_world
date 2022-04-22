from joy import *
from _img import render

#Country: Republic of India
#Description: Representing Indian Flag.
#version: 1.0.0
#Status: Completed

#Co-ordinates for the lines.
x1,y1 = 0,41
x2,y2 = 0,-41

#Individual components of the Indian flag.
saffron_rectangle = rectangle(y=100,w=300, h=100, fill="#FF9933",stroke="none")
white_rectangle = rectangle(w=300, h=100, fill="#FFFFFF",stroke="none")
green_rectangle = rectangle(y=-100,w=300, h=100, fill="#138808",stroke="none")
outer_circle = circle(r=41, stroke="#000080", stroke_width=4)
inner_circle = circle(r=7, fill="#000080", stroke="none")
spokes = line(x1,y1,x2,y2, fill="#000080", stroke_width=2) | repeat(24, rotate(15))
semi_circles = circle(x=5,y=39,r=3,fill="#000080",stroke="none") | repeat(24, rotate(15))

#combine all the various shapes and assign them to a single variable.
indian_flag = saffron_rectangle + white_rectangle + green_rectangle + outer_circle + inner_circle + spokes + semi_circles

#display the indian flag.
show(indian_flag)
render(indian_flag)