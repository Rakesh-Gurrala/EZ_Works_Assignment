# main.py
# CLI version of Smart Assistant for restricted/sandboxed environments

import sys

# Inline mock backend logic
def ask_question(context, user_question, eval_mode=False, expected=None):
    if eval_mode:
        is_correct = user_question.strip().lower() == expected.strip().lower()
        return ("Correct" if is_correct else "Incorrect", f"Expected: {expected}")
    else:
        return ("[Sample Answer] This is a dummy response.", "[Source] Document content snippet")

def generate_challenge(document_text):
    return [
        {"question": "What is the main topic of the document?", "context": document_text, "answer": "Sample topic"},
        {"question": "List one key finding.", "context": document_text, "answer": "Sample finding"},
        {"question": "What conclusion is drawn in the last section?", "context": document_text, "answer": "Sample conclusion"},
    ]

# Inline document parsing and summarization
def parse_doc(text_data):
    return text_data.strip()

def summarize_doc(text):
    lines = text.splitlines()
    return " ".join(lines[:5]) + "..." if len(lines) > 5 else text

def main():
    print("=== Smart Assistant for Research Summarization ===")

    # Use predefined inline content due to I/O restrictions
    predefined_text = """
    This document explains the principles of neural networks. It introduces perceptrons,
    activation functions, and backpropagation. One key finding is the effectiveness of
    ReLU in deep architectures. The document concludes with a discussion on ethical AI.
    """
    full_text = parse_doc(predefined_text)

    print("\n--- Document Summary (≤150 words) ---")
    print(summarize_doc(full_text))

    # Predefined mode selection due to restricted input environment
    mode = "1"  # Change to "2" to run Challenge Me mode
    print("\nSelected Mode:", "Ask Anything" if mode == "1" else "Challenge Me")

    if mode == "1":
        sample_questions = [
            "What is the main subject of the document?",
            "Which activation function is mentioned?",
            "What is discussed in the conclusion?"
        ]
        for user_question in sample_questions:
            print(f"\nQuestion: {user_question}")
            answer, source = ask_question(full_text, user_question)
            print(f"Answer: {answer}")
            print(f"Justification: {source}")

    elif mode == "2":
        questions = generate_challenge(full_text)
        print("\n--- Answer the following questions ---")
        for i, q in enumerate(questions):
            print(f"Q{i+1}: {q['question']}")
            user_input = q['answer']  # Simulated user response
            eval_result = ask_question(q['context'], user_input, eval_mode=True, expected=q['answer'])
            print(f"Evaluation: {eval_result[0]}")
            print(f"Justification: {eval_result[1]}")
    else:
        print("Invalid selection. Exiting.")

if __name__ == "__main__":
    main()
