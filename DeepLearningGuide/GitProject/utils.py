"""
Provides utility
"""
import numpy as np
from Dataset.character_table import CharacterTable
from Dataset.data import generate_data




# Parameters for the model and dataset.
DIGITS = 3
REVERSE = True
# Maximum length of input is 'int + int' (e.g., '345+678'). Maximum length of int is DIGITS.
MAXLEN = DIGITS + 1 + DIGITS

def vectorization(questions, expected):
    """
    Vectorize and encode the given String.
        Arguments:
            questions (str): A string containing values like 12+89
            expected (str): A sting containing values like 101
        Returns:
            x, y (numpy): 2d encoded Matrix
    """
    chars = "0123456789+ "
    ctable = CharacterTable(chars)
    X = np.zeros((len(questions), MAXLEN, len(chars)), dtype=np.bool)
    Y = np.zeros((len(questions), DIGITS + 1, len(chars)), dtype=np.bool)
    for i, sentence in enumerate(questions):
        X[i] = ctable.encode(sentence, MAXLEN)
    for i, sentence in enumerate(expected):
        Y[i] = ctable.encode(sentence, DIGITS + 1)
    return X, Y

# Shuffle (x, y) in unison as the later parts of x will almost all be larger digits.
def shuffle(data, label):
    """
    Shuffles the Dataset.
        Arguments:
            data : Data samples
            label : Data labels
        Returns:
            x : Shuffled samples
            y : Shuffled ssamples

    """
    indices = np.arange(len(label))
    np.random.shuffle(indices)
    data = data[indices]
    label = label[indices]
    return data, label

def train_val_split(data, label):
    """
    Split dataset into training and Validation
    Arguments:
        data : Data samples
        label : Data labels
    Returns:
        x_train: Training data samples
        y_train: Training data labels
        x_val: Validation data samples
        y_val: Validation data labels
    """
    # Explicitly set apart 10% for validation data that we never train over.
    split_at = len(data) - len(data) // 10
    (x_train, x_val) = data[:split_at], data[split_at:]
    (y_train, y_val) = label[:split_at], label[split_at:]

    print("Training Data:")
    print(x_train.shape)
    print(y_train.shape)

    print("Validation Data:")
    print(x_val.shape)
    print(y_val.shape)
    return x_train, y_train, x_val, y_val

if __name__ == '__main__':
    x, y = generate_data(data_size=10)
    print(x)
    print(y)
    x_vect, y_vect = vectorization(x, y)
    print(x_vect)
    print(y_vect)
    x_shuff, y_shuff = shuffle(x_vect, y_vect)
    print(x_shuff)
    print(y_shuff)
    x_train, y_train, x_val, y_val = train_val_split(x_shuff, y_shuff)
    print(x_train)
    print(y_train)
    print(x_val)
    print(y_val)
