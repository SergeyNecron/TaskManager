# Пример использования
from task_manager import TaskManager

task_manager = TaskManager()

while True:
    print("\n1. Добавить задачу")
    print("2. Отметить задачу как выполненную")
    print("3. Вывести текущие задачи")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        description = input("Введите описание задачи: ")
        deadline = input("Введите срок выполнения задачи: ")
        task_manager.add_task(description, deadline)
    elif choice == "2":
        task_index = int(input("Введите индекс задачи: ")) - 1
        task_manager.mark_task_as_done(task_index)
    elif choice == "3":
        task_manager.print_current_tasks()
    elif choice == "4":
        break
    else:
        print("Неправильный выбор. Пожалуйста, выберите действие из списка.")