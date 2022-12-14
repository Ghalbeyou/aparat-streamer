# imports
from asyncio import sleep
import asyncio
import json
import os
from vidgear.gears import CamGear
from vidgear.gears import WriteGear
import cv2
import colorama

# Loads config
with open('config.json', 'r') as f:
    CONFIG = json.load(fp=f)
    VIDEO_SOURCE = CONFIG["stream_video_location"] # video source
    VIDOE_STREAM_KEY = CONFIG["stream_key"] # stream key
async def main():
    print(colorama.Fore.GREEN + "Streamer by " + colorama.Style.DIM + "GHALBEYOU\n" + colorama.Style.RESET_ALL + colorama.Fore.GREEN + "GitHub.com/ghalbeyou\n\n              Loading ...")
    await sleep(5)
    os.system("cls")
    # Open stream
    stream = CamGear(source=VIDEO_SOURCE, logging=True).start()

    # define required FFmpeg optimizing parameters for your writer
    # [NOTE]: Added VIDEO_SOURCE as audio-source
    # [WARNING]: VIDEO_SOURCE must contain audio
    output_params = {
        "-i": VIDEO_SOURCE,
        "-acodec": "aac",
        "-ar": 44100,
        "-b:a": 712000,
        "-vcodec": "libx264",
        "-preset": "medium",
        "-b:v": "4500k",
        "-bufsize": "512k",
        "-pix_fmt": "yuv420p",
        "-f": "flv",
    }

    # [WARNING]: Change your YouTube-Live Stream Key here:

    # Define writer with defined parameters and
    writer = WriteGear(
        output_filename="rtmp://rtmp.cdn.asset.aparat.com:443/event/{}".format(VIDOE_STREAM_KEY),
        logging=True,
        **output_params
    )

    # loop over
    while True:

        # read frames from stream
        frame = stream.read()

        # check for frame if Nonetype
        if frame is None:
            break

        # {do something with the frame here}

        # write frame to writer
        writer.write(frame)

    # safely close video stream
    stream.stop()

    # safely close writer
    writer.close()


if __name__ == '__main__':
    asyncio.run(main=main())