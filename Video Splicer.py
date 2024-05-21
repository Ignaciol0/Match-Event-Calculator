from moviepy.video.io.VideoFileClip import VideoFileClip
import json
from GetMatchStats import get_time
import os

def splice_video(match_url,stats):
    match = match_url.split("/")[3]
    with open(f"{match}/{match}_minutes.json","r") as f:
        minutes = json.load(f)
    home_team = match.split("-")[0] #Not right
    away_team = match.split("-")[-1]
    first_time, second_time = get_time(match_url)
    video1 = VideoFileClip(f"{match}/match.mp4")
    video2 = VideoFileClip(f"{match}/match2.mp4")
    time_offset1 = abs(video1.duration/60  -  (int(first_time) + 45))
    time_offset2 = 45 + int(first_time) + 15
    for stat in stats:
        clips = []
        home_index = 1
        away_index = 1
        if os.path.isdir(f"{match}/{stat}Clips") == False:
            os.mkdir(f"{match}/{stat}Clips")
        for minute in minutes[stat]:
            if abs(minute) < (45 + int(first_time)):
                starting_minute = (time_offset1 + abs(minute) - 1.0)
                end_minute = (time_offset1 + abs(minute))
                starting_second = starting_minute * 60
                end_second = end_minute * 60
                clip = video1.subclip(starting_second,end_second)
            else:
                starting_minute = (- time_offset2 + abs(minute) - 1.0) 
                end_minute = (- time_offset2 + abs(minute)) 
                starting_second = starting_minute * 60
                end_second = end_minute * 60
                clip = video2.subclip(starting_second,end_second)
            
            if minute >= 0:
                clip.write_videofile(f"{match}/{stat}Clips/{home_team}{home_index}.mp4",codec="libx264")
                home_index += 1
            else:
                clip.write_videofile(f"{match}/{stat}Clips/{away_team}{away_index}.mp4",codec="libx264")
                away_index += 1
        
splice_video("https://www.sofascore.com/liverpool-aston-villa/PU#id:11352523",["Big chances","Dribbles"])