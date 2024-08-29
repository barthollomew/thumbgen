import json
import requests
from bs4 import BeautifulSoup
import yt_dlp
import os

def load_cookies(cookie_file):
    with open(cookie_file, 'r') as file:
        cookie_data = json.load(file)
    cookies = {cookie['name']: cookie['value'] for cookie in cookie_data['cookies']}
    return cookies

def get_final_redirect_url(initial_url, session):
    try:
        response = session.get(initial_url, allow_redirects=True)
        response.raise_for_status()
        return response.url
    except Exception as e:
        print(f"Error following redirects: {e}")
        return None

def get_video_url(video_title, video_url, session):
    try:
        response = session.get(video_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        media_sources = None
        for script in soup.find_all('script'):
            if 'media_sources' in script.text:
                media_sources = script.text
                break
        if media_sources:
            sources = []
            for part in media_sources.split('{'):
                if '"src":' in part and '"bitrate":' in part:
                    try:
                        src_url = part.split('"src":"')[1].split('"')[0].replace("\\", "")
                        bitrate = int(part.split('"bitrate":"')[1].split('"')[0])
                        sources.append((bitrate, src_url))
                    except IndexError:
                        continue
            if sources:
                highest_quality_url = max(sources, key=lambda x: x[0])[1]
                final_url = get_final_redirect_url(highest_quality_url, session)
                if final_url:
                    print(f"Final URL after redirects for {video_title}: {final_url}")
                return final_url
        return None
    except Exception as e:
        print(f"An error occurred while processing {video_title}: {e}")
        return None

def download_video(url, video_title, cookies):
    try:
        download_dir = 'downloads'
        os.makedirs(download_dir, exist_ok=True)
        ydl_opts = {
            'outtmpl': os.path.join(download_dir, f'{video_title}.mp4'),
            'format': 'best',
            'cookies': 'cookies.txt',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Failed to download {video_title}: {e}")

def process_video_links(file_path, session):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    i = 0
    while i < len(lines):
        video_title = lines[i].strip()
        video_url = lines[i+1].strip() if i + 1 < len(lines) else ''
        if video_title and video_url:
            final_video_url = get_video_url(video_title.replace(" ", "_"), video_url, session)
            if final_video_url:
                download_video(final_video_url, video_title.replace(" ", "_"), cookies)
        i += 2

session = requests.Session()
cookies = load_cookies('cookies.json')
session.cookies.update(cookies)
with open('cookies.txt', 'w') as f:
    for name, value in cookies.items():
        f.write(f'{name}\tTRUE\t/\tFALSE\t0\t{name}\t{value}\n')
process_video_links('video_links.txt', session)
