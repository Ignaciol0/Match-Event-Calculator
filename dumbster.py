from playwright.sync_api import sync_playwright
from time import sleep
from unidecode import unidecode
from datetime import datetime
import threading
import re
import os
import json
# Deprecated for being to heavy for a raspberry pi.
def get_stats(match_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=500)

        page = browser.new_page()
        page.goto(match_url)
        for e in range(3):

            page.keyboard.press("Tab")

        page.keyboard.press("Enter")
        sleep(1)
        index = 0
        minute = 1
        match = match_url.split("/")[3]
        if match not in os.listdir():
            os.mkdir(match)
        for i in range(0,240):
            text = page.locator("//html/body/div[1]/main/div[2]/div[2]/div[1]/div[1]/div[4]/div[2]/div/div[3]/div").all_inner_texts()
           
            with open(f"{match}/stats minute {i+1}.txt",'w') as f:
                try:
                    f.write(text[0])
                except:
                    while True:
                        try:
                            text = page.locator("//html/body/div[1]/main/div[2]/div[2]/div[1]/div[1]/div[4]/div[2]/div/div[3]/div").all_inner_texts()
                            f.write(text[0])
                            break
                        except:
                            sleep(1)
                    
            sleep(30)
# Probably still userfull.
def get_final_stats(match_url):
    match = url.split("/")[3]
    result = {}
    team1_name = match.split("-")[0]
    team2_name = match.split("-")[1]
    result[team1_name] = {}
    result[team2_name] = {}
    minutes = {}
    for minute in range(len(os.listdir(match+'/'))):
        print(f"stats minute {minute+1}.txt")
        with open(f"{match}/stats minute {minute+1}.txt",'r') as f:
            text = f.read().split("\n")
        team1 = {}
        team2 = {}
        for e in range(len(text)//3):
            team1[text[3*e+1]] = text[3*e]
            team2[text[3*e+1]] = text[3*e+2]
        for e in team1.keys():
            try:
                if team1[e] != result[team1_name][e]:
                    minutes.setdefault(e,[])
                    minutes[e] += [int(minute+1)]
                    result[team1_name][e] = team1[e]
                if team2[e] != result[team2_name][e]:
                    minutes.setdefault(e,[])
                    minutes[e] += [-int(minute+1)]
                    result[team2_name][e] = team2[e]
            except:
                result[team1_name][e] = team1[e]
                result[team2_name][e] = team2[e]
    with open(f"{match}_minutes.json","w") as f:
        json.dump(minutes,f)

def get_matches_stats(match_list):
    threads = []
    for match in match_list:
        thread = threading.Thread(target=get_stats, args=(match,))
        thread.start()
        threads += [thread]
    for thread in threads:
        thread.join()

def get_match_urls():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True,slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.sofascore.com/es/")
        sleep(1)
        html = page.locator('//*[@id="pinned-list-fade-target"]').inner_html()
        dates = re.findall(r"\d{2}:\d{2}",html)
        html = ["https://www.sofascore.com"+element.split('"')[0] for element in html.split('/es')[4:] if "#" in element.split('"')[0]]
        match_list = []
        for index in range(len(dates)):
            if datetime.strptime(dates[index], "%H:%M").time() > datetime.now().time() or dates[index] == "21:00":
                match_list += [html[index]]
    with open("urls.txt","r") as f:
        text = f.read()
    if '\n'.join(match_list) not in text:
        text += '\n' + '\n'.join(match_list)
    with open("urls.txt","w") as f:
        f.write(text)
    print("Urls successfully retrieved")
    return match_list
    
#get_matches_stats(["https://www.sofascore.com/valencia-rayo-vallecano/tgbsDgb#id:11368641"])
get_matches_stats(get_match_urls())















urls = ["https://www.sofascore.com/liverpool-uy-palmeiras/nOsEMc#id:12172509",
"https://www.sofascore.com/olympiacos-fc-aston-villa/PsVob#id:12173516",
"https://www.sofascore.com/independiente-del-valle-san-lorenzo/bobsyUp#id:12172501",
"https://www.sofascore.com/fulham-manchester-city/rsT#id:11352529",
"https://www.sofascore.com/liverpool-uy-palmeiras/nOsEMc#id:12172509",
"https://www.sofascore.com/colo-colo-fluminense/lOsfnb#id:12172419",
"https://www.sofascore.com/bournemouth-brentford/abskb#id:11352519",
"https://www.sofascore.com/everton-sheffield-united/psY#id:11352527",
"https://www.sofascore.com/newcastle-united-brighton-and-hove-albion/FsO#id:11352536",
"https://www.sofascore.com/tottenham-hotspur-burnley/gsI#id:11352542",
"https://www.sofascore.com/luton-town-west-ham-united/Msxb#id:11352513",
"https://www.sofascore.com/crystal-palace-wolverhampton/dsh#id:11352516",
"https://www.sofascore.com/las-palmas-mallorca/BgbsCGc#id:11368643",
"https://www.sofascore.com/sevilla-villarreal/ugbsIgb#id:11368644",
"https://www.sofascore.com/granada-real-madrid/EgbsEAn#id:11368634",
"https://www.sofascore.com/athletic-club-osasuna/vgbsAgb#id:11368657",
"https://www.sofascore.com/bayer-04-leverkusen-vfl-bochum-1848/RabsGdb#id:11396184"]