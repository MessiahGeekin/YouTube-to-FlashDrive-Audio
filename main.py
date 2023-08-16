import os
import requests
from pytube import YouTube


def validate_flashdrive(drive):
    for drives in os.listdir("/media"):
        if drive == drives.lower():
            print("Flash Drive Sucessfully Found!")
            return os.path.join("/media", drives)
    return False
        

def check_audio(youtube_link):
    response = requests.get(url = youtube_link)
    if response.status_code == 200:
        return True
    else:
        return False
    

def download_audio(youtube_link, drive):
    youtube = YouTube(youtube_link)
    title  = youtube.title
    stream = youtube.streams.filter(only_audio = True).first()
    stream.download(drive, filename = f"{title}.mp3" )

    print("Download Completed!")


def main():
    os.system("cls" if os.name == "nt" else "clear")
    
    print("MAKE SURE FLASHDRIVE IS PLUGGED IN TO DEVICE".center(os.get_terminal_size().columns))
    drive = input("FlasDrive Name: ")
    if drive:
        while True:
            validate_flashdrive(drive)
            youtube_link = input("Enter youtube url: ")
            if youtube_link:
                if check_audio(youtube_link):
                    download_audio(youtube_link, drive)
                    while True:
                        download_more = input("Would you like to download more (y/n): ").lower()
                        if download_more in ("y","yes"):
                            break
                        elif download_more in ("n","no"):
                            return
                        else:
                            print("Provide a valid value either (y)es or (n)o")

if __name__ == "__main__":
    main()



