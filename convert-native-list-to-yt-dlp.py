import re

#This script converts a file with episodes, series and links to yt-dlp commands that are download ready and executable

def clean_string(string):
    return string.replace(' ', '-').replace('.', '').replace(',', '').replace('!', '').replace('%', '')\
        .replace(':','').replace('@', '').replace('?', '').replace('=', '').replace('+', '').replace('*', '')\
        .replace('/', '-').replace("&", ' ').replace("{", '(').replace("}", ')').replace("<", '(').replace("\"", '')\
        .replace(">", ')').replace("*", '').replace("$", '').replace("\'", '').replace("\\", '').replace("`", '')\
        .replace("|", '').replace("\n", '')

def get_season_number(string):
    m = re.search(r'\d+$', string)
    return int(m.group()) if m else None

def get_episode_number(string):
    m = re.search(r'\d+', string)
    return int(m.group()) if m else None

with open("dirty-list.txt", 'r', encoding='utf-8') as file:
    initial_text = file.readlines()
season = None
episode = None
title = None
link = None

test_previous_number = None
test_conter = 0

test_previous_number_ep = None
test_conter_ep = 0
output = open("download-list.txt", "a+", encoding="utf-8")
prev_link = None

for line in initial_text:
    # check for a season of current object
    if line.startswith("			SEZON") or line.startswith("				SEZON") or line.startswith(
            "					SEZON") or line.startswith("				    SEZON"):
        season = (get_season_number(line))
        # test
        if (test_conter > 0) and (test_previous_number + 1 != season):
            print("error")
        test_conter += 1
        test_previous_number = season
        # endtest
    # check for episode and title of current object
    if line[0].isdigit():
        episode = get_episode_number(line)
        # test
        if (test_conter_ep > 0) and (test_previous_number_ep + 1 != episode):
            print("error")
        test_conter_ep += 1
        test_previous_number_ep = episode
        # endtest
        title = clean_string(line.lstrip('0123456789.'))
    # check for file link
    if line.startswith("	http://"):
        link = line.rstrip('\n')[1:]
        #print(link)
    # combine and add to a list
    if link and prev_link != link:
        output_string = ("yt-dlp " + "-o " "\""+"S"+str(season)+"E"+str(episode)+title+".%(ext)s\" " + '\"' + link + '\"' + "\n")
        output.write(output_string)
        prev_link = link
output.close()