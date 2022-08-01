def create_youtube_video(title,description):
	 return {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments" : {}}


	def like(youtube video) :
		if 'likes' in video:
			youtube_video["likes"]+= 1
			return youtube_video


	def deslike(youtube video) :
		if 'dislikes' in video:
			youtube_video["dislikes"]+=1
			return youtube_video

	def addComment(youtube video, username, comment):
    youtube_video["comments"][username] = comment
    return 


    function= create_youtube_video()
    for i in range(495):
    	like(function)
