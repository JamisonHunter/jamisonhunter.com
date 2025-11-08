from flask import Flask, render_template
import markdown
import re

def parse_markdown(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        first_line = text.split('\n', 1)[0]
        title = first_line.lstrip('# ').strip()
    html_content = markdown.markdown(text, extensions=['fenced_code'])
    return html_content, title

def html_to_description(html, max_chars=160):
    text = re.sub(r'<[^>]+>', '', html)
    text = text.replace('&nbsp;', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) <= max_chars:
        return text
    truncated = text[:max_chars].rsplit(' ', 1)[0]
    if not truncated:
        truncated = text[:max_chars]
    return truncated.rstrip() + '...'

app = Flask(__name__, static_folder='static')

# Create a new route when adding a blog post.

@app.route("/")
def index():
    try:
        html_content, title = parse_markdown('./posts/index.md')
        description = html_to_description(html_content, max_chars=160)
        return render_template("index.html", text=html_content, title=title, description=description)
    except Exception as e:
        return render_template("error.html", error=str(e))

@app.route("/benchmarking-programming-languages-with-math")
def benchmarking_programming_languages_with_math():
    try:
        html_content, title = parse_markdown('./posts/benchmarking-programming-languages-with-math.md')
        description = html_to_description(html_content, max_chars=160)
        return render_template('index.html', text=html_content, title=title, description=description)
    except Exception as e:
        return render_template("error.html", error=str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)