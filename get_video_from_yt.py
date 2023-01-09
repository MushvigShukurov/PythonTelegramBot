from pytube import YouTube

def download_mp4(link,process_path,video_name):
    YouTube(link).streams.first().download(output_path=process_path+"/videos/",filename=video_name)