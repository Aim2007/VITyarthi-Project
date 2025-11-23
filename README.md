
# Calculator


## Overview of the Project
This project is a lightweight Graphical User Interface (GUI) calculator application. It is designed to perform basic arithmetic operations using a clean and simple interface. The application is built to demonstrate the capabilities of Python's `tkinter` library for desktop application development.

## Features
* **Standard Arithmetic:** Performs Addition (+), Subtraction (-), Multiplication (*), and Division (/).
* **Interactive GUI:** User-friendly grid layout with clickable buttons.
* **Error Handling:** gracefully handles invalid operations (like division by zero) by displaying "Error" instead of crashing.
* **Clear Functionality:** dedicated 'C' button to instantly clear the input field.
* **Expression Evaluation:** Uses Python's underlying evaluation capabilities for accurate results.

## Technologies/Tools Used
* **Language:** Python 3.x
* **GUI Library:** Tkinter (Standard Python interface to the Tk GUI toolkit)
* **Editor/IDE:** PyCharm

## Steps to Install & Run the Project
1.  **Prerequisites:** Ensure you have Python installed on your system. You can verify this by typing `python --version` in your terminal.
2.  **Download:** Download the file named `rps.py` to a known folder on your computer.
3.  **Navigate:** Open your terminal or command prompt and navigate to the folder where you saved the file.
4.  **Run:** Execute the following command:
    ```bash
    python calculator.py
    ```
    
## Instructions for Testing
To ensure the calculator is working correctly, follow these manual test cases:

1.  **Addition Test:**
    * Launch the app.
    * Click `5`, then `+`, then `3`, then `=`.
    * **Expected Result:** Display shows `8`.

2.  **Division by Zero Test:**
    * Click `Clear (C)` if needed.
    * Click `9`, then `/`, then `0`, then `=`.
    * **Expected Result:** Display shows `Error`.

3.  **Clear Button Test:**
    * Type any number sequence (e.g., `123`).
    * Click `C`.
    * **Expected Result:** The display becomes empty.

4.  **Complex Operation Test:**
    * Click `2`, `*`, `3`, `+`, `1`, `=`.
    * **Expected Result:** Display shows `7` (due to Python's order of operations).




