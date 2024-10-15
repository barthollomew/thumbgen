import os
from thumbgen.pptx_util import create_thumbnail_from_template

def process_video_thumbnails(input_file, template_path, output_dir, change_text_box_name):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        video_name = line.strip()
        print(f"Generating thumbnail for: {video_name}")

        thumbnail_path = create_thumbnail_from_template(template_path, output_dir, video_name, change_text_box_name)
        if thumbnail_path:
            print(f"Thumbnail for '{video_name}' saved to: {thumbnail_path}")
        else:
            print(f"Failed to create thumbnail for '{video_name}'.")
