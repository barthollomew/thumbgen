import os
from thumbgen.pptx_util import create_thumbnail_from_template
from rich.console import Console

# initialize Rich console for styled output
console = Console()


def process_video_thumbnails(
    input_file,
    template_path,
    output_dir,
    change_text_box_name,
    text_color="white",
    font_size=16,
):
    """
    Read video names from input_file, generate thumbnails, and
    display styled console output using Rich.
    """
    # load and clean video names
    with open(input_file, "r") as f:
        video_names = [line.strip() for line in f if line.strip()]

    for video_name in video_names:
        console.print(
            f"[bold yellow]Generating thumbnail for:[/] [cyan]{video_name}[/]"
        )

        thumbnail_path = create_thumbnail_from_template(
            template_path,
            output_dir,
            video_name,
            change_text_box_name,
            text_color,
            font_size,
        )

        if thumbnail_path:
            console.print(
                f"[bold green]✔ Thumbnail saved:[/] [underline]{thumbnail_path}[/]"
            )
        else:
            console.print(
                f"[bold red]✖ Failed to create thumbnail for:[/] [cyan]{video_name}[/]"
            )
