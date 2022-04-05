from draw.grid.cell import DEFAULT_CELL_WIDTH
from draw.grid import GridWithBars, Row
from utils.timetable import Timetable


class Gantt(GridWithBars):
    """
    gantt chart class
    """
    def __init__(
        self, x, y, project,
        default_cell_width=DEFAULT_CELL_WIDTH
    ):
        GridWithBars.__init__(self, x, y)
        self.default_cell_width = default_cell_width

        self.timetable = Timetable(
            project.start_date, project.end_date
        )
        self.project = project

        self.prepare_top_header()

        for entry in range(project.entries):
            r = Row()
            r.add_cols(len(self.timetable.days))
            self.add_row(r)

            for wp in project.workpackages:
                for t in wp.tasks:
                    print(wp, t)
            #g.add_bar((5, 3), 5)

            # ACCESS DATES BY DICT ?! =>DRAW BARS


    def prepare_top_header(self):
        """
        prepare the top header
        """
        fmap = {
            "year": self.timetable.years,
            "quarter": self.timetable.quarters,
            "month": self.timetable.months,
            "week": self.timetable.weeks,
            "day": self.timetable.days,
        }

        for s in self.timetable.hierarchy():
            r = Row()
            for items in s:
                cell = r.add_cell(
                    cell_width=self.default_cell_width * len(items),
                    text=items[0].default
                )

            self.add_row(r)
