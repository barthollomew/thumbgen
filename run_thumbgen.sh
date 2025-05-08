#!/bin/bash

# 1. Activate virtualenv
source venv/bin/activate

# 2. Add LibreOffice to PATH if not already present
export PATH="/Applications/LibreOffice.app/Contents/MacOS:$PATH"

# 3. Install package in editable mode (safe to re-run)
pip install -e .

# 4. Run thumbgen with sample/default values
thumbgen \
  --input_file video_links.txt \
  --template_path template.pptx \
  --output_dir thumbnails \
  --text_box_name "Change here"
