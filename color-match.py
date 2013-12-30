#!/usr/bin/env python

from gimpfu import *
import os

def color_match(img, drawable):
  fgcolor = pdb.gimp_context_get_foreground()
  bgcolor = pdb.gimp_context_get_background()

  try:
    pdb.gimp_image_undo_group_start(img)
    for (index, channel) in [(0, HISTOGRAM_RED), (1, HISTOGRAM_GREEN), (2, HISTOGRAM_BLUE)]:
      print bgcolor[index], fgcolor[index]
      pdb.gimp_curves_spline(drawable, channel, 6, [0, 0, bgcolor[index], fgcolor[index], 255, 255])
  finally:
    pdb.gimp_image_undo_group_end(img)

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
