#!/usr/bin/env python

from manimlib.imports import *

class FeynmanMachineTitle(Scene):
    def title_plate(self, ch_num, ch_title):
        title = TextMobject("Feynman Machine")
        chapter_title = TextMobject("Chapter ",ch_num,": ",ch_title)
        title.scale(3)
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.to_edge, UP)
        self.play(FadeIn(chapter_title),run_time=4)
        self.wait(6)
        self.play(FadeOut(chapter_title),
                  FadeOut(title))

class Ch01_01_Title(FeynmanMachineTitle):
    def construct(self):
        self.title_plate("1","Order to Chaos")
