"""
Provides model
"""

from operator import mod
import re
from tensorflow import keras
from tensorflow.keras import layers

# Parameters for the model and dataset.
DIGITS = 3
REVERSE = True
# Maximum length of input is 'int + int' (e.g., '345+678'). Maximum length of
# int is DIGITS.
MAXLEN = DIGITS + 1 + DIGITS
chars = "0123456789+ "

print("Build model...")
def model_creation():
    """
    Initializes Model Architecture
        Arguments: 
            None
        Returns:
            model : Returns keras model
    """
    num_layers = 1  # Try to add more LSTM layers!

    model = keras.Sequential()
    # "Encode" the input sequence using a LSTM, producing an output of size 128.
    # Note: In a situation where your input sequences have a variable length,
    # use input_shape=(None, num_feature).
    model.add(layers.LSTM(128, input_shape=(MAXLEN, len(chars))))
    # As the decoder RNN's input, repeatedly provide with the last output of
    # RNN for each time step. Repeat 'DIGITS + 1' times as that's the maximum
    # length of output, e.g., when DIGITS=3, max output is 999+999=1998.
    model.add(layers.RepeatVector(DIGITS + 1))
    # The decoder RNN could be multiple layers stacked or a single layer.
    for _ in range(num_layers):
        # By setting return_sequences to True, return not only the last output but
        # all the outputs so far in the form of (num_samples, timesteps,
        # output_dim). This is necessary as TimeDistributed in the below expects
        # the first dimension to be the timesteps.
        model.add(layers.LSTM(128, return_sequences=True))

    # Apply a dense layer to the every temporal slice of an input. For each of step
    # of the output sequence, decide which character should be chosen.
    model.add(layers.Dense(len(chars), activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.summary()
    return model

if __name__ == '__main__':
    model = model_creation()