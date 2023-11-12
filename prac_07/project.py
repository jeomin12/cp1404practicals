from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def update(self, new_percentage=None, new_priority=None):
        if new_percentage is not None:
            self.completion_percentage = new_percentage
        if new_priority is not None:
            self.priority = new_priority

    def is_complete(self):
        return self.completion_percentage == 100

    @classmethod
    def from_string(cls, project_string):
        project_data = project_string.strip().split('\t')
        if len(project_data) != 5:
            raise ValueError("Incorrect number of fields in project string.")
        return cls(*project_data)
