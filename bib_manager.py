import os
import bibtexparser


class BibManager:
    def __init__(self, input_filename: str, output_folder: str, split_save: bool):
        self.__input_filename = input_filename
        self.__output_folder = output_folder
        self.__split_save = split_save

    def load(self):
        with open(self.__input_filename, "r", encoding="utf-8") as bibtex_file:
            bib_db = bibtexparser.load(bibtex_file)
        bib_entries = bib_db.entries_dict
        return bib_entries

    def save(self, entries):
        self.__try_to_create_folder()
        if self.__split_save:
            return self.__save_entries_separate(entries)
        return self.save_entries_bundled(entries)

    def __try_to_create_folder(self):
        if not os.path.exists(self.__output_folder):
            os.makedirs(self.__output_folder)

    def __save_entries_separate(self, entries):
        for key, entry in entries.items():
            entry_db = bibtexparser.bibdatabase.BibDatabase()
            entry_db.entries = [entry]
            output_filename = os.path.join(self.__output_folder, f"{key}.bib")
            self.save_bib_db(entry_db, output_filename)

    def save_entries_bundled(self, entries):
        entry_db = bibtexparser.bibdatabase.BibDatabase()
        entry_db.entries = entries.values()
        output_filename = os.path.join(self.__output_folder, "output.bib")
        self.save_bib_db(entry_db, output_filename)

    def save_bib_db(self, entry_db, output_folder):
        with open(output_folder, "w", encoding="utf-8") as output_file:
            bibtexparser.dump(entry_db, output_file)
