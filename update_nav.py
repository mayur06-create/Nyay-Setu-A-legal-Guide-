import re

files = ['index.html', 'directory.html', 'news.html']
links = [
    ('Explore Issues', '#', False),
    ('Guide', 'index.html', False),
    ('Directory', 'directory.html', False),
    ('News', 'news.html', False),
    ('RTI Generator', '#', False),
    ('AI Analysis', '#', False)
]

def generate_nav(active_name):
    html = ['<div class="nav-links">']
    for name, href, _ in links:
        cls = ' class="active"' if name == active_name else ''
        html.append(f'                    <a href="{href}"{cls}>{name}</a>')
    html.append('                </div>')
    return '\\n'.join(html)

def update_file(filename, active_name):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # regex to replace `<div class="nav-links">...</div>` block
    pattern = re.compile(r'<div class="nav-links">.*?</div>', re.DOTALL)
    
    new_nav = generate_nav(active_name)
    
    new_content = pattern.sub(new_nav, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {filename}")

update_file('index.html', 'Guide')
update_file('directory.html', 'Directory')
update_file('news.html', 'News')
