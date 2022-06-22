"""
Provides training
"""
import numpy as np

from Dataset.character_table import CharacterTable
from Dataset.data import generate_data
from utils import vectorization, shuffle, train_val_split
from Models.model import model_creation


chars = "0123456789+ "
ctable = CharacterTable(chars)
REVERSE = True

def training(model, epochs, batch_size, x_train, y_train, x_val, y_val):
    """ Starts Training of the dataset with validation

    Args:
        model (model): LSTM Model
        epochs (int): Number of Epochs
        batch_size (int): Dataset Batch Size
        x_train (ndarray): Training data vectors
        y_train (ndarray): Training label vectors
        x_val (ndarray): Validation data vectors
        y_val (ndarray): Validation label vectors
    """
    # Train the model each generation and show predictions against the validation dataset.
    for i in range(1, epochs):
        print()
        print("Iteration", i)
        model.fit(
            x_train,
            y_train,
            batch_size=batch_size,
            epochs=1,
            validation_data=(x_val, y_val),
        )
        # Select 10 samples from the validation set at random so we can visualize errors.
        for i in range(10):
            ind = np.random.randint(0, len(x_val))
            rowx, rowy = x_val[np.array([ind])], y_val[np.array([ind])]
            preds = np.argmax(model.predict(rowx), axis=-1)
            q = ctable.decode(rowx[0])
            correct = ctable.decode(rowy[0])
            guess = ctable.decode(preds[0], calc_argmax=False)
            print("Q", q[::-1] if REVERSE else q, end=" ")
            print("T", correct, end=" ")
            if correct == guess:
                print("☑ " + guess)
            else:
                print("☒ " + guess)

if __name__ == '__main__':
    epochs = 30
    batch_size = 32
    x, y = generate_data(data_size=10)
    print(x)
    print(y)
    x, y = vectorization(x, y)
    print(x)
    print(y)
    x, y = shuffle(x, y)
    print(x)
    print(y)
    x_train, y_train, x_val, y_val = train_val_split(x, y)
    print(x_train)
    print(y_train)
    print(x_val)
    print(y_val)
    model = model_creation()
    training(model, epochs, batch_size, x_train, y_train, x_val, y_val)
