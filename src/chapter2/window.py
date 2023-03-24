##
#  This program creates a graphics window with a rectangle. It provides the
#  template used with all of the graphical programs used in the book.
#

from ezgraphics import GraphicsWindow

# Create the window and access the canvas.
win = GraphicsWindow(1000, 1000)
canvas = win.canvas()

# To draw red outline setOutline(r,g,b)
canvas.setOutline(255, 0, 0)
# To set fill color of green setFill(r,g,b)
canvas.setFill(0, 255, 0)

# Draw on the canvas between the points (x, y, width, height)
canvas.drawRect(20, 20, 30, 50)

# draws a line on the canvas between the points (x1, y1) and (x2, y2)
canvas.drawLine(100, 100, 200, 100)

# draw a text on the canvas drawText(x, y, text)
canvas.drawText(50, 100, "Message")

# To draw an oval drawOval(x, y, width, height). For circle use same width and height.
canvas.drawOval(150, 150, 50, 40)

# Wait for the user to close the window.
win.wait()

