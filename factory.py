import os
import random

# তোমার অ্যাড লিঙ্কগুলো
AD_LINKS = [
    "https://www.profitablecpmratenetwork.com/ud2qw6p3d7?key=275a836a0d6ce5c21562f245c57cdf1a",
    "https://www.profitablecpmratenetwork.com/zaa9nppna?key=e42ebc0a997943ef4b244903273e1743"
]

def create_landing_page(trend_name):
    if not os.path.exists('pages'):
        os.makedirs('pages')
    
    # র্যান্ডমলি একটি লিঙ্ক সিলেক্ট করা
    target_link = random.choice(AD_LINKS)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{trend_name} - Exclusive Content</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #0f0f0f; color: white; text-align: center; padding: 50px; }}
            .container {{ border: 2px solid #e50914; padding: 20px; border-radius: 10px; display: inline-block; }}
            .btn {{ background-color: #e50914; color: white; padding: 15px 30px; text-decoration: none; font-size: 20px; border-radius: 5px; font-weight: bold; display: inline-block; margin-top: 20px; }}
            .btn:hover {{ background-color: #ff0f1f; }}
            img {{ max-width: 100%; border-radius: 10px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Trending: {trend_name}</h1>
            <p>Click below to Watch or Download the latest viral content!</p>
            <a href="{target_link}" class="btn">WATCH / DOWNLOAD NOW</a>
        </div>
    </body>
    </html>
    """
    
    with open('pages/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Landing page created for: {trend_name}")

if __name__ == "__main__":
    create_landing_page("Latest Viral Movie Clip")
