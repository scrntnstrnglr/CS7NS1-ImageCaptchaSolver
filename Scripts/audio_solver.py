import speech_recognition
import pydub
import os
import json
pydub.AudioSegment.converter = "C:\\Users\\SIDDHARTHA\\Downloads\\ffmpeg-4.2.1-win64-static\\bin\\ffmpeg.exe"
pydub.AudioSegment.ffmpeg = "C:\\Users\\SIDDHARTHA\\Downloads\\ffmpeg-4.2.1-win64-static\\bin\\ffmpeg.exe"
pydub.AudioSegment.ffprobe = "C:\\Users\\SIDDHARTHA\\Downloads\\ffmpeg-4.2.1-win64-static\\bin\\ffprobe.exe"


def solve_captcha():
    audio_path = 'test.mp3'
    print('HER!!')
  
    if os.path.exists(audio_path):
        sound = pydub.AudioSegment.from_mp3(audio_path)
        sound.export("audio.wav", format="wav")
        print('HER!!')
        AUDIO_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "audio.wav")

        r = speech_recognition.Recognizer()  
        with speech_recognition.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)   
        try:
            text=r.recognize_google(audio,language='en-US',show_all=True)
            response = json.dumps(text, ensure_ascii=False).encode('utf8')
            print(response)
            return text
            #os.remove(audio_path)
            os.remove('audio.wav')
        except speech_recognition.UnknownValueError:
            print("Can not understand audio!")
            try:
                #os.remove(audio_path)
                os.remove('audio.wav')
            except:
                print("Can not delete files.")

        except speech_recognition.RequestError:
            print("No results!")
            try:
                #os.remove(audio_path)
                os.remove('audio.wav')
            except:
                print("Can not delete files.")
    
def main():
    print(solve_captcha())
    
if __name__ == '__main__':
    main()