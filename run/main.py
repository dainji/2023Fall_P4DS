import yaml
import subprocess


def execute_tasks(task_list):
    for task in task_list:
        print(f"Executing {task['name']}...")
        commands = task.get('commands')
        if commands:
            for command in commands:
                subprocess.run(command.split(), check=True)


def main():
    # Load tasks from the YAML file
    with open('/Users/dain/PycharmProjects/Fall_2023/2023Fall_P4DS/run/task.yaml', 'r') as file:
        tasks = yaml.safe_load(file)

    # Execute tasks
    execute_tasks(tasks.get('tasks', []))


if __name__ == "__main__":
    main()
