from draw.base import Dimension, Margin, Padding
from draw.base.consts import DEFAULT_MARGIN, DEFAULT_PADDING
from draw.shapes.line import Line


class Box(Dimension):
    """
    box that has a position, a size, a filling and a
    borderstyle (per side); additionally, margin and
    padding is considered
    """
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        fill: str = "white",
        margin: Margin = DEFAULT_MARGIN,
        padding: Padding = DEFAULT_PADDING,
        class_: str = "defaultbox"
    ):
        Dimension.__init__(self, x, y, width, height)
        
        self.fill = fill
        self.margin = margin
        self.padding = padding
        self.class_ = class_

    def draw(self, dwg, grp=None):
        # get group
        grp = grp or dwg.g()

        # rectangle for background
        grp.add(
            dwg.rect(
                (
                    self.x1 + self.margin.left,
                    self.y1 + self.margin.top,
                ),
                (
                    self.width - self.margin.right - self.margin.left,
                    self.height - self.margin.bottom - self.margin.top
                ),
                class_=f"{self.class_} background"
            )
        )

        # top
        top_line = Line(
            self.x1 + self.margin.left,
            self.y1 + self.margin.top,
            self.x2 - self.margin.right - self.margin.left,
            self.y1 + self.margin.top,
            class_=f"{self.class_} top"
        )
        top_line.draw(dwg, grp)

        # right
        right_line = Line(
            self.x2 - self.margin.right - self.margin.left,
            self.y1 + self.margin.top,
            self.x2 - self.margin.right - self.margin.left,
            self.y2 - self.margin.bottom - self.margin.top,
            class_=f"{self.class_} right"
        )
        right_line.draw(dwg, grp)

        # bottom
        bottom_line = Line(
            self.x1 + self.margin.left,
            self.y2 - self.margin.bottom - self.margin.top,
            self.x2 - self.margin.right - self.margin.left,
            self.y2 - self.margin.bottom - self.margin.top,
            class_=f"{self.class_} bottom"
        )
        bottom_line.draw(dwg, grp)

        # left
        left_line = Line(
            self.x1 + self.margin.left,
            self.y1 + self.margin.top,
            self.x1 + self.margin.left,
            self.y2 - self.margin.bottom - self.margin.top,
            class_=f"{self.class_} left"
        )
        left_line.draw(dwg, grp)

        return grp

    def __repr__(self):
        return f"<Box(dimension={self})>"
