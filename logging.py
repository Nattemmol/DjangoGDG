import logging
def count_words_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            line_count = len(lines)
            return line_count, word_count
    except FileNotFoundError:
        print("File not found.")
        return None, None

file_path = "nati.txt"  
lines, words = count_words_lines(file_path)
if lines is not None:
    print(f"Lines: {lines}, Words: {words}")


logging.basicConfig(filename='script.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_data():
    logging.info("Script started.")
    try:
        print("Processing data...")

        logging.info("Data processed successfully.")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
    finally:
        logging.info("Script execution finished.")

process_data()
