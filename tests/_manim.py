# -*- coding: utf-8 -*-
import os
from pathlib import Path

import manimpango


def markup_to_svg_test(markup_str: str, file_name: str = "test.svg", **kwargs):
    dir_name = Path(file_name).parent
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    width = 600
    height = 400
    return manimpango.markup_to_svg(markup_str, file_name, width, height, **kwargs)
