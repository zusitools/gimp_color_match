#!/usr/bin/env python

from gimpfu import *
import os

def color_match(img, drawable):
  tempname = pdb.gimp_temp_name("curve")
  fgcolor = pdb.gimp_context_get_foreground()
  bgcolor = pdb.gimp_context_get_background()

  samples = " ".join(map(lambda x: "{:.5f}".format(x/255.0), range(0,256)))
  points_unused = "-1.0 -1.0" * 14

  print bgcolor
  print fgcolor

  file_contents = """
    # GIMP curves tools settings
    (time 0)
    (channel red)
    (curve
      (curve-type smooth)
      (n-points 17)
      (points 34 0.0 0.0 {} {:.4f} {:.4f} 1.0 1.0)
      (n-samples 256)
      (samples 256 {})
    )
    (channel green)
    (curve
      (curve-type smooth)
      (n-points 17)
      (points 34 0.0 0.0 {} {:.4f} {:.4f} 1.0 1.0)
      (n-samples 256)
      (samples 256 {})
    )
    (channel blue)
    (curve
      (curve-type smooth)
      (n-points 17)
      (points 34 0.0 0.0 {} {:.4f} {:.4f} 1.0 1.0)
      (n-samples 256)
      (samples 256 {}) 
    )
  """.format(
    points_unused, bgcolor[0] / 255.0, fgcolor[0] / 255.0, samples,
    points_unused, bgcolor[1] / 255.0, fgcolor[1] / 255.0, samples,
    points_unused, bgcolor[2] / 255.0, fgcolor[2] / 255.0, samples,
  )

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
