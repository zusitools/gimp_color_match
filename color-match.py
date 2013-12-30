#!/usr/bin/env python

from gimpfu import *
import os

def color_match(img, drawable):
  tempname = pdb.gimp_temp_name("curve")
  fgcolor = pdb.gimp_context_get_foreground()
  bgcolor = pdb.gimp_context_get_background()

  default_line = "0 0 " + ("-1 -1 " * 15) + "255 255" + os.linesep
  red_line = "0 0 " + str(bgcolor[0]) + " " + str(fgcolor[0]) + " " + ("-1 -1 " * 14) + "255 255" + os.linesep
  green_line = "0 0 " + str(bgcolor[1]) + " " + str(fgcolor[1]) + " " + ("-1 -1 " * 14) + "255 255" + os.linesep
  blue_line = "0 0 " + str(bgcolor[2]) + " " + str(fgcolor[2]) + " " + ("-1 -1 " * 14) + "255 255" + os.linesep

  file_contents = "# GIMP Curves File" + os.linesep + default_line + red_line + green_line + blue_line + default_line

  with open(tempname, "w") as temp_file:
    print tempname
    temp_file.write(file_contents)
    print(file_contents)

    pdb.plug_in_wr_curves(img, drawable, tempname, run_mode = RUN_NONINTERACTIVE)

register(
  "color-match",
  "Color match (BG to FG)",
  "Performs a color match on the active layer, changing the BG color to the FG one.",
  "Johannes",
  "(C) 2013",
  "12/29/2013",
  "<Image>/Colors/Color match",
  "*",
  [],
  [],
  color_match
)

main()
