import os

def generate_html():
    folders = ['deepseek', 'claude']
    links_html = ""

    for folder in folders:
        if not os.path.exists(folder):
            continue
            
        # フォルダ内の .html ファイルを取得してソート
        files = sorted([f for f in os.listdir(folder) if f.endswith('.html')])
        
        color_class = folder # cssクラス名として使用
        icon = "🤖" if folder == "deepseek" else "🎨"
        description = "DeepSeek Logic Generations" if folder == "deepseek" else "Claude UI/UX Generations"

        links_html += f"""
    <div class="card {color_class}">
        <h2><span>{icon}</span> {folder.capitalize()}</h2>
        <p class="description">{description}</p>
        <div class="version-list">"""
        
        for file in files:
            version_name = file.replace('.html', '')
            links_html += f'\n            <a href="{folder}/{file}" class="v-btn">{version_name} <span>HTML</span></a>'
            
        links_html += """
        </div>
    </div>"""

    # HTML全体のテンプレート
    template = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI for AI - Auto Hub</title>
    <style>
        :root {{ --bg: #0f172a; --card-bg: #1e293b; --text-main: #f1f5f9; --text-dim: #94a3b8; --deepseek-color: #3b82f6; --claude-color: #f97316; }}
        body {{ font-family: sans-serif; background-color: var(--bg); color: var(--text-main); display: flex; flex-direction: column; align-items: center; padding: 40px 20px; }}
        h1 {{ font-size: 2.5rem; background: linear-gradient(to right, #60a5fa, #fb923c); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .container {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px; width: 100%; max-width: 900px; }}
        .card {{ background: var(--card-bg); border-radius: 16px; padding: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.1); }}
        .card.deepseek h2 {{ color: var(--deepseek-color); }}
        .card.claude h2 {{ color: var(--claude-color); }}
        .description {{ color: var(--text-dim); font-size: 0.95rem; margin-bottom: 25px; }}
        .version-list {{ display: flex; flex-direction: column; gap: 12px; }}
        .v-btn {{ display: flex; justify-content: space-between; align-items: center; padding: 12px 20px; background: rgba(255,255,255,0.05); border-radius: 8px; text-decoration: none; color: var(--text-main); transition: all 0.2s; }}
        .v-btn:hover {{ background: rgba(255,255,255,0.15); transform: translateX(5px); }}
        .v-btn span {{ font-size: 0.8rem; background: rgba(0,0,0,0.3); padding: 2px 8px; border-radius: 4px; color: var(--text-dim); }}
    </style>
</head>
<body>
    <header><h1>AI for AI Project</h1></header>
    <div class="container">
        {links_html}
    </div>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(template)

if __name__ == "__main__":
    generate_html()
