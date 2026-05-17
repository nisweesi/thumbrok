# Thmbnail
## to end up with a functional product (MVP)

1. transcribe, english
2. timestamps
3. Whisper OpenAI
4. JSON and srt
5. JSON Grok -> 5 moments -> 5 moments (via transcription)
6. ffmpeg (assembly) -> (12:13 - 12: 40) -> (13+40)//2= 26
7. Grok 4.3 -> json
8. Grok Imagine -> thumbnails

## create the main business logic

[X] transcripe a video with timestamp using whisper
[X] store the stranscript in txt/srt file
[X] pass it to Grok to get the top 3 moments
4. use ffmpeg to get snippets of these 10 moments (maybe a snipped for every 2 seconds)?
5. pass 2-4 images of every moments to Grok Imagine to get the the thumbnail


## things to implment in the first hour
1. Rest API endpoints to handle the calls between methods
[X] models to validate the requests and responses


## things to implements if passed to the stage after this
1. Rate-limiting
2. Database
3. Queue simulation
