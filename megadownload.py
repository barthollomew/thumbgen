import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import subprocess

# Function to extract video URL from browser logs
def extract_video_url_selenium_logs(embed_url, driver_path):
    # Set up Chrome options to enable logging
    options = Options()
    options.add_argument('--enable-logging')
    options.add_argument('--v=1')
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    
    # Initialize Selenium WebDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # Load the page
    driver.get(embed_url)

    # Wait for the page to fully load (adjust this as necessary)
    time.sleep(2)

    # Initialize the variable to store the video URL
    video_url = None

    # Extract performance logs
    logs = driver.get_log('performance')

    # Iterate over the performance logs
    for log in logs:
        message = log['message']
        if '.mp4' in message and '206' in message:
            video_url = message.split('"url":"')[1].split('"')[0]
            break

    # Close the browser
    driver.quit()

    return video_url

# Function to download video using yt-dlp
def download_video(video_url, video_name):
    # Ensure the downloads directory exists
    if not os.path.exists('./downloads'):
        os.makedirs('./downloads')
    
    # Construct the yt-dlp command to download the video
    download_path = os.path.join('./downloads', f"{video_name}.mp4")
    command = ['yt-dlp', video_url, '-o', download_path]
    
    # Run the yt-dlp command
    subprocess.run(command, check=True)

# Main function to read the video_links.txt file and download videos
def process_video_links(file_path, driver_path):
    # Open the file and read the lines
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Process lines in pairs (name, url)
    for i in range(0, len(lines), 2):
        video_name = lines[i].strip()  # Video name
        embed_url = lines[i + 1].strip()  # Embed URL
        
        print(f"Processing {video_name} - {embed_url}")
        
        # Extract the video URL using Selenium
        video_url = extract_video_url_selenium_logs(embed_url, driver_path)

        if video_url:
            print(f"Found video URL: {video_url}")
            # Download the video using yt-dlp
            download_video(video_url, video_name)
            print(f"Downloaded {video_name} to ./downloads/")
        else:
            print(f"Video URL not found for {video_name}")

# Example usage
if __name__ == "__main__":
    file_path = 'video_links.txt'  # Path to your video_links.txt file
    driver_path = '/usr/local/bin/chromedriver'  # Path to your chromedriver

    process_video_links(file_path, driver_path)
