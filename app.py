from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)
# У хмарному демо використовуємо список у пам'яті для швидкості розгортання
team_tasks = []

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Командний планувальник</title>
    <style>
        body { font-family: sans-serif; margin: 40px; background-color: #f4f4f9; }
        .container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        input, button { padding: 10px; margin: 5px 0; width: 95%; }
        button { background-color: #28a745; color: white; border: none; cursor: pointer; }
        li { padding: 8px; border-bottom: 1px solid #ddd; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Хмарний командний планувальник завдань</h2>
        <form action="/add" method="POST">
            <input type="text" name="user" placeholder="Ваше ім'я" required>
            <input type="text" name="task" placeholder="Що потрібно зробити?" required>
            <button type="submit">Додати завдання</button>
        </form>
        <h3>Поточні завдання команди:</h3>
        <ul>
            {% for t in tasks %}
                <li><b>{{ t.user }}</b>: {{ t.task }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE, tasks=team_tasks)

@app.route('/add', methods=['POST'])
def add():
    user = request.form.get('user')
    task = request.form.get('task')
    if user and task:
        team_tasks.append({'user': user, 'task': task})
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)