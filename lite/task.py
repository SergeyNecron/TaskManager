# Задача: Создай класс `Task`, который позволяет управлять задачами (делами). 
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). 
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        """
        Инициализация задачи.

        :param description: Описание задачи
        :param deadline: Срок выполнения задачи
        """
        self.description = description
        self.deadline = deadline
        self.is_done = False

    def mark_as_done(self):
        # Отметить задачу как выполненную.
        self.is_done = True

    def __str__(self):
        # Возвращает строковое представление задачи.
        status = "Выполнено" if self.is_done else "Не выполнено"
        return f"{self.description} (Срок: {self.deadline}, Статус: {status})"
