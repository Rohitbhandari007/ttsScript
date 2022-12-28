from gtts import gTTS
import os

# Prompt the user for the input and output file names
input_file_name = input("Enter the input file name (text): ")
output_file_name = input("Enter the output file name (audio):")

# Construct the full input file name

input_folder = "text"
output_folder = "output"


input_file_path = os.path.join(input_folder, input_file_name + ".txt")
output_file_path = os.path.join(output_folder, output_file_name + ".mp3")


# Open the text file and read the contents
with open(input_file_path, "r") as f:
    text = f.read()

# Convert the text to speech with fast playback
tts = gTTS(text, slow=False)

print("Please wait......")
# Save the audio to an MP3 file

tts.save(output_file_path)

print("Your file has been succesfully converted, check your output folder. ")
