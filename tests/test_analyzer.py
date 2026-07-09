from core.analyzer import Analyzer

url = input("Paste a YouTube URL: ")

video = Analyzer().analyze(url)

print("\nVideo information")
print("-" * 40)
print(f"Title      : {video.title}")
print(f"Uploader   : {video.uploader}")
print(f"Duration   : {video.duration} seconds")
print(f"Upload Date: {video.upload_date}")
print(f"Thumbnail  : {video.thumbnail}")
print(f"URL        : {video.webpage_url}")