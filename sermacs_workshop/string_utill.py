"""
string_utill.py
Sample file to practice pull request
"""

def title_case(sentence):
    """
    onverts string to title case
    Parameters
    _____________
    sentence: string
        Sentence to be transformed
    
    Returns
    ____________
    titled:  string
         Sentence in title format
    
    Example
    ___________
    >>> title_case('This iS a string')
        This Is A String
    >>>
    """
    ignore = ['the', 'of', 'a']
    titled = [x[0].upper()+x[1:].lower() for  x in sentence.split()]
    caps = []
    caps.append(titled[0])
    for tit in titled[1:]:
       print(tit)
       if tit.lower() in ignore:
           caps.append(tit.lower())
       else:
           caps.append(tit)
    titled = ' '.join(caps)
    return titled


