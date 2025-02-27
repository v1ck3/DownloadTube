import yt_dlp
import pyfiglet
import time

# Print tool header with ASCII art for "DownloadTube"
def print_banner():
    result = pyfiglet.figlet_format("DownloadTube", font="standard")  # You can change "slant" to other fonts like "standard"
    print(result)
    print("Downloading started")
    print("Copyright - MR SUDO (since 2022)\n")
    print("<====== ONGOING ======>")
    time.sleep(2)

def download_video(url, download_path='.'):
    try:
        # Define options for downloading the video
        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save video with title as filename
            'format': 'bestvideo+bestaudio/best',            # Get the best quality video and audio
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',                # Use FFmpeg for conversion
                'preferedformat': 'mp4',                     # Convert to mp4
            }],
        }

        # Create the YoutubeDL object with the specified options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {url}")
            ydl.download([url])
            print(f"Download complete! Video saved to: {download_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def show_available_qualities(url):
    try:
        # Define options for extracting available formats without downloading
        ydl_opts = {
            'quiet': True,
            'format': 'bestvideo+bestaudio/best',  # Only retrieve available formats
            'extract_flat': True,  # Don't download, just get info
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            
            print(f"Available qualities for video: {info_dict['title']}")
            for format in formats:
                print(f"{format['format_id']} - {format['format_note']} - {format['ext']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print_banner()  # Display the banner when the script starts

    url = input("Enter the YouTube URL or Shorts link: ")
    
    # Optionally show available qualities first
    show_qualities = input("Do you want to see available qualities? (y/n): ")
    if show_qualities.lower() == 'y':
        show_available_qualities(url)
    
    download_path = input("Enter the folder path where you want to save the video (default is current folder): ")
    if not download_path:
        download_path = '.'

    download_video(url, download_path)
