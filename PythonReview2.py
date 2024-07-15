def create_youtube_video(title, description):
    Youtube_Video = {"title":title, "description":description, "likes":0, "dislikes":0, "comments":{}}
    return Youtube_Video
    
    
def like(Youtube_Video):
    if "likes" in Youtube_Video:
        Youtube_Video["likes"] += 1
    return Youtube_Video
    
def dislike(Youtube_Video):
    if "dislikes" in Youtube_Video:
        Youtube_Video["dislikes"] += 1
    return Youtube_Video    
    
def add_comment(Youtube_Video, username, comment_text):
     Youtube_Video["comments"][username]=comment_text
     
# Youtube_Video

video = create_youtube_video("Once a king always a king", "Elior Blux opening packs")

add_likes = like(video)


comment = add_comment(video, "ofir", "shit video")
print(comment)

    