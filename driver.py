import sys
import concurrent.futures
from engine import execute_command1, execute_command2, execute_command3, execute_command4

# ... (other imports and functions)

def execute_task(task):
    cmd, directory, _ = task
    if cmd == 1:
        return execute_command1(directory)
    elif cmd == 2:
        return execute_command2(directory)
    elif cmd == 3:
        return execute_command3(directory)
    elif cmd == 4:
        return execute_command4(directory)

def main():
    if len(sys.argv) != 2:
        print("Usage: python driver.py input.txt")
        return

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        directory = f.readline().strip()
        commands = list(map(int, f.readline().strip().split()))

    tasks = [(cmd, directory, None) for cmd in commands]

    results = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(execute_task, tasks))

    for result in results:
        print(result)

if __name__ == '__main__':
    main()
