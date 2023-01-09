import moviepy.editor
import os

def get_audio(video_name,video_name_without_ext,BASE_DIR):
    audios_dir_path = os.path.join(BASE_DIR,"audios")
    if os.path.isdir(audios_dir_path) == False:
        os.mkdir(audios_dir_path)
    try:
        video = os.path.join(BASE_DIR,"videos",video_name)
        video = moviepy.editor.VideoFileClip(video)
        audio = video.audio
        audio_file_name = os.path.join(BASE_DIR,"audios",video_name_without_ext + ".mp3") 
        audio.write_audiofile(audio_file_name)
        data = {
            "ok":True,
            "audio":audio_file_name
        }
        return data
    except:
        data = {
            "ok":True,
        }
        return data


