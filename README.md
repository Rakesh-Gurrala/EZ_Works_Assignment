# Smart Assistant for Research Summarization

A command-line interface (CLI) tool for simulating a smart assistant that summarizes documents, answers user questions, and provides evaluation challenges—all without requiring an internet connection or external API access.

## Features

* 🔍 **Ask Anything**: Ask questions based on the document's content and get simulated answers.
* ✅ **Challenge Mode**: Automatically evaluate simulated user responses against predefined questions.
* 🧠 **Summarization**: Extract a short summary from the document.
* ⚙️ **Offline Simulation**: Fully operational without OpenAI API or external modules.

## Usage

Run the script using Python 3:

```bash
python main.py [mode]
```

Where `[mode]` is optional:

* `1`: Ask Anything mode (default)
* `2`: Challenge Me mode

Example:

```bash
python main.py 2
```

## Project Structure

* `main.py`: Core CLI logic and simulated backend.
* No dependencies required (no need for `micropip` or `openai` modules).

## Development Notes

* This project is sandbox-friendly.
* Designed for educational and testing purposes.

## License

MIT License. Use freely with attribution.
