# Debian Bullseye ကို အခြေခံထားတဲ့ ပိုမိုသစ်လွင်သော Image သို့ ပြောင်းလဲခြင်း
FROM nikolaik/python-nodejs:python3.11-nodejs20

# apt update လုပ်ရာတွင် ပြဿနာမရှိစေရန် တည်ငြိမ်သော source များသုံးခြင်း
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

# dependencies များကို install လုပ်ခြင်း
RUN pip3 install --no-cache-dir -U -r requirements.txt

# CMD ကိုလည်း အကြံပြုထားတဲ့အတိုင်း shell script သို့မဟုတ် JSON format ဖြင့် သုံးခြင်း
CMD ["bash", "start"]
