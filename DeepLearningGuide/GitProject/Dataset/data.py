"""
Provides data
"""
import numpy as np
from Dataset.character_table import CharacterTable



# Parameters for the model and dataset.
DIGITS = 3
REVERSE = True
# Maximum length of input is 'int + int' (e.g., '345+678'). Maximum length of
# int is DIGITS.
MAXLEN = DIGITS + 1 + DIGITS
chars = "0123456789+ "
ctable = CharacterTable(chars)

def generate_data(data_size):
    """
    Generates Dataset of desired Size
    Arguments:
        data_size (int): Size of the dataset
    Returns:
        question (str): Data samples
        expected (str): Data Labels
    """
    questions = []
    expected = []
    seen = set()
    print("Generating data...")
    while len(questions) < data_size:
        f = lambda: int(
            "".join(
                np.random.choice(list("0123456789"))
                for i in range(np.random.randint(1, DIGITS + 1))
            )
        )
        a, b = f(), f()
        # Skip any addition questions we've already seen
        # Also skip any such that x+Y == Y+x (hence the sorting).
        key = tuple(sorted((a, b)))
        if key in seen:
            continue
        seen.add(key)
        # Pad the data with spaces such that it is always MAXLEN.
        q = "{}+{}".format(a, b)
        query = q + " " * (MAXLEN - len(q))
        ans = str(a + b)
        # Answers can be of maximum size DIGITS + 1.
        ans += " " * (DIGITS + 1 - len(ans))
        if REVERSE:
            # Reverse the query, e.g., '12+345  ' becomes '  543+21'. (Note the
            # space used for padding.)
            query = query[::-1]
        questions.append(query)
        expected.append(ans)
    #print(questions[0:10])
    #print(expected[0:10])
    #print("Total questions:", len(questions))
    return questions, query


if __name__ == '__main__':
    x, y = generate_data(data_size=100)
    print(x)
    print(y)
