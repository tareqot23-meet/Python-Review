def create_youtube_video(title,description):
	 return {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments" : {}}


	def like(youtube video) :
		youtube_video["likes"]+= 1
		return youtube_video


	def deslike(youtube video) :
		youtube_video["dislikes"]+=1
		return youtube_video

	def addComment(youtube video, username, comment):
    youtube_video["comments"][username] = comment
    return youtube_video
