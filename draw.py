from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    x, y = int(x0), int(y0)
    if y1 - y0 == 0:
        while x <= x1:
            plot(screen, color, x, y)
            x += 1
    elif x1 - x0 == 0:
        if y0 > y1:
            y0, y1 = y1, y0
        while y <= y1:
            plot(screen, color, x, y)
            y += 1
    else:
        m = (y1 - y0) * 1.0 / (x1 - x0)
        A = y1 - y0
        B = -(x1 - x0)
        if m > 1:
            d = A + 2 * B
            while y <= y1:
                # print("(%d, %d)", x, y)
                plot(screen, color, x, y)
                if d < 0:
                    x += 1
                    d += (2 * A)
                y += 1
                d += (2 * B)
        elif m > 0:
            d = 2 * A + B
            while x <= x1:
                # print("(%d, %d)", x, y)
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += (2 * B)
                x += 1
                d += (2 * A)
        elif m > -1:
            d = 2 * A - B
            while x <= x1:
                # print("(%d, %d)", x, y)
                plot(screen, color, x, y)
                if d < 0:
                    y -= 1
                    d -= (2 * B)
                x += 1
                d += (2 * A)
        else:
            d = A - 2 * B
            while y >= y1:
                # print("(%d, %d)", x, y)
                plot(screen, color, x, y)
                if d > 0:
                    x += 1
                    d += (2 * A)
                y -= 1
                d -= (2 * B)
