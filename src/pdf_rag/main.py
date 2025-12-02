#!/usr/bin/env python
import sys
import warnings
from crew import PdfRag
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    user_input = input("Ask a question: ")
    inputs = {"input": user_input}
    PdfRag().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
