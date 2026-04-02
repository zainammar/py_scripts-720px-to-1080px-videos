import os
import subprocess

input_folder = "input_videos"
output_folder = "output_videos"

# Create output folder if not exists
# only add 720px in input folder, and the output will be 1080px
os.makedirs(output_folder, exist_ok=True)

# Supported video formats
video_extensions = (".mp4", ".avi", ".mov", ".mkv")
git status
for filename in os.listdir(input_folder):
    if filename.lower().endswith(video_extensions):
        
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"1080_{filename}")

        print(f"Processing: {filename}")

        # FFmpeg command
        command = [
            "ffmpeg",
            "-i", input_path,
            "-vf", "scale=1920:1080",
            "-c:a", "copy",
            output_path
        ]

        subprocess.run(command)

print("✅ All videos converted successfully!")