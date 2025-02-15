# BibTeX Manipulator CI Tool

## Overview

BibTeX Manipulator CI Tools is a command-line utility designed to filter and separate BibTeX entries based on specified criteria. This tool is particularly useful for managing large BibTeX databases by allowing users to selectively save entries into separate files or folders.

## Features

- **Filtering by Entry Names**: Specify entries to save or exclude based on their names.
- **Filtering by Entry Keys**: Specify entry keys to save or exclude for more granular control.
- **Output Directory Configuration**: Define the output directory for filtered entries.
- **Separate Files Save Option**: Save each entry in separate files for easy management.

## Installation

Ensure you have Python installed on your system. This tool is built using Python's `bibtexparser` library. A poetry project is available.

## Usage

`
python main.py bib_filename [options]
`

### Options

- `-fe`, `--filtered_entries`: Entries to save. Example: `-fe entry1 entry2`.
- `-ee`, `--excluded_entries`: Entries to not save. Example: `-ee entry3 entry4`.
- `-fk`, `--filtered_entry_keys`: Entry keys to save. Example: `-fk key1 key2`.
- `-ek`, `--excluded_entry_keys`: Entry keys to not save. Example: `-ek key3 key4`.
- `-o`, `--output`: Output directory for filtered entries. Example: `-o output_folder`.
- `-sp`, `--split_save`: Save entries in separate files. Example: `-sp`.

### Example

To filter entries named `entry1` and `entry2`, excluding `entry3` and `entry4`, and save them in a folder named `filtered_bibtex`, run:

`
python bibtex_manipulator.py -fe entry1 entry2 -ee entry3 entry4 -o filtered_bibtex
`

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
