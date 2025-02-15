import argparse


def configure_argument_parser():
    parser = argparse.ArgumentParser(
        description="Filter and separate BibTeX entries based on keys."
    )
    parser.add_argument("bib_filename", help="Path to the BibTeX file.")
    parser.add_argument(
        "-fe",
        "--filtered_entries",
        dest="filtered_entry_names",
        nargs="+",
        help="Entries to save",
    )
    parser.add_argument(
        "-ee",
        "--excluded_entries",
        dest="excluded_entry_names",
        nargs="+",
        help="Entries to not save",
    )
    parser.add_argument(
        "-fk",
        "--filtered_entry_keys",
        dest="filtered_entry_keys",
        nargs="+",
        help="Entry keys to save",
    )
    parser.add_argument(
        "-ek",
        "--excluded_entry_keys",
        dest="excluded_entry_keys",
        nargs="+",
        help="Entry keys to not save",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_folder",
        help="Output directory for filtered entries.",
    )
    parser.add_argument(
        "-sp",
        "--split_save",
        dest="split_save",
        action="store_true",
        help="Save entries in separate files",
        default=False,
    )
    return parser


def load_arguments(parser):
    args = parser.parse_args()
    bib_filename = args.bib_filename
    filtered_entry_names = args.filtered_entry_names
    excluded_entry_names = args.excluded_entry_names
    filtered_entry_keys = args.filtered_entry_keys
    excluded_entry_keys = args.excluded_entry_keys
    output_folder = args.output_folder
    if output_folder is None:
        output_folder = bib_filename.split(".")[0]
    split_save = args.split_save
    return (
        bib_filename,
        filtered_entry_names,
        excluded_entry_names,
        filtered_entry_keys,
        excluded_entry_keys,
        output_folder,
        split_save,
    )
