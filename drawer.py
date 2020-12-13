import matplotlib.pyplot as plt


class Text():
    def __init__(self, pos, txt):
        self.pos = pos
        self.text = txt

    def draw(self):
        plt.text(self.pos[0] + 0.05, self.pos[1], self.text, size=15)


class Points():
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

    def draw(self):
        plt.scatter(self.xs, self.ys)


class Lines():
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

    def draw(self):
        plt.plot(self.xs, self.ys)


class Figure():
    def __init__(self):
        self.items = []

    def add_points(self, ps):
        self.add(Points(ps[:, 0], ps[:, 1]))

    def add_point(self, x, y):
        self.add(Points([x], [y]))

    def add(self, x):
        self.items.append(x)

    def draw(self):
        for i in self.items:
            i.draw()

    def add_lines(self, *ps):
        xs = [p[0] for p in ps]
        ys = [p[1] for p in ps]
        self.add(Lines(xs, ys))

    def add_text(self, pos, txt):
        self.add(Text(pos, txt))


def fig():
    return Figure()
