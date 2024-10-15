import os
import subprocess
from pdf2image import convert_from_path

def convert_pptx_to_png(pptx_path, output_dir, safe_video_name):
    cmd = [
        'libreoffice',
        '--headless',
        '--convert-to',
        'pdf',
        pptx_path,
        '--outdir',
        output_dir
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0 or not os.path.exists(os.path.splitext(pptx_path)[0] + ".pdf"):
        print(f"LibreOffice conversion to PDF failed for '{safe_video_name}'.")
        return None

    temp_pdf_path = os.path.splitext(pptx_path)[0] + ".pdf"
    pages = convert_from_path(temp_pdf_path, dpi=300)
    thumbnail_path = os.path.join(output_dir, f"{safe_video_name}.png")
    pages[0].save(thumbnail_path, 'PNG')

    os.remove(pptx_path)
    os.remove(temp_pdf_path)

    return thumbnail_path
