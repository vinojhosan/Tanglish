import numpy as np
import data_format as df
# from keras.utils import to_categorical


def load_texts():
    with open('data/tamil_lines.txt', 'r', encoding="utf8") as f:
        tamil_lines = f.readlines()

    with open('data/english_lines.txt', 'r', encoding="utf8") as f:
        english_lines = f.readlines()

    return tamil_lines, english_lines


batch_size = 1
np.random.seed(4)
TL = df.TamilLetters()
EL = df.EnglishLetters()


def text_generator():
    tamil_lines, english_lines = load_texts()

    while True:
        k = 0
        tamil_sample_list = []
        english_sample_list = []
        while k < batch_size:
            rand_int = np.random.randint(0, len(tamil_lines), 1)
            tamil_line = tamil_lines[rand_int[0]]
            english_line = english_lines[rand_int[0]]

            if len(tamil_line) < 3 or len(english_line) < 3:
                continue
            t_split = tamil_line[:-1].split(' ')
            e_split = english_line[:-1].split(' ')

            rand_int = np.random.randint(0, len(t_split), 1)

            if len(e_split) <= rand_int[0]:
                continue

            tamil_sample_list.append(t_split[rand_int[0]])
            english_sample_list.append(e_split[rand_int[0]])
            k += 1


        input_mat = np.zeros((batch_size, TL.m_max, TL.n_classes), np.float32)
        output_mat = np.zeros((batch_size, EL.m_max, EL.n_classes), np.float32)
        for itr in range(len(tamil_sample_list)):
            t_encoded = np.zeros((TL.m_max, TL.n_classes), np.float32)
            t_word = tamil_sample_list[itr]
            t_word_list = df.string2Letter(t_word, TL)
            for i,w in enumerate(t_word_list):
                t_encoded[i][w.index] = 1

            e_encoded = np.zeros((EL.m_max, EL.n_classes), np.float32)
            e_word = english_sample_list[itr]
            e_word_list = df.string2Letter(e_word, EL)
            for i, w in enumerate(e_word_list):
                e_encoded[i][w.index] = 1

            input_mat[itr] = t_encoded
            output_mat[itr] = e_encoded

        yield input_mat, output_mat


# for k in text_generator():
#     print(k[0].shape)
#     print(k[1].shape)
#     break



