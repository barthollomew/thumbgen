import os
import tempfile
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Pt
from thumbgen.pdf_util import convert_pptx_to_png


def create_thumbnail_from_template(
    template_path,
    output_dir,
    video_name,
    change_text_box_name,
    text_color="white",
    font_size=16,
):
    try:
        safe_video_name = "".join(
            c for c in video_name if c.isalnum() or c in (" ", "_", "-")
        ).rstrip()
        prs = Presentation(template_path)
        slide = prs.slides[0]

        # Convert text color
        rgb = (
            RGBColor(255, 255, 255)
            if text_color.lower() == "white"
            else RGBColor(0, 0, 0)
        )
        font_size_pt = Pt(font_size)

        dynamic_text_box = None
        for shape in slide.shapes:
            if shape.has_text_frame and change_text_box_name in shape.text:
                dynamic_text_box = shape
                break

        if not dynamic_text_box:
            print(
                f"Error: Could not find the '{change_text_box_name}' text box on the slide for '{video_name}'."
            )
            return None

        dynamic_text_box.text = video_name
        for paragraph in dynamic_text_box.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.color.rgb = rgb
                run.font.size = font_size_pt

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with tempfile.NamedTemporaryFile(
            delete=False, suffix=".pptx", dir=output_dir
        ) as tmp_pptx_file:
            temp_pptx_path = tmp_pptx_file.name
        prs.save(temp_pptx_path)
        prs = None

        thumbnail_path = convert_pptx_to_png(
            temp_pptx_path, output_dir, safe_video_name
        )
        return thumbnail_path
    except Exception as e:
        print(f"Exception occurred while processing '{video_name}': {e}")
        return None
