# Import necessary modules
from asyncio import sleep
import asyncio
import json
import os
from vidgear.gears import CamGear
from vidgear.gears import WriteGear
import cv2
import colorama

# Load configuration from config.json file
with open('config.json', 'r') as f:
    CONFIG = json.load(fp=f)
VIDEO_SOURCE = CONFIG["stream_video_location"] # video source
VIDOE_STREAM_KEY = CONFIG["stream_key"] # stream key

async def main():
    """
    Main function for streaming video using VidGear library.

    This function reads video frames from the specified video source, applies any necessary processing or manipulation
    to the frames, and then writes the frames to the specified output location using VidGear's WriteGear module.

    Returns:
        None
    """

    print(colorama.Fore.GREEN + "Streamer by " + colorama.Style.DIM + "GHALBEYOU\n" + colorama.Style.RESET_ALL + colorama.Fore.GREEN + "GitHub.com/ghalbeyou\n\n              Loading ...")
    await sleep(5)
    os.system("cls")

    # Open video stream
    stream = CamGear(source=VIDEO_SOURCE, logging=True).start()

    # Define required FFmpeg optimizing parameters for the writer
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

    # [WARNING]: Change your Aparat Stream Key here:
    # Define writer with defined parameters and stream key
    writer = WriteGear(
        output_filename="rtmp://rtmp.cdn.asset.aparat.com:443/event/{}".format(VIDOE_STREAM_KEY),
        logging=True,
        **output_params
    )

    # Loop to continuously read and write frames
    while True:

        # Read frames from video stream
        frame = stream.read()

        # Check for NoneType frames
        if frame is None:
            break


        # Write frame to writer
        writer.write(frame)

    # Safely close video stream
    stream.stop()

    # Safely close writer
    writer.close()


if __name__ == '__main__':
    # Run the main function using asyncio
    asyncio.run(main=main())
