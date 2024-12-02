# ref
https://nerfies.github.io/

# split mp4
ffmpeg -i input.mp4 -ss start_time -t duration -c copy output.mp4

ffmpeg -i ./static/videos/GaussianRoom_720p.mp4 -ss 00:00:00 -t 00:00:46 -c copy ./static/videos/ReconstructionResults_720p.mp4 
ffmpeg -i ./static/videos/GaussianRoom_720p.mp4 -ss 00:00:47 -t 00:02:10 -c copy ./static/videos/ReconstructionComparisons_720p.mp4 
ffmpeg -i ./static/videos/GaussianRoom_720p.mp4 -ss 00:02:10 -t 00:03:31 -c copy ./static/videos/RenderingComparisons_720p.mp4 

ffmpeg -i ./static/videos/ReconstructionComparisons_720p.mp4  -c:v libx264 -preset veryslow -crf 0 -c:a copy ./static/videos/ReconstructionComparisons_720p111.mp4

ffmpeg -i input.mp4 -c:v libx264 -preset slow -crf 23 -c:a copy output.mp4

ffmpeg -i ./static/videos/ReconstructionComparisons_720p.mp4 -c:v libx264 -preset slow -crf 23 -c:a copy ./static/videos/ReconstructionComparisons_720p1.mp4

# slow_down
ffmpeg -i input.mp4 -vf "setpts=2*PTS" output_slow.mp4

ffmpeg -i static\videos\RenderinigComparison_slow\0050.mp4 -vf "setpts=1.5*PTS" static\videos\RenderinigComparison_slow\0050_slow.mp4
ffmpeg -i static\videos\RenderinigComparison_slow\0085.mp4 -vf "setpts=1.5*PTS" static\videos\RenderinigComparison_slow\0085_slow.mp4
ffmpeg -i static\videos\RenderinigComparison_slow\0580.mp4 -vf "setpts=1.5*PTS" static\videos\RenderinigComparison_slow\0580_slow.mp4
ffmpeg -i static\videos\RenderinigComparison_slow\0603.mp4 -vf "setpts=1.5*PTS" static\videos\RenderinigComparison_slow\0603_slow.mp4
ffmpeg -i static\videos\RenderinigComparison_slow\0616.mp4 -vf "setpts=1.5*PTS" static\videos\RenderinigComparison_slow\0616_slow.mp4
ffmpeg -i static\videos\RenderinigComparison_slow\0721.mp4 -vf "setpts=1.5*PTS" static\videos\RenderinigComparison_slow\0721_slow.mp4


# split mp4
ffmpeg -i input.mp4 -ss 00:01:00 -to 00:01:30 -c copy output.mp4



ffmpeg -i static\videos\RenderinigComparison_slow\0085_slow.mp4 -ss 00:00:00 -t 00:00:08 -c copy static\videos\RenderinigComparison_slow\0085_slow_1.mp4 

ffmpeg -i static\videos\RenderinigComparison_slow\0085_slow.mp4 -ss 00:00:00 -to 00:00:08 -c copy static\videos\RenderinigComparison_slow\0085_slow_1.mp4 

ffmpeg -ss 00:00:00 -i static\videos\RenderinigComparison_slow\0085_slow.mp4 -to 00:00:08 -c copy static\videos\RenderinigComparison_slow\0085_slow_1.mp4
