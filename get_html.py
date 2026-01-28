import requests

base_url = 'https://qghuxmu.github.io/Sigma-MoE-Tiny/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15',
}

response = requests.get(url=base_url, headers=headers, timeout=10)
html = response.text

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)