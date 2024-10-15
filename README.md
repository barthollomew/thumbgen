# ThumbGen

ThumbGen is a tool for **quickly bulk-generating images/thumbnails from a PowerPoint slide**.

## Installation

First, clone the repository and navigate to the project directory. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Usage

To generate thumbnails from a PowerPoint template, use the following command:

```bash
thumbgen --input_file video_links.txt --template_path template.pptx --output_dir ./thumbnails --text_box_name "Change here"
```

### Arguments:
- `--input_file`: Path to the input file containing video names (one per line).
- `--template_path`: Path to the PowerPoint `.pptx` template file.
- `--output_dir`: Directory where the generated thumbnails will be saved.
- `--text_box_name`: The name or text in the text box to be replaced in the PowerPoint template.

## Example

Suppose you have a text file `video_links.txt` containing the following:

```txt
Video Title 1
Video Title 2
Video Title 3
```

And a PowerPoint template `template.pptx` where you want to replace the text box labeled "Change here" with each of these video titles.

Run the command:

```bash
thumbgen --input_file video_links.txt --template_path template.pptx --output_dir ./thumbnails --text_box_name "Change here"
```

This will generate thumbnails in the `./thumbnails` directory, with each video title replacing the specified text box in the PowerPoint slide.

MIT License