from __future__ import print_function
import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print ("Error\n")
	print ("Usage: $>python video_get_stats.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]

ziggeo = Ziggeo(api_token, private_key)

print (ziggeo.videos().get_stats(video_token))
