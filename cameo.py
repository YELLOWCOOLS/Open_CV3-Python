#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 13:24
# @Author  : YELLOWCOOL
# @File    : cameo.py
# @Software: python3.7

import cv2
import filters
from managers import WindowManager, CaptureManager

class Cameo(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0,cv2.CAP_DSHOW), self._windowManager, True)
        self._curveFilter = filters.BGRPortraCurveFilter()

    def run(self):
        """Run the main loop."""

        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            filters.strokeEdges(frame, frame)
            self._curveFilter.apply(frame, frame)

            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keynode):

        if keynode == 32:
            self._captureManager.writeImage('screencast.png')
        elif keynode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screenvicast.avi')
            else:
                self._captureManager.stopWriteVideo()
        elif keynode == 27:
            self._windowManager.destroyWindow()

if __name__ == "__main__":
    Cameo().run()