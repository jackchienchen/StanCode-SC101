"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    year_d = {}
    x_margin = (width-GRAPH_MARGIN_SIZE*2)//(len(YEARS))  # The width margin across every year.
    x = GRAPH_MARGIN_SIZE  # The starting x point
    for i in range(len(YEARS)):
        year_d[str(YEARS[i])] = x
        x += x_margin
    return year_d[str(YEARS[year_index])]


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the current year
    returns the y coordinate where the rank should be drawn.

    Input:
        height (int): The height of the canvas
        rank (str): The rank number
    Returns:
        y_coordinate (int): The y coordinate of the rank.
    """
    # GRAPH_MARGIN_SIZE + (dividing the chart height into 1000 pieces, thus times the rank)
    return GRAPH_MARGIN_SIZE + (((height-GRAPH_MARGIN_SIZE*2)/1000)*int(rank))


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE
                       , width=LINE_WIDTH, fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                       , width=LINE_WIDTH, fill='black')
    canvas.create_line(CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='white')
    for i in range(len(YEARS)):  # to create the vertical lines for each year.
        x_margin = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_margin, 0, x_margin, CANVAS_HEIGHT, width=LINE_WIDTH, fill='black')
        canvas.create_text(x_margin, CANVAS_HEIGHT, text=YEARS[i], anchor=tkinter.SW, fill='black', font='times 20')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid
    # ----- Write your code below this line ----- #
    for j in range(len(lookup_names)):  # loop the amount of names for search
        # loop the amount of years given( -1 since the last line created contains the last year's point(x,y)
        for i in range(len(YEARS) - 1):
            color = COLORS[j % len(COLORS)]  # rotation of the colors
            rank_content = ''  # the str for (Name,Rank) that appears on the graph
            k = i + 1  # the index for the next point
            x1 = get_x_coordinate(CANVAS_WIDTH, i)
            x2 = get_x_coordinate(CANVAS_WIDTH, k)
            if str(YEARS[i]) not in name_data[lookup_names[j]]:
                # if the lookup name isn't in ranked in top 1000 names for a certain year
                # the y will be at the bottom of the chart
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2
                rank_content += '*'
                if str(YEARS[k]) not in name_data[lookup_names[j]]:  # if the further point isn't ranked top 1000
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2
                else:
                    y2 = get_y_coordinate(CANVAS_HEIGHT, name_data[lookup_names[j]][str(YEARS[k])])
            else:
                y1 = get_y_coordinate(CANVAS_HEIGHT, name_data[lookup_names[j]][str(YEARS[i])])
                rank_content += name_data[lookup_names[j]][str(YEARS[i])]
                if str(YEARS[k]) not in name_data[lookup_names[j]]:
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2
                else:
                    y2 = get_y_coordinate(CANVAS_HEIGHT, name_data[lookup_names[j]][str(YEARS[k])])
            canvas.create_line(x1, GRAPH_MARGIN_SIZE + y1, x2, GRAPH_MARGIN_SIZE + y2, width=LINE_WIDTH,
                               fill=color)  # create line between two decades
            canvas.create_text(x1 + TEXT_DX, GRAPH_MARGIN_SIZE + y1, text=lookup_names[j] + ' ' + rank_content,
                               anchor=tkinter.SW, fill=color, font='times 15')
    

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
