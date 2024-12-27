from task import Task

class TaskManager:
    def __init__(self):
        """
        Инициализация менеджера задач.
        """
        self.tasks = []

    def add_task(self, description, deadline):
        """
        Добавить новую задачу.

        :param description: Описание задачи
        :param deadline: Срок выполнения задачи
        """
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_done(self, task_index):
        """
        Отметить задачу как выполненную.

        :param task_index: Индекс задачи в списке
        """
        try:
            self.tasks[task_index].mark_as_done()
        except IndexError:
            print("Задача с таким индексом не существует.")

    def print_current_tasks(self):
        # Вывести список текущих (не выполненных) задач.
        current_tasks = [task for task in self.tasks if not task.is_done]
        if current_tasks:
            print("Текущие задачи:")
            for i, task in enumerate(current_tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Нет текущих задач.")