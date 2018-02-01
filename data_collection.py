from imutils.video import VideoStream
from PIL import Image
import os
import time
import argparse


def collect_specific_hand(character_wanted, name):
    vs = VideoStream().start() #start up the video stream
    if os.path.exists("hand/%s" % character_wanted): #if you don't have a file for the character you specified, it'll be created
        pass
    else:
        os.makedirs("hand/%s" % character_wanted)
    print("Starting data collection for character", character_wanted, "in 5 seconds, get ready...")
    time.sleep(3)
    print("Collecting now!")
    num_of_images = 50
    while True and num_of_images != 0:
        num_of_images = num_of_images - 1
        frame = vs.read()
        im = Image.fromarray(frame)
        im.save("hand/%s/%s.jpg" % (character_wanted, name + str(num_of_images)))

    print("Done!")

def collect_not_hand():
    vs = VideoStream().start()
    print("Starting data collection for non-hands in 5 seconds, get ready...")
    time.sleep(3)
    print("Collecting now!")
    num_of_images = 500
    while True and num_of_images != 0:
        num_of_images = num_of_images - 1
        frame = vs.read()
        im = Image.fromarray(frame)
        im.save("not_hand/%s.jpg" % (num_of_images))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--character", required=True,
                    help="Character Wanted, type 'None' if you're making negative images")
    ap.add_argument("-n", "--name", required=True,
                    help="Your name, used to save file.")
    args = vars(ap.parse_args())
    if args["character"] == 'None':
        collect_not_hand()
    else:
        collect_specific_hand(args["character"].lower(), args["name"].lower())

