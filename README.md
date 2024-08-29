# Video Downloader

This script automates the process of downloading videos from specific URLs using authentication cookies and `yt-dlp`. The videos are automatically downloaded into a `downloads` directory.

## Setup

1. **Install dependencies:**

   Ensure you have `yt-dlp`, `requests`, and `beautifulsoup4` installed.

   ```bash
   pip install yt-dlp requests beautifulsoup4
   ```

2. **Obtain cookies:**

   Log in to your account via a web browser and export the cookies as `cookies.json`.

3. **Prepare your video links:**

   Create a text file `video_links.txt` with alternating lines of video titles and URLs.

## Usage

1. Run the script:

   ```bash
   python dall.py
   ```

2. The videos will be downloaded into the `downloads` folder.

## Directory Structure

```
.
├── cookies.json
├── cookies.txt
├── dall.py
├── video_links.txt
└── downloads
    └── <downloaded videos>.mp4
```

## License

This project is licensed under the MIT License.
