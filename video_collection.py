from googleapiclient.discovery import build

# create a YouTube API client
api_key = 'your_api_key_here'
youtube = build('youtube', 'v3', developerKey=api_key)

# search for music videos
query = 'music'
max_results = 1000
videos = []
next_page_token = None

while len(videos) < max_results:
    # make API request
    search_response = youtube.search().list(
        q=query,
        type='video',
        part='id',
        maxResults=min(max_results - len(videos), 50),
        pageToken=next_page_token
    ).execute()
    
    # add video IDs to list
    for search_result in search_response.get('items', []):
        videos.append(search_result['id']['videoId'])
    
    # check if there are more results
    next_page_token = search_response.get('nextPageToken')
    if next_page_token is None:
        break
