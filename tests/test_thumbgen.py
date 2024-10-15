import unittest
import os
from thumbgen.generator import process_video_thumbnails
from thumbgen.pptx_util import create_thumbnail_from_template
from thumbgen.pdf_util import convert_pptx_to_png

class TestThumbGen(unittest.TestCase):
    
    def setUp(self):
        """Set up test environment: create a temporary output directory"""
        self.output_dir = './test_output'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        self.template_path = 'test_template.pptx'  # You should create a simple test PPTX file
        self.text_box_name = 'Change here'
        self.video_name = 'Test Video'
        self.input_file = 'test_video_list.txt'  # A test file with video names

        # Write test video names to input file
        with open(self.input_file, 'w') as f:
            f.write(self.video_name + '\n')

    def tearDown(self):
        """Clean up test environment: remove temporary files"""
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, file))
            os.rmdir(self.output_dir)

        if os.path.exists(self.input_file):
            os.remove(self.input_file)

    def test_create_thumbnail_from_template(self):
        """Test thumbnail creation from a PowerPoint template"""
        thumbnail_path = create_thumbnail_from_template(self.template_path, self.output_dir, self.video_name, self.text_box_name)
        self.assertTrue(os.path.exists(thumbnail_path), "Thumbnail should be generated and saved.")

    def test_convert_pptx_to_png(self):
        """Test the conversion from PPTX to PNG using LibreOffice and PDF"""
        pptx_path = 'test_slide.pptx'  # Create a basic test slide for testing
        with open(pptx_path, 'w') as f:
            f.write('This is a test slide.')
        
        png_path = convert_pptx_to_png(pptx_path, self.output_dir, self.video_name)
        self.assertTrue(os.path.exists(png_path), "PNG should be created from the PPTX.")

        # Clean up the test slide
        if os.path.exists(pptx_path):
            os.remove(pptx_path)

    def test_process_video_thumbnails(self):
        """Test the main video thumbnail processing function"""
        process_video_thumbnails(self.input_file, self.template_path, self.output_dir, self.text_box_name)
        thumbnail_files = os.listdir(self.output_dir)
        self.assertTrue(len(thumbnail_files) > 0, "At least one thumbnail should be generated.")

if __name__ == '__main__':
    unittest.main()
