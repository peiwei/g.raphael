#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slimit import minify

inputs = (
    "g.raphael.js",
    "g.bar.js",
    "g.dot.js",
    "g.line.js",
    "g.pie.js",
)

out_dir = "min"

header = """/*!
 * g.Raphael 0.51 - Charting library, based on Raphaël
 *
 * Copyright (c) 2009-2012 Dmitry Baranovskiy (http://g.raphaeljs.com)
 * Licensed under the MIT (http://www.opensource.org/licenses/mit-license.php) license.
 */
"""

for source in inputs:
    target = "%s/%s-min.js" % (out_dir, source[:-3])
    print '(slimit) %s -> %s' % (source, target)
    with open(source) as f:
        compiled = str(header)
        compiled += minify(f.read())

    with open(target, 'w') as f:
        f.write(compiled)
