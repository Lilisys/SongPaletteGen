from flask import *
import requests 
import json
import os 
from watson_developer_cloud import ToneAnalyzerV3Beta


tone_analyzer = ToneAnalyzerV3Beta( 
    username='719c30fd-054f-4221-a00c-911f3461825f', 
    password='0dMvFyNX5qJu', 
    version='2016-05-19')


main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
    #this dictionary stores any info you wanna pass from python to html
    #i.e. list of songs
    options = {}

    options['name'] = "dania"
    options['result'] = ""
    options['resulted'] = ""

    options['songs'] = ["blank space", "shake it off"]

    return render_template("index.html", **options)

@main.route('/', methods=['POST'])
def main_route_form():
    options = {}
    title1 = request.form['song-title1']
    artist1 = request.form['artist1']
    processed_text1 = title1.upper()
    processed_artist1 = artist1.upper()

    title2 = request.form['song-title2']
    artist2 = request.form['artist2']
    processed_text2 = title2.upper()
    processed_artist2 = artist2.upper()

    title3 = request.form['song-title3']
    artist3 = request.form['artist3']
    processed_text3 = title3.upper()
    processed_artist3 = artist3.upper()
# track.search?q_track=back%20to%20december&q_artist=taylor%20swift&f_has_lyrics=1
    # r = requests.get('http://api.musixmatch.com/ws/1.1/track.search?apikey=f316db2a6a195b45a7ca85d622055158&q_track=back%20to%december&q_artist=taylor%20swift&f_has_lyrics=1')
                                          

    r = requests.get('http://api.musixmatch.com/ws/1.1/track.search?apikey=f316db2a6a195b45a7ca85d622055158&q_track='+title1+'&q_artist='+artist1+'=1')                                           
    # r = requests.get('http://api.musixmatch.com/ws/1.1/track.search?apikey=f316db2a6a195b45a7ca85d622055158&q_artist=queen&q_track=we%20are%20the%20champions&format=json&page_size=1&f_has_lyrics=1')
    result = json.loads(r.text)
    options['result'] = result
    print result
    if len(result["message"]["body"]["track_list"]) == 0: 
        print "NOOOOOO"
        return "NOOOOO"
    #return render_template("index.html", **options)
    j = 0
    for i in result["message"]["body"]["track_list"]:
        if j == 0: 
            trackid1 = i["track"]["track_id"]
            j += 1
        if j == 1: 
            trackidjust_in_case = i["track"]["track_id"] 

        # print "iiiiii"
        #print i["track"]["track_name"] 

        # print i["track"]["track_id"] 
        # print i["track"]["track_mbid"]
    print "iiiii" 
    print trackid1
    theid = requests.get('http://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey=f316db2a6a195b45a7ca85d622055158&track_id='+str(trackid1))                                           
    
    print "asdfasdfsf"
    print theid
    resulted = json.loads(theid.text)
   # print resulted["message"]["body"]["lyrics"]["lyrics_body"]
    lyrics = resulted["message"]["body"]["lyrics"]["lyrics_body"]
    lyrics = ' '.join(lyrics.split('\n'))
    lyrics = lyrics.strip('.')
    print "DID WE STRIP", lyrics
    lyrics = lyrics.strip('\"')
    print lyrics
    lyrics = lyrics.split('*')[0]
    

    print "length: ", len(lyrics), lyrics
    if len(lyrics) == 0: 
            theid = requests.get('http://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey=f316db2a6a195b45a7ca85d622055158&track_id='+str(trackidjust_in_case))                                           
            resulted = json.loads(theid.text)
            lyrics = resulted["message"]["body"]["lyrics"]["lyrics_body"]

            lyrics = lyrics.strip('.')
            lyrics = lyrics.strip('"')
            print "DID WE STRIP", lyrics
            lyrics = lyrics.split('*')[0]
            lyrics = ' '.join(lyrics.split('\n'))

    print lyrics
   


    print "~~~~~~~~~~~~~~~~~~"
    stuff = os.system('curl -u "719c30fd-054f-4221-a00c-911f3461825f":"0dMvFyNX5qJu" -H "Content-Type: application/json" \
        -d \"{\\"text\\": \\"%s\\"}\" \
        "https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-19"  > outfile' % lyrics)
    print "!~!~!~!~!~!~!~!~!~"
    f = open('outfile', 'r')
    #print 'f: ', f
    scores = json.loads(f.read())
    #print "scores: ", scores
    
    toneMap = {}
    m = 0; 
    for i in scores['document_tone']['tone_categories']: 
        if m >= 5: 
            break
        for j in i['tones']:
            m = m+1;
            toneMap[j['tone_name']] = j['score']
            print j['tone_name'] + ' : ' + str(j['score'])
            if m >= 5: 
                break

    print toneMap
   
    return processed_text1 + ' ' + processed_artist1 + processed_text2 + processed_artist2 + processed_text3 + processed_artist3










