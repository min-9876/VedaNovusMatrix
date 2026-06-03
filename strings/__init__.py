import os
import yaml
from typing import List

languages = {}
languages_present = {}

def get_string(lang: str):
    return languages.get(lang, languages["en"])

# path ကို လွယ်ကူအောင် ပြင်ရေးထားပါတယ်
lang_path = "./strings/langs/"

# 'en.yml' ကို အရင်ဆုံးသေချာအောင် load လုပ်ပါ
en_file = os.path.join(lang_path, "en.yml")
if os.path.exists(en_file):
    with open(en_file, encoding="utf8") as f:
        languages["en"] = yaml.safe_load(f) or {}
    languages_present["en"] = languages["en"].get("name", "English")
else:
    print("Error: en.yml not found!")
    exit()

# တခြား language ဖိုင်များကို loop ပတ်ပါ
for filename in os.listdir(lang_path):
    if filename.endswith(".yml") and filename != "en.yml":
        language_name = filename[:-4]
        file_full_path = os.path.join(lang_path, filename)
        
        with open(file_full_path, encoding="utf8") as f:
            data = yaml.safe_load(f)
            
            # ဖိုင်က None ဖြစ်နေရင် (အလွတ်ဖြစ်နေရင်) အလွတ် dict အဖြစ် ပြောင်းပေးပါ
            languages[language_name] = data if data else {}
            
        # အဓိကပြင်ဆင်ချက် - 'en' ထဲမှာရှိတာတွေကို လိုအပ်ရင် ဖြည့်ပေးခြင်း
        for item, value in languages["en"].items():
            if item not in languages[language_name]:
                languages[language_name][item] = value
                
        languages_present[language_name] = languages[language_name].get("name", language_name)
