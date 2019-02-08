from keras.models import Sequential
from keras.layers import LSTM, TimeDistributed, Dense, InputLayer

import data_generator
from data_generator import TL, EL


# prepare sequence
seq_length = TL.m_max


# define LSTM configuration
n_batch = data_generator.batch_size
n_epoch = 1000

def train_tamil2english():
    # create LSTM
    model = Sequential()
    input_layer = InputLayer(batch_input_shape=(n_batch, seq_length, TL.n_classes))
    model.add(input_layer)
    model.add(LSTM(64, input_shape=(seq_length, TL.n_classes), return_sequences=True))
    model.add(TimeDistributed(Dense(EL.n_classes)))
    model.compile(loss='mean_squared_error', optimizer='adam')
    print(model.summary())
    # train LSTM

    model.fit_generator(data_generator.text_generator(), epochs=n_epoch, steps_per_epoch=100, verbose=2)
    model.save('tamil2english_model.hdf5')


def train_english2tamil():
    # create LSTM
    model = Sequential()
    input_layer = InputLayer(batch_input_shape=(n_batch, seq_length, EL.n_classes))
    model.add(input_layer)
    model.add(LSTM(64, input_shape=(seq_length, EL.n_classes), return_sequences=True))
    model.add(TimeDistributed(Dense(TL.n_classes)))
    model.compile(loss='mean_squared_error', optimizer='adam')
    print(model.summary())
    # train LSTM

    model.fit_generator(data_generator.text_generator(), epochs=n_epoch, steps_per_epoch=100, verbose=2)
    model.save('english2tamil_model.hdf5')


train_english2tamil()