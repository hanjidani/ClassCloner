import requests
import zipfile
import os
#from pydub import AudioSegment

def pagecloner(url):
    url = url.replace("?proto=true", "")
    url = url + "output/content.zip?download=zip"
    print("downloading")
    con = requests.get(url, allow_redirects=True)
    print("downloaded")
    open("content.zip", "wb").write(con.content)

def extract(file):
    print("unzipping")
    with zipfile.ZipFile(file, "r") as zip_ref:
        zip_ref.extractall("output")
    print("unziped")

def refactorfiles(file_list):
    audios = []
    videos = []
    for file in file_list:
        if ".flv" in file:
            if "camera" in file:
                audios.append(file)
            if "screen" in file:
                videos.append(file)
    return audios, videos
#def Audio(audios):
#    finalaudio = AudioSegment.empty()
 #   for audio in audios:
  #      print(audio)
   #     au = AudioSegment.from_flv("output/" + audio)
    #    finalaudio.append(au)
   # AudioSegment.export(finalaudio)

if __name__ == '__main__':
     url = input("Please enter the URL : ")
     pagecloner(url)
     extract("content.zip")
    # a,v = refactorfiles(os.listdir("output"))
    # Audio(a)
    # print(os.listdir("output"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
