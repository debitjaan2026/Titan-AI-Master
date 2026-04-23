import os
import re
import random
from datetime import datetime

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text).strip('-')
    return text[:80]

def create_page(title, content):
    os.makedirs("pages", exist_ok=True)
    slug = slugify(title)
    filename = f"{slug}.html"
    path = f"pages/{filename}"
    
    # তোমার দেওয়া দুটি লিঙ্ক এখানে রোটেশন হবে
    links = [
        "https://www.profitablecpmratenetwork.com/ud2qw6p3d7?key=275a836a0d6ce5c21562f245c57cdf1a",
        "https://www.profitablecpmratenetwork.com/zaa9nppna?key=e42ebc0a997943ef4b244903273e1743"
    ]
    TARGET_URL = random.choice(links)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
    body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f0f2f5; margin: 0; padding: 15px; color: #1c1e21; }}
    .container {{ max-width: 650px; margin: 20px auto; background: white; padding: 25px; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.15); }}
    h1 {{ color: #1877f2; font-size: 24px; line-height: 1.2; }}
    .content {{ font-size: 16px; line-height: 1.6; color: #4b4f56; margin-top: 20px; }}
    .cta {{ text-align: center; margin-top: 35px; border-top: 1px solid #ddd; padding-top: 20px; }}
    .btn {{ background: linear-gradient(to bottom, #4267b2, #365899); color: white; padding: 16px 32px; border: none; border-radius: 6px; font-size: 18px; font-weight: bold; cursor: pointer; text-decoration: none; display: inline-block; width: 80%; }}
    .progress-box {{ display: none; margin-top: 25px; }}
    .progress-text {{ font-weight: bold; color: #fa3e3e; }}
    .progress-bar {{ width: 100%; background: #ddd; height: 12px; border-radius: 6px; margin-top: 10px; overflow: hidden; }}
    .progress {{ width: 0%; height: 100%; background: #42b72a; transition: width 1s linear; }}
</style>
</head>
<body>
<div class="container">
    <h1>{title}</h1>
    <p style="color: #90949c; font-size: 13px;">📅 Last Updated: {datetime.now().strftime("%B %d, %Y")}</p>
    <div class="content">{content}</div>
    <div class="cta">
        <button class="btn" onclick="startLoading()">🚀 CONTINUE TO FULL ARTICLE</button>
        <div class="progress-box" id="pbox">
            <p class="progress-text">Checking for safety... <span id="timer">5</span>s</p>
            <div class="progress-bar"><div class="progress" id="pbar"></div></div>
        </div>
    </div>
</div>
<script>
function startLoading() {{
    document.getElementById('pbox').style.display = 'block';
    let timeLeft = 5;
    let width = 0;
    const interval = setInterval(() => {{
        timeLeft--;
        width += 20;
        document.getElementById('timer').innerText = timeLeft;
        document.getElementById('pbar').style.width = width + '%';
        if(timeLeft <= 0) {{
            clearInterval(interval);
            window.location.href = "{TARGET_URL}";
        }}
    }}, 1000);
}}
</script>
</body>
</html>"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path
