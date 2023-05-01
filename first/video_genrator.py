from .image_genrator import img_create
from moviepy.editor import *
import itertools
from django.conf import settings
from PIL import ImageFont
from moviepy.video.tools.drawing import *
# Load the video

def GenrateVideo(video, logo,  text, profile, user_name, output_file):
    clip = VideoFileClip(video)
#     text="हमारे संवाददाता नैंसी मिश्रा एक रिपोर्ट न्यूज़ रूम से kaif"

    img_create(text)
    # Resize the video to add a white border of 20 pixels
    clip = clip.resize(width=clip.w+40, height=clip.h+40)
    # Add a watermark to the video
    watermark = (ImageClip(logo)
                .set_duration(clip.duration)
                .set_position(('left', 'top')))
    '''Add user profile to the video'''
    usrprofile = (ImageClip(profile)
                .set_duration(clip.duration)
                .set_position(('right', 'top')))
    '''Add user name to the video'''
    usrname=(TextClip(user_name, font="TiroDevanagariHindi-Regular.ttf",
                    fontsize=50, color='black').set_position(('right', 200))
            .set_duration(clip.duration))
    '''Add text image to the video'''
    test_image = (ImageClip(str(settings.BASE_DIR)+"/media/images/hinditext/hindi_text.png")
                .set_duration(clip.duration)
                .set_position(('right', 'buttom'))
                )


    #adding line 
    frame = (ImageClip('media/images/hinditext/line_new.png')
            .resize(width=clip.w-1)
            .set_duration(clip.duration)
            .set_position(('center', 'center')))

    text_clips = []
    for i in range(10):
        # Set the start and end times of the text clip
        text_clip = test_image.set_start(i * 2).set_end((i + 1) * 2)
        # Use itertools.cycle to create an infinite iterator that repeats the x-position
        x_pos = itertools.cycle(range(clip.w, -text_clip.w, -10))
        def x(t): return (next(x_pos), 'bottom')
        text_clip = text_clip.set_position(x)
        text_clips.append(text_clip)
    final_clip = CompositeVideoClip([clip,watermark,usrname,usrprofile,frame]+text_clips)
    # Write the output video file
    final_clip.write_videofile(output_file)

