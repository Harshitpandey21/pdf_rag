#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import PdfRag

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    user_input = input("Enter a question: ")
    inputs = {"input": user_input}
    PdfRag().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()