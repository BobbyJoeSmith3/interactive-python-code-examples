Week three

Canvas — Canvas and drawing
===========================

- The canvas is the area associated with an application where information contain in the application may be drawn.
- In SimpleGUI applications, the width and height of the canvas are specified (in pixels) in create_frame. (A pixel is the smallest unit of area that your computer can draw in.)
- The origin for the canvas is the upper left-hand corner.
- Positions in the canvas are specified as pairs [x,y] where x is the horizontal coordinate and y is the vertical coordinate.
- Lecture examples - Canvas and Drawing
- More examples - Structure


Event-driven drawing — Canvas and drawing
==========================================

- Computers refresh their screens around 60 times per sec.
- For each application, the computer calls a special event handler, the draw handler, that is registered to the application.
- In SimpleGUI, the draw handler is registered via set_draw_handler.
- The draw handler can modify the canvas via simple draw operations defined in SimplGUI
- Lecture examples - Canvas and Drawing
- More examples - Structure, Echo


String operations — String processing
=====================================

- The function str converts other types of data into a string.
- The concatenation operator + joins two strings to form a single string,
- The ith element of a string my_string can be access via my_string[i]. Note that strings are immutable (cannot be changed).
- Substrings of my_string can be accessed via slicing .
- Lecture examples - Strings, Dollars and Cents One, Dollars and Cents Two
- More examples - Operations, Input Checking, Initials


Drawing text — Interactive drawing
===================================

- The method draw_text draws a string when given a position (lower left corner), a font size and a color.
- The method draw_circle (see "More examples" below) draws a circle at a given point with a given radius in pixels. To draw a point, draw a circle of radius one.
- The method draw_line (see "More examples" below) draws a line between two points.
- The method draw_polygon (see "More examples" below) draws a sequence of points (enclosed in square brackets and separated by commas) as a closed polygon.
- Colors for drawing methods can be specified as HTML color strings; "White", "Red", "Green", ...
- Lecture examples - Drawing, Interactive Drawing
- More examples - Shapes, Pictures, Hidden Picture


Timers — Timers
==================
- Timers are another component of SimpleGUI that generate regularly timed events.
- Users create a timer using create_timer with a specified interval and event handler.
- The timer calls its associated event handler regularly at the given interval.
- A timer t is started with t.start() and is stopped by t.stop().
- Lecture examples - Timers
- More examples - Blinking Text, Reaction Time
