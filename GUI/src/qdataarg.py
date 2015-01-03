#!/usr/bin/env python
from __future__ import division, print_function

import symbolic
import signature

from PyQt4 import QtCore, QtGui


class QDataArg(QtGui.QWidget):
    def __init__(self, call):
        QtGui.QWidget.__init__(self)
        self.Qt_call = call
        self.app = call.app
        self.polygonmin = None
        self.linesminfront = None
        self.linesminback = None
        self.polygonmax = None
        self.linesmaxfront = None
        self.linesmaxback = None

        self.UI_init()

    def UI_init(self):
        self.setContentsMargins(0, 0, 0, 0)
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        layout.setSpacing(0)
        layout.setMargin(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # name
        self.Qt_name = QtGui.QLineEdit()
        layout.addWidget(self.Qt_name, 1, QtCore.Qt.AlignHCenter|
                         QtCore.Qt.AlignVCenter)
        self.Qt_name.setAlignment(QtCore.Qt.AlignHCenter)
        self.Qt_name.textChanged.connect(self.change)
        regexp = QtCore.QRegExp("[a-zA-Z]+")
        validator = QtGui.QRegExpValidator(regexp, self.app)
        self.Qt_name.setValidator(validator)

        # vary
        self.Qt_vary = QtGui.QCheckBox("vary")
        layout.addWidget(self.Qt_vary, 0, QtCore.Qt.AlignHCenter |
                         QtCore.Qt.AlignBottom)
        self.Qt_vary.setSizePolicy(QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed,
            QtGui.QSizePolicy.Fixed
        ))
        self.Qt_vary.stateChanged.connect(self.vary_change)

        # style
        self.setStyleSheet("""
            [invalid="true"] QLineEdit {
                background: #FFDDDD;
            }
            [invalid="false"] > QLineEdit:!focus:!hover {
                background: transparent;
                border: none;
            }
        """)

    def paintEvent(self, event):
        if not self.polygonmax:
            return QtGui.QWidget.paintEvent(self, event)

        brushes = self.app.Qt_brushes
        pens = self.app.Qt_pens
        painter = QtGui.QPainter(self)

        # max
        painter.setBrush(brushes["max"])
        painter.setPen(pens[None])
        painter.drawPolygon(self.polygonmax)
        painter.setPen(pens["maxback"])
        painter.drawLines(self.linesmaxback)
        painter.setPen(pens["maxfront"])
        painter.drawLines(self.linesmaxfront)

        # min
        painter.setBrush(brushes["min"])
        painter.setPen(pens[None])
        painter.drawPolygon(self.polygonmin)
        painter.setPen(pens["minback"])
        painter.drawLines(self.linesminback)
        painter.setPen(pens["minfront"])
        painter.drawLines(self.linesminfront)

    # getter
    def text(self):
        return self.Qt_name.text()

    # setters
    def set(self):
        value = self.app.calls[self.Qt_call.callid][self.argid]
        if value is None:
            self.Qt_name.setText("")
            self.Qt_vary.setChecked(False)
        else:
            self.Qt_name.setText(value)
            self.Qt_vary.setChecked(self.app.vary[value])
        self.viz()

    def setsize(self, height, width):
        nameheight = self.Qt_name.minimumSizeHint().height()
        namewidth = self.Qt_name.minimumSizeHint().width()
        namewidth += self.Qt_name.fontMetrics().width(self.Qt_name.text())
        namewidth = max(namewidth, nameheight)
        varywidth = varyheight = 0
        if self.app.usevary:
            varyheight = self.Qt_vary.minimumSizeHint().height()
            varywidth = self.Qt_vary.minimumSizeHint().width()
        contentheight = nameheight + varyheight
        contentwidth = max(namewidth, varywidth)
        fixedwidth = max(width, contentwidth)
        fixedheight = max(height, contentheight)
        self.setFixedSize(fixedwidth, fixedheight)
        hoff = max(0, (contentheight - height) // 2)
        woff = max(0, (contentwidth - width) // 2)
        return hoff, woff

    def viz(self):
        value = self.app.calls[self.Qt_call.callid][self.argid]
        if value is None:
            self.viz_none()
            return
        self.Qt_vary.setChecked(self.app.vary[value])
        data = self.app.data[value]
        if data["sym"] is None:
            self.viz_none()
            return
        if not isinstance(data["sym"], symbolic.Prod):
            # TODO
            self.app.alert("don't know how to vizualize", data["sym"])
            self.viz_none()
            return
        # compute min and max from range
        scale = self.app.datascale / self.app.data_maxdim()
        dim = data["sym"][1:]
        dimmin = []
        dimmax = []
        for expr in dim:
            values = self.app.range_eval(expr)
            if any(value is None for value in values):
                self.viz_none()
                return
            dimmin.append(round(scale * min(values)))
            dimmax.append(round(scale * max(values)))
        if len(dim) == 1:
            self.viz_vector(dimmin, dimmax)
        elif len(dim) == 2:
            self.viz_matrix(dimmin, dimmax)
        elif len(dim) == 3:
            self.viz_tensor(dimmin, dimmax)

    def viz_none(self):
        self.polygonmax = None
        self.linesmaxfront = None
        self.linesmaxback = None
        self.polygonmin = None
        self.linesminfront = None
        self.linesminback = None
        self.setMinimumSize(self.Qt_name.minimumSize())

    def viz_vector(self, dimmin, dimmax):
        self.viz_matrix(dimmin + [1], dimmax + [1])

    def viz_matrix(self, dimmin, dimmax):
        properties = self.app.calls[self.Qt_call.callid].properties(self.argid)
        for prop in properties:
            if prop in (signature.lower, signature.upper):
                self.viz_triangular(dimmin, dimmax, properties)
                return
        self.viz_tensor(dimmin + [1], dimmax + [1])

    def viz_triangular(self, dimmin, dimmax, properties):
        # compute total size and offsets
        h, w = dimmax
        hoff, woff = self.setsize(h + 1, w + 1)
        # maximum
        h, w = dimmax
        points = [[QtCore.QPoint(woff + x, hoff + y)
                   for x in [0, w]]
                  for y in [0, h]]
        if signature.lower in properties:
            self.polygonmax = QtGui.QPolygon([
                points[0][0],
                points[1][0],
                points[1][1],
                points[0][0],
            ])
            self.linesmaxfront = [
                QtCore.QLine(points[0][0], points[1][0]),  # |
                QtCore.QLine(points[1][0], points[1][1]),  # -
                QtCore.QLine(points[1][1], points[0][0]),  # \
            ]
        else:
            self.polygonmax = QtGui.QPolygon([
                points[0][0],
                points[1][1],
                points[0][1],
                points[0][0],
            ])
            self.linesmaxfront = [
                QtCore.QLine(points[0][0], points[1][1]),  # \
                QtCore.QLine(points[1][1], points[0][1]),  # |
                QtCore.QLine(points[0][1], points[0][0]),  # -
            ]
        self.linesmaxback = []
        if signature.symm in properties or signature.herm in properties:
            self.linesmaxback = [
                QtCore.QLine(points[0][0], points[1][0]),  # |
                QtCore.QLine(points[1][0], points[1][1]),  # -
                QtCore.QLine(points[1][1], points[0][1]),  # |
                QtCore.QLine(points[0][1], points[0][0]),  # -
            ]
        # minimum
        h, w = dimmin
        points = [[QtCore.QPoint(woff + x, hoff + y)
                   for x in [0, w]]
                  for y in [0, h]]
        if signature.lower in properties:
            self.polygonmin = QtGui.QPolygon([
                points[0][0],
                points[1][0],
                points[1][1],
                points[0][0],
            ])
            self.linesminfront = [
                QtCore.QLine(points[0][0], points[1][0]),  # |
                QtCore.QLine(points[1][0], points[1][1]),  # -
                QtCore.QLine(points[1][1], points[0][0]),  # \
            ]
        else:
            self.polygonmin = QtGui.QPolygon([
                points[0][0],
                points[1][1],
                points[0][1],
                points[0][0],
            ])
            self.linesminfront = [
                QtCore.QLine(points[0][0], points[1][1]),  # \
                QtCore.QLine(points[1][1], points[0][1]),  # |
                QtCore.QLine(points[0][1], points[0][0]),  # -
            ]
        self.linesminback = []
        if signature.symm in properties or signature.herm in properties:
            self.linesminback = [
                QtCore.QLine(points[0][0], points[1][0]),  # |
                QtCore.QLine(points[1][0], points[1][1]),  # -
                QtCore.QLine(points[1][1], points[0][1]),  # |
                QtCore.QLine(points[0][1], points[0][0]),  # -
            ]

    def viz_tensor(self, dimmin, dimmax):
        # compute total size and offsets
        h, w, d = dimmax
        hoff, woff = self.setsize(h + d // 2 + 1, w + d // 2 + 1)
        # maximum
        h, w, d = dimmax
        points = [[[QtCore.QPoint(woff + x + z // 2, hoff + y + (d - z) // 2)
                    for z in [0, d]]
                   for x in [0, w]]
                  for y in [0, h]]
        self.polygonmax = QtGui.QPolygon([
            points[0][0][0],
            points[1][0][0],
            points[1][1][0],
            points[1][1][1],
            points[0][1][1],
            points[0][0][1],
        ])
        self.linesmaxfront = [
            QtCore.QLine(points[0][0][0], points[0][0][1]),  # /
            QtCore.QLine(points[0][1][0], points[0][1][1]),  # /
            QtCore.QLine(points[1][1][0], points[1][1][1]),  # /
            QtCore.QLine(points[0][0][0], points[0][1][0]),  # -
            QtCore.QLine(points[0][0][1], points[0][1][1]),  # -
            QtCore.QLine(points[1][0][0], points[1][1][0]),  # -
            QtCore.QLine(points[0][0][0], points[1][0][0]),  # |
            QtCore.QLine(points[0][1][0], points[1][1][0]),  # |
            QtCore.QLine(points[0][1][1], points[1][1][1]),  # |
        ]
        self.linesmaxback = [
            QtCore.QLine(points[1][0][0], points[1][0][1]),  # /
            QtCore.QLine(points[1][0][1], points[1][1][1]),  # -
            QtCore.QLine(points[0][0][1], points[1][0][1]),  # |
        ]
        # minimum
        h, w, d = dimmin
        points = [[[QtCore.QPoint(woff + x + z // 2, hoff + y + (d - z) // 2)
                    for z in [0, d]]
                   for x in [0, w]]
                  for y in [0, h]]
        self.polygonmin = QtGui.QPolygon([
            points[0][0][0],
            points[1][0][0],
            points[1][1][0],
            points[1][1][1],
            points[0][1][1],
            points[0][0][1],
        ])
        self.linesminfront = [
            QtCore.QLine(points[0][0][0], points[0][0][1]),  # /
            QtCore.QLine(points[0][1][0], points[0][1][1]),  # /
            QtCore.QLine(points[1][1][0], points[1][1][1]),  # /
            QtCore.QLine(points[0][0][0], points[0][1][0]),  # -
            QtCore.QLine(points[0][0][1], points[0][1][1]),  # -
            QtCore.QLine(points[1][0][0], points[1][1][0]),  # -
            QtCore.QLine(points[0][0][0], points[1][0][0]),  # |
            QtCore.QLine(points[0][1][0], points[1][1][0]),  # |
            QtCore.QLine(points[0][1][1], points[1][1][1]),  # |
        ]
        self.linesminback = [
            QtCore.QLine(points[1][0][0], points[1][0][1]),  # /
            QtCore.QLine(points[1][0][1], points[1][1][1]),  # -
            QtCore.QLine(points[0][0][1], points[1][0][1]),  # |
        ]

    def usevary_apply(self):
        self.Qt_vary.setVisible(self.app.usevary)

    # event handlers
    def change(self):
        value = str(self.Qt_name.text())
        width = self.Qt_name.fontMetrics().width(value)
        width += self.Qt_name.minimumSizeHint().width()
        height = self.Qt_name.sizeHint().height()
        self.Qt_name.setFixedSize(max(height, width), height)
        if self.app.setting:
            return
        value = str(self.Qt_name.text())
        self.app.UI_arg_change(self.Qt_call.callid, self.argid, value)

    def vary_change(self):
        if self.app.setting:
            return
        self.app.UI_vary_change(self.Qt_call.callid, self.argid,
                                self.Qt_vary.isChecked())