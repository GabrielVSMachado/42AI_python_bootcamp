from random import randint


def generator(text: str, sep=" ", option=None) -> GeneratorExit:
    """
    Split the text according to sep value and yield the substrings.
    @param: text: text to be slipted;
    @param: sep: separator to slipt text;
    @param: option: the behaviour apply to list of substrings;
    return: a iterator with words
    """

    if type(text) != str:
        yield "ERROR"

    def shuffle(slipted_txt: list) -> list:
        """
        Create a list of words in shuffled order.
        @param: slipted_txt: list of strings
        return: A list of strings
        """
        shuffled_slpt_txt = []
        for string in slipted_txt:
            i = randint(0, len(slipted_txt) - 1)
            shuffled_slpt_txt.insert(i, string)
        return shuffled_slpt_txt

    def unique(slipted_txt: list) -> list:
        """
        Create list with only a uniq sample of which word in slipted_txt
        @param: slipted_txt: list of strings;
        return: List of strings
        """
        slipted_uniq_txt = []
        for string in slipted_txt:
            if string not in slipted_uniq_txt:
                slipted_uniq_txt.append(string)
        return slipted_uniq_txt

    def sort(slipted_txt: list) -> list:
        """
        Create a sorted list as ASCII characters
        @param: slipted_txt: list of strings;
        return: Sorted list of strings
        """
        slpt_sorted_txt = []
        for string in slipted_txt:
            i = 0
            while (i < len(slpt_sorted_txt) and string > slpt_sorted_txt[i]):
                i += 1
            slpt_sorted_txt.insert(i, string)
        return slpt_sorted_txt

    slipted_txt = text.split(sep=sep)

    lookup_fn = {
        "shuffle": shuffle,
        "unique": unique,
        "ordered": sort
    }

    if option:
        if type(option) != str or option not in lookup_fn.keys():
            yield "ERROR"
        slipted_txt = lookup_fn[option](slipted_txt)

    for string in slipted_txt:
        yield string
