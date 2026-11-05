# Skyscrapers Puzzle Validator – Turing Machine

## Overview

This project implements a **Turing Machine that validates solutions to the Skyscrapers puzzle**.

The Skyscrapers puzzle consists of a square grid where each cell contains a building of a certain height. The goal is to arrange the buildings so that each row and column contains every height exactly once, while also satisfying the visibility clues around the grid.

This project uses a Python script to automatically generate the transition table of a Turing Machine that checks whether a given puzzle configuration is valid.

## Project Structure

```text
.
├── create_final.py          # Python script that generates the Turing Machine
└── skyscrapers_final.tms    # Generated Turing Machine transition table
```

## How It Works

The Python script defines a function called `create_final()` that generates the transitions required by the Turing Machine.

Instead of manually writing every transition, the script builds them programmatically using predefined valid permutations and loops.

The generated machine uses the following main steps:

### 1. Initialization

The machine starts in the `start` state and moves across the input until it reaches the `#` separator.

### 2. Row Validation

The machine searches for the first tower in a row and uses a sequence of states to identify the current row configuration.

A predefined list of permutations represents the valid row arrangements. The machine follows transitions corresponding to these permutations to determine whether the current row is valid.

### 3. Moving Between Rows

After processing a row, the machine checks whether more rows need to be examined. It uses intermediate states such as `skip` and `reset` to navigate the input and return to the appropriate position.

### 4. Column Validation

Once the row checks are completed, the machine moves on to the columns.

It uses the `X` symbol to mark positions that have already been processed. By following the corresponding permutation-based transitions, it checks whether each column contains a valid arrangement.

### 5. Acceptance

If all required checks are successfully completed, the machine reaches the accepting state `Y`.

If the input does not match any of the valid transition sequences, the machine cannot continue and therefore rejects the configuration.

## Valid Permutations

The script contains a predefined list of valid permutations:

```python
permutations = [
    "141232", "142132",
    "141323", "142313", "143123",
    "143214",
    "231241", "232141",
    "214232", "221432", "224132",
    "231422", "232412", "234122",
    "214323", "224313", "234213",
    "313241", "321341", "323141",
    "312432", "313422", "323412",
    "412341"
]
```

These permutations are used to construct the transition sequences that the Turing Machine follows when validating the puzzle.

## Generating the Turing Machine

To generate the transition table, run the Python script:

```bash
python create_final.py
```

This executes `create_final()` and creates a file named:

```text
skyscrapers_final.tms
```

The output file contains the generated Turing Machine transitions.

## Transition Table Generation

Each transition is represented using the following structure:

```text
current_state, read_symbol
next_state, write_symbol, movement
```

For example:

```text
start, 1
start, 1, >
```

This means that when the machine is in the `start` state and reads `1`, it keeps the symbol unchanged, remains in the same state, and moves one position to the right.

The script also removes duplicate transitions before writing the final output, ensuring that the generated transition table does not contain repeated commands.

## Technologies Used

- **Python 3** – Generates the transition table programmatically.
- **Turing Machines** – Used to validate puzzle configurations.
- **`.tms` format** – Stores the generated transition rules.

## Purpose

The main purpose of this project is to demonstrate how a computational problem, such as validating a Skyscrapers puzzle, can be represented and solved using a Turing Machine.

Rather than implementing the validation directly in Python, Python is used only to generate the machine's transition table. The actual validation is performed by the generated Turing Machine.
