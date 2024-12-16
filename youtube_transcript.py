from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re


def get_video_id(url):
    # Remove any query parameters (e.g., ?si=...)
    url = url.split('?')[0]
    
    # Check if it's a full YouTube URL or a shortened one
    if "youtu.be" in url:
        # For shortened URLs like youtu.be
        return url.split("/")[-1]
    elif "youtube.com" in url:
        # For full URLs like youtube.com/watch?v=VIDEO_ID
        match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
        if match:
            return match.group(1)
    return None


def get_transcript(video_url):
    video_id=get_video_id(video_url)

    if not video_id:
        return 'Error: Invalid youtube url or video id cannot etracted.'
    
    try:
        transcript=YouTubeTranscriptApi.get_transcript(video_id)

        formatter=TextFormatter()
        transcript_text=formatter.format_transcript(transcript)

        return transcript_text
    except Exception as e:
        return f"Error: {str(e)}"
    
# Input the YouTube video link
video_url = input("Enter YouTube video link: ")
transcript = get_transcript(video_url)
print("\nTranscript of the video:\n")
print(transcript)