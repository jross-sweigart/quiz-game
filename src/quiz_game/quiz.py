#!/usr/bin/env python

import csv
import argparse
import threading
import time
import random
import sys

def load_quiz(filename):
    questions = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                questions.append((row[0].strip(), row[1].strip()))
    return questions

def run_quiz(questions, time_limit):
    correct_count = 0
    total_count = len(questions)
    
    def timer():
        time.sleep(time_limit)
        print("\nTime's up!")
        print(f"You got {correct_count} out of {total_count} questions correct.")
        sys.exit()
        
    threading.Thread(target=timer).start()
    
    for question, answer in questions:
        user_answer = input(f"Question: {question} = ? ")
        
        if user_answer.strip() == answer:
            correct_count += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {answer}.")
            
    print(f"You got {correct_count} out of {total_count} questions correct.")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Quiz Application')
    parser.add_argument('--file', type=str, default='../../problems.csv', help='CSV files with quiz questions')
    parser.add_argument('--time', type=int, default=15, help='Time limit in seconds')
    parser.add_argument('--shuffle', action='store_true', help='Shuffle quiz questions')
    args = parser.parse_args()
    
    questions = load_quiz(args.file)
    if args.shuffle:
        random.shuffle(questions)
    
    input('Press Enter to start the quiz...')
    run_quiz(questions, args.time)