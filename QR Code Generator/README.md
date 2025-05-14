## QR Code Reader & Generator App

A simple Python app to create and scan QR codes — right from your command line!
Built for quick access, easy customization, and lightweight usage.

### Features ✨

🔍 Read QR Codes from image files (.png, .jpg, etc.)

✏️ Create QR Codes with custom size, color, and output name

🖼️ Terminal QR preview (optional) using termimage on supported systems

### Requirements ⚙️

Install the required Python libraries:
```
pip install pyzbar pillow segno
```
Optional (for QR preview in terminal):
```
pkg install termimage
```
### How To Use ▶️

Run the script:
```
python QR_Code_Generator.py
```

#### 1️⃣ Read QR Code

- 📸 Enter the path to an image with a QR code

- ✅ Displays the decoded text or URL

#### 2️⃣ Create QR Code

- 📝 Enter the data you want to encode

- 🖼️ Choose filename, scale (size), foreground & background colors

- 💾 Saves the QR code as a PNG file

- 🧪 Optional: preview it in your terminal if termimage is installed

### Screenshots 📸
<img src="https://github.com/rasel-ml/rasel-ml/blob/main/Screenshots/qr_ss1.png" alt="Screenshot1" width="100%"></img>
<br/><br/>
<img src="https://github.com/rasel-ml/rasel-ml/blob/main/Screenshots/qr_ss2.png" alt="Screenshot2" width="100%"></img>

### Notes 🗒️

- Make sure your image path is correct.

- All dependencies must be installed for full functionality.

- Terminal preview is optional and supported on compatible Linux terminals.

### Author ✍️
Developed by **[Md. Rasel Molla](https://github.com/rasel-ml)**


### 📄 License
This project is open-source and free for educational use.
