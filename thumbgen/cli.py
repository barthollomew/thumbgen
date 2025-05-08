import argparse
from thumbgen.generator import process_video_thumbnails


def main():
    parser = argparse.ArgumentParser(
        description="Generate thumbnails for videos using a PowerPoint template."
    )

    parser.add_argument(
        "--input_file",
        type=str,
        required=True,
        help="Path to the input file containing video names.",
    )
    parser.add_argument(
        "--template_path",
        type=str,
        required=True,
        help="Path to the PowerPoint (.pptx) template file.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        required=True,
        help="Directory where thumbnails will be saved.",
    )
    parser.add_argument(
        "--text_box_name",
        type=str,
        required=True,
        help="The name or text in the text box to be replaced in the template.",
    )

    # Optional flags
    parser.add_argument(
        "--text_color",
        type=str,
        choices=["white", "black"],
        default="white",
        help="Text color: white or black (default: white)",
    )
    parser.add_argument(
        "--font_size", type=int, default=16, help="Font size in points (default: 16)"
    )

    args = parser.parse_args()

    process_video_thumbnails(
        args.input_file,
        args.template_path,
        args.output_dir,
        args.text_box_name,
        text_color=args.text_color,
        font_size=args.font_size,
    )


if __name__ == "__main__":
    main()
