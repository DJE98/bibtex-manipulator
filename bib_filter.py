class BibFilter:
    def __init__(
        self,
        filtered_entry_names=None,
        excluded_entry_names=None,
        filtered_entry_keys=None,
        excluded_entry_keys=None,
    ):
        self.__filtered_entry_names = filtered_entry_names
        self.__excluded_entry_names = excluded_entry_names
        self.__filtered_entry_keys = filtered_entry_keys
        self.__excluded_entry_keys = excluded_entry_keys
        self.__mandatory_keys = ["ENTRYTYPE", "ID"]

    def __call__(self, bib_entries):
        if isinstance(self.__filtered_entry_names, list):
            bib_entries = self.filter_entry_names(bib_entries)
        if isinstance(self.__filtered_entry_keys, list):
            bib_entries = self.filter_entry_keys(bib_entries)
        if isinstance(self.__excluded_entry_names, list):
            bib_entries = self.exclude_entry_names(bib_entries)
        if isinstance(self.__excluded_entry_keys, list):
            bib_entries = self.exclude_entry_keys(bib_entries)
        return bib_entries

    def filter_entry_names(self, bib_entries):
        return self.__manipulate_entry_names(
            bib_entries, self.__filter, self.__filtered_entry_names
        )

    def exclude_entry_names(self, bib_entries):
        return self.__manipulate_entry_names(
            bib_entries, self.__exclude, self.__excluded_entry_names
        )

    def exclude_entry_keys(self, bib_entries):
        return self.__manipulate_entry_keys(
            bib_entries, self.__exclude, self.__excluded_entry_keys
        )

    def filter_entry_keys(self, bib_entries):
        return self.__manipulate_entry_keys(
            bib_entries, self.__filter, self.__filtered_entry_keys
        )

    def __manipulate_entry_names(self, bib_entries, manipulator, manipulator_keys):
        filtered_entries = {
            key: entry
            for key, entry in bib_entries.items()
            if manipulator(key, manipulator_keys)
        }
        return filtered_entries

    def __manipulate_entry_keys(self, bib_entries, manipulator, manipulator_keys):
        modified_entries = {}
        for entry_name, entry in bib_entries.items():
            modified_entries[entry_name] = {}
            for key in entry:
                if manipulator(key, manipulator_keys) or key in self.__mandatory_keys:
                    modified_entries[entry_name][key] = entry[key]
        return modified_entries

    def __filter(self, key: str, filtered_keys):
        return key in filtered_keys

    def __exclude(self, key: str, excluded_keys: list):
        return key not in excluded_keys
