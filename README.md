# GPT-SoVITS Automated script

The script utilizes the Selenium library in Python to automate the process of entering text, clicking the synthesis button, and downloading the audio files on the GPT-SoVITS interface. This enables batch generation of speech and saving it locally.

## How to Use

![Inference interface](image.png)

### Step Zero
Run the script, and once the webpage loads, manually upload your reference audio and the corresponding text.

### Step One
Prepare to synthesize the speech file, for example using **千秋诗颂_zh.txt**, and place it in the directory where the script is located. 
(The program will automatically read the file and input the text into the input box.)

### Step Two
(The program automatically clicks the **synthesize speech** button and waits for the synthesis to complete.)

### Step Three
Create a folder on the local computer. Take **E:\vedio_generated\\** * as an example to save the synthesized voice file to this folder.
(The program automatically downloads the synthesized voice file and saves it to the directory where the script resides.)

### Step Four
After the script runs, close the browser window.