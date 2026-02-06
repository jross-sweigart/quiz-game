#!/usr/bin/env python

import csv
import argparse

def load_quiz(filename):
    questions = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                questions.append((row[0].strip(), row[1].strip()))
    return questions

def run_quiz(questions):
    correct_count = 0
    total_count = len(questions)
    
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
    parser.add_argument('--file', type=str, default='problems.csv', help='CSV files with quiz questions')
    
    args = parser.parse_args()
    
    questions = load_quiz(args.file)
    run_quiz(questions)