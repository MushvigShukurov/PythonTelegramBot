import os 
import telebot
import time
from get_audio_from_videos import get_audio
from get_video_from_yt import download_mp4
from tokens import my_tokens
from tkinter.filedialog import *
from get_random_file_name import get_random_name
from save_link_to_links import write_link
BASE_DIR = os.getcwd()
bot = telebot.TeleBot(my_tokens.get("token"), parse_mode=None) 




def get_mp3(link):  
    if write_link(link) == False:
        print("Evvelce yuklenmisdi !")
        return False
    video_name_without_ext = get_random_name(20)
    video_name = video_name_without_ext + ".mp4"
    download_mp4(link,BASE_DIR,video_name)
    is_okay = get_audio(video_name,video_name_without_ext,BASE_DIR)
    if(is_okay.get("ok")):
        return is_okay.get("audio")
    else:
        print("Xəta baş verdi!")

link = "https://youtu.be/gvDK35FM980?list=RDCEK9JDeOjLk"


@bot.message_handler(commands=['start'])
def start(m,res=False):
	bot.send_message(m.chat.id, "Zəhmət olmasa youtube video linkini göndərin!")

@bot.message_handler(content_types=['text', 'audio'])
def handle_text(m,res=False):
    bot.send_message(m.chat.id,"15 saniyə sonra mp3 göndəriləcək")
    audio = open(get_mp3(m.text.strip()),"rb")
    time.sleep(15)
    bot.send_audio(m.chat.id, audio=audio)

bot.polling(non_stop=True, interval=0)