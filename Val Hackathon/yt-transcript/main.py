from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

formatter = TextFormatter()

f = open('./Val Hackathon/yt-transcript/links-champions.txt', 'r')
text = f.read()
links = text.split(',\n')

count = 0

for v in links:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(v[32:])

        text_formatted = formatter.format_transcript(transcript)

        with open(f'./Val Hackathon/yt-transcript/trans-champ{count}.txt', 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_formatted)

        count += 1
    except:
        print('failed to retrieve subtitles')