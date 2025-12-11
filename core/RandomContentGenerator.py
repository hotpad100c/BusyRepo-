import requests
def fetch_random_word():
    lang = random.choice(['zh', 'en'])
    try:
        r = requests.get(f"https://random-word-api.herokuapp.com/word?lang={lang}", timeout=10)
        if r.status_code == 200:
            data = r.json()
            if data and len(data) > 0:
                return data[0]
    except Exception:
        pass
    
    return "Ohhnagg III failed whygssjl"
    
def fetch_random_text():
    try:
        r = requests.get("https://api.quotable.io/random", timeout=10)
        if r.status_code == 200:
            data = r.json()
            return f"{data['content']—— {data['author']}"
    except Exception:
        pass
    
    try:
        r = requests.get("https://zenquotes.io/api/random", timeout=10)
        if r.status_code == 200:
            data = r.json()[0]
            return f"{data['q']} —— {data['a']}"
    except Exception:
        pass
    
    try:
        r = requests.get("https://api.adviceslip.com/advice", timeout=10)
        if r.status_code == 200:
            data = r.json()
            return f""{data['slip']['advice']}"
    except Exception:
        pass
    
    return "OOoAaa I faild i fell so sad i am bad."
