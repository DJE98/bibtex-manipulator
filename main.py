import os

import bibtexparser

from arguments import configure_argument_parser, load_arguments
from bib_filter import BibFilter
from bib_manager import BibManager


def transform(bib_manager, bib_filter):
    bib_entries = bib_manager.load()
    bib_entries = bib_filter(bib_entries)
    bib_manager.save(bib_entries)


if __name__ == "__main__":
    parser = configure_argument_parser()
    (
        bib_filename,
        filtered_entry_names,
        excluded_entry_names,
        filtered_entry_keys,
        excluded_entry_keys,
        output_folder,
        split_save,
    ) = load_arguments(parser)
    bib_manager = BibManager(bib_filename, output_folder, split_save)
    bib_filter = BibFilter(
        filtered_entry_names,
        excluded_entry_names,
        filtered_entry_keys,
        excluded_entry_keys,
    )
    transform(bib_manager, bib_filter)
