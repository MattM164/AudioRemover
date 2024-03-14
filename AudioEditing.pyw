from moviepy.editor import VideoFileClip

def remove_audio(input_video, output_video):
    video = VideoFileClip(input_video)
    video_without_audio = video.set_audio(None)
    video_without_audio.write_videofile(output_video, codec='libx264', audio_codec='aac')

#input_video = 'input_video.mp4'
#output_video = 'output_video_without_audio.mp4'

#remove_audio(input_video, output_video)