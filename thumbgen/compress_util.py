# thumbgen/compress_util.py

import os
import tempfile
import shutil
from PIL import Image

# 3 MB threshold
MAX_SIZE = 3 * 1024 * 1024

# try progressively fewer colors
COLOR_LEVELS = [256, 128, 64, 32, 16, 8, 4, 2]


def compress_image(file_path: str):
    """
    If the PNG at file_path is > MAX_SIZE, quantize+optimize
    until it falls under the limit.
    """
    orig = os.path.getsize(file_path)
    if orig <= MAX_SIZE:
        return

    img = Image.open(file_path)
    for colors in COLOR_LEVELS:
        # create a palettized, optimized temp PNG
        pal = img.convert("P", palette=Image.ADAPTIVE, colors=colors)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            tmp_path = tmp.name
        pal.save(tmp_path, optimize=True, compress_level=9)

        new_size = os.path.getsize(tmp_path)
        if new_size <= MAX_SIZE:
            shutil.move(tmp_path, file_path)
            print(f"↳ compressed to {new_size//1024} KB")
            return
        os.remove(tmp_path)

    print(f"⚠️  could not get {file_path} under {MAX_SIZE//(1024*1024)} MB")
