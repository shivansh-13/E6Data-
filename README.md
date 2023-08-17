# Text Analysis Toolkit

The Text Analysis Toolkit is a Python script designed to process and analyze text data from multiple files within a specified directory. It provides various functions to perform tasks such as counting total files, total words, distinct words, and finding the top words with their frequencies.

## How to run

In the correct directory, run the following command:

```bash 
./run.sh
```

## Architecture

The script is organized into several functions, each serving a specific purpose:

1. `process_file(file_path)`: Tokenizes the content of a given file, converting it to lowercase and splitting it into words.
2. `total_file_count(directory)`: Counts the total number of files in the specified directory with the `.txt` extension.
3. `total_word_count(directory)`: Counts the total number of words across all `.txt` files in the directory using multiprocessing for parallel processing.
4. `total_distinct_word_count(directory)`: Counts the total number of distinct words across all `.txt` files using multiprocessing.
5. `top_words_with_frequencies(directory, n=100)`: Finds the top `n` words with their frequencies in the `.txt` files using multiprocessing.
6. `execute_commandX(directory)`: Executes specific commands (1-4) on the directory, measuring the time taken for execution.
7. `execute_task(task)`: Executes a given command on the directory, measuring the time taken, and returns the result along with the execution time.

The main control flow of the program is in the `if __name__ == '__main__':` block. It reads user input to determine the command to execute and the target directory. It then delegates the execution to the corresponding `execute_commandX` function, printing the result and execution time.

## Prerequisites

- Python 3.x
- Required packages: `multiprocessing`, `collections`, `functools`, `time`

## Usage

1. Clone the repository or download the script.
2. Install the required packages if not already installed
3. Run the script: `python text_analysis_toolkit.py`
4. Follow the on-screen instructions to choose a command and provide a directory path.

## Example

Suppose you have a directory named `text_data` containing several `.txt` files. Running the script and selecting various commands will provide insights such as total file count, total word count, distinct word count, and top words with frequencies, along with the time taken for each operation.

## Note

- The script uses multiprocessing for improved performance in tasks like word counting and distinct word counting. However, the overhead of creating and managing processes may result in slower performance for smaller datasets. Therefore, the script uses a threshold value of 1000 files to determine whether to use multiprocessing or not. This value can be changed in the `execute_command2` and `execute_command3` functions.


