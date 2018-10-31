"""
string_util.py
Oh god how do I push things.

Misc. string processing functions
"""

def title_case(sentence):
    """
    Capitalize the first letter of every word.

    Parameters
    ----------------
    sentence: string
        The sentence to be put into title case.

    Returns
    ----------------
    capitalized: string
        The input string in title case.
    """

    if sentence == sentence.upper():
        capitalized = ' '.join([x[0].upper()+x[1:].lower() for x in sentence.strip().split()])
    else:
        capitalized = ' '.join([x[0].upper()+x[1:] for x in sentence.strip().split()])
    return capitalized

if __name__ == "__main__":
    this = 'I AM SUPER ANNOYED WITH THESE CCQC TURDS.'
#   this = 'I am super annoyed with these CCQC turds.'
    print(title_case(this))
