# GPT-SoVITS Automated script

The script utilizes the Selenium library in Python to automate the process of entering text, clicking the synthesis button, and downloading the audio files on the GPT-SoVITS interface. This enables batch generation of speech and saving it locally.

## How to Use

![推理界面](image.png)

### Step Zero
运行该脚本，待网页打开后，手动上传你的参考录音和对应的文本。

### Step One
准备合成语音文件，以 **千秋诗颂_zh.txt** 为例，将其放到脚本所在目录下。
（程序自动读取该文件，并将其中的文本输入到输入框中。）

### Step Two
（程序自动点击 **合成语音** 按钮，并等待合成完成。）

### Step Three
在本地电脑建立文件夹，以 **E:\vedio_generated\\** 为例，将合成的语音文件保存到该文件夹。
(程序自动下载合成的语音文件，并保存到脚本所在目录下。)

### Step Four
脚本运行结束，关闭浏览器窗口。