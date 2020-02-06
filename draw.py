from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0 != min(x0, x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    x, y = int(x0), int(y0)
    m = (y1 - y0) / (x1 - x0)
    if m > 0:
        if m > 1:
            return None
        else:
            A = y1 - y0
            B = -(x1 - x0)
            d = 2 * A + B
            while x <= x1:
                # print("(%d, %d)", x, y)
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += (2 * B)
                x += 1
                d += (2 * A)
    #
    # else:
    #     if m < 1:
