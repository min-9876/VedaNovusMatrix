# 📡 Part of VedaNovus Matrix 

# 🎵 VedaNovus- The Ultimate Telegram Music Bot

<p align="center">
  <img src="" alt="TusharMusic Logo" width="1280" height="720">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/SudarshanTushar/VedaNovusMatrix?style=for-the-badge&color=blue" alt="GitHub stars">
  <img src="https://img.shields.io/github/forks/SudarshanTushar/VedaNovusMatrix?style=for-the-badge&color=blue" alt="GitHub forks">
  <img src="https://img.shields.io/github/issues/SudarshanTushar/VedaNovusMatrix?style=for-the-badge&color=red" alt="GitHub issues">
  <img src="https://img.shields.io/github/license/SudarshanTushar/VedaNovusMatrix?style=for-the-badge&color=green" alt="GitHub license">

</p>

## 🚀 About TusharMusic 
TusharMusic is a high-performance Telegram music bot that streams music in voice chats with premium-quality audio. It supports multiple streaming sources like **YouTube, Spotify, Apple Music**, and more! Optimized with **Docker & GitHub Actions**, it ensures smooth deployment and operation.

## ✨ Features
✅ **Multi-Source Streaming** – Play music from YouTube, Spotify, SoundCloud, and more.
✅ **Queue System** – Add multiple tracks and enjoy seamless playback.
✅ **Interactive Controls** – Pause, resume, skip, or stop music anytime.
✅ **Crystal-Clear Audio** – Enjoy high-fidelity sound in your voice chat.
✅ **Persistent AFK Mode** – Stay online even when you're inactive.
✅ **Inline Help & Admin Commands** – Easy-to-use bot commands with interactive buttons.
✅ **Customizable Settings** – Adjust volume, equalizer, and other playback options.

## 🔥 Fix for YouTube Blocking VPS IPs
If YouTube blocks your VPS IP, follow these steps to bypass restrictions:
1. **Join our Support Group** – Type `#script` in our [support group](https://t.me/LovelyAppeal) to get the required script.
2. **Generate Cookies** – Run the script on your Windows PC using VS Code or another software.
3. **Fork the Repository** – Fork this repo to your GitHub account.
4. **Upload Cookies** – Place the generated cookies inside the `cookies` folder.
5. **Deploy the Bot** – Follow the deployment guide below.

---

## 🚀 Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/SudarshanTushar/VedaNovusMatrix)

---

## 🛠 Installation Guide
Follow these steps to set up and run NetflixMusic:

### 1️⃣ Update System Packages
```bash
sudo apt-get update && sudo apt-get upgrade -y
```

### 2️⃣ Install Dependencies
```bash
sudo apt-get install python3-pip ffmpeg -y
```

### 3️⃣ Setup PIP
```bash
sudo pip3 install -U pip
```

### 4️⃣ Install Node.js
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash && source ~/.bashrc && nvm install v18
```

### 5️⃣ Clone the Repository
```bash
git clone https://github.com/SudarshanTushar/VedaNovusMatrix && cd TusharMusic
```

### 6️⃣ Install Required Python Packages
```bash
pip3 install -U -r requirements.txt
```

### 7️⃣ Configure Environment Variables
```bash
cp sample.env .env
vi .env  # Edit your credentials
```
To edit:
- Press `I` to start editing.
- Modify values as needed.
- Press `Esc`, type `:wq`, then press `Enter` to save.

### 8️⃣ Install tmux (Optional but Recommended)
```bash
sudo apt install tmux -y && tmux
```

### 9️⃣ Run the Bot
```bash
bash start
```

---

## 📜 Commands & Usage
| Command              | Description                                      |
|----------------------|--------------------------------------------------|
| `/play <song name>`  | Play a song by name or link.                    |
| `/pause`             | Pause the current track.                         |
| `/resume`           | Resume the paused song.                          |
| `/skip`             | Skip to the next song in the queue.              |
| `/stop`             | Stop music playback and clear the queue.         |
| `/queue`            | View the current song queue.                     |
| `/help`             | Show the list of available commands.              |

For a full command list, use `/help` in [Telegram](https://t.me/Netflix_Musicbot).

---

## 🔄 Stay Updated
<p align="center">
  <a href="https://t.me/LovelyAppeal">
    <img src="https://img.shields.io/badge/Join-Support%20Group-blue?style=for-the-badge&logo=telegram">
  </a>
  <a href="https://telegram.me/AboutVedmat">
    <img src="https://img.shields.io/badge/Join-Update%20Channel-blue?style=for-the-badge&logo=telegram">
  </a>
</p>

---

## 🤝 Contribute to TusharMusic 
We welcome contributions from the community! To contribute:
1. **Fork** this repository.
2. **Create a feature branch** for your updates.
3. **Make your changes** and commit with a clear message.
4. **Submit a pull request** to our `master` branch.
5. Our team will review and merge your contributions.

For queries, reach out to us on [Telegram](https://t.me/LovelyAppeal).

---

## 📜 License
TusharMusic is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

💙 **Enjoy your ultimate music experience with TusharMusic!** 🚀
