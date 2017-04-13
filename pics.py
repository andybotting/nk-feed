import auth
from instagram.client import InstagramAPI

def pics(limit=4):

    api = InstagramAPI(access_token=auth.INSTAGRAM_ACCESS_TOKEN,
                       client_secret=auth.INSTAGRAM_CLIENT_SECRET)

    recent_media, _next = api.user_recent_media(user_id='6204130', count=10)

    # Only include images, no videos
    images = [p for p in recent_media if p.type == 'image']
    images.sort(key=lambda p: p.created_time, reverse=True)

    return images[:limit]
