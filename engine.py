# Import necessary libraries
import os
import multiprocessing
from collections import Counter
from functools import partial
import time

# Define function to process a file and return its content as a list of lowercase words
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return content.lower().split()

# Calculate the total count of files with '.txt' extension in a directory
def total_file_count(directory):
    return len([file for file in os.listdir(directory) if file.endswith('.txt')])

# Calculate the total word count across all files in a directory using multiprocessing
def total_word_count(directory):
    files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.txt')]
    with multiprocessing.Pool() as pool:
        word_lists = pool.map(process_file, files)
    return sum(len(words) for words in word_lists)

# Calculate the total count of distinct words across all files in a directory using multiprocessing
def total_distinct_word_count(directory):
    files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.txt')]
    with multiprocessing.Pool() as pool:
        word_lists = pool.map(process_file, files)
    all_words = [word for words in word_lists for word in words]
    return len(set(all_words))

# Calculate the top 'n' words with their frequencies across all files in a directory using multiprocessing
def top_words_with_frequencies(directory, n=100):
    files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.txt')]
    with multiprocessing.Pool() as pool:
        word_lists = pool.map(process_file, files)
    all_words = [word for words in word_lists for word in words]
    word_freq = Counter(all_words)
    top_words = word_freq.most_common(n)
    return top_words

# Execute command to get the total file count and measure the execution time
def execute_command1(directory):
    start_time = time.time()
    result = str(total_file_count(directory))
    end_time = time.time()
    time_taken = int((end_time - start_time) * 1000)  # Convert to milliseconds
    return f"{result} {time_taken}"

# Execute command to get the total word count and measure the execution time
def execute_command2(directory):
    start_time = time.time()
    result = str(total_word_count(directory))
    end_time = time.time()
    time_taken = int((end_time - start_time) * 1000)  # Convert to milliseconds
    return f"{result} {time_taken}"

# Execute command to get the total distinct word count and measure the execution time
def execute_command3(directory):
    start_time = time.time()
    result =  str(total_distinct_word_count(directory))
    end_time = time.time()
    time_taken = int((end_time - start_time) * 1000)  # Convert to milliseconds
    return f"{result} {time_taken}"

# Execute command to get the top 'n' words with frequencies and measure the execution time
def execute_command4(directory, n=100):
    start_time = time.time()
    top_words = top_words_with_frequencies(directory, n)
    end_time = time.time()
    result = " ".join([f"{word} {freq}" for word, freq in top_words])
    time_taken = int((end_time - start_time) * 1000)  # Convert to milliseconds
    return f"{result} {time_taken}"

# Execute a given task (command) on a specified directory
def execute_task(task):
    command, directory, arg = task
    if command == 1:
        result = execute_command1(directory)
    elif command == 2:
        result = execute_command2(directory)
    elif command == 3:
        result = execute_command3(directory)
    elif command == 4:
        result = execute_command4(directory)
    return f"{result}"

# Main program execution
if __name__ == '__main__':
    # ... (same as before)
    pass
