import os
import json

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def main():
    tasks = load_tasks()
    while True:
        print("\n--- Список справ ---")
        for idx, task in enumerate(tasks, start=1):
            status = "[✓]" if task['completed'] else "[ ]"
            print(f"{idx}. {status} {task['title']}")

        print("\n1. Додати завдання | 2. Виконати | 3. Вийти")
        choice = input("Оберіть дію: ")

        if choice == '1':
            title = input("Назва завдання: ")
            tasks.append({"title": title, "completed": False})
            save_tasks(tasks)
        elif choice == '2':
            task_num = int(input("Номер виконаного завдання: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]['completed'] = True
                save_tasks(tasks)
        elif choice == '3':
            break


if __name__ == "__main__":
    main()