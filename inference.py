import keras
import numpy as np
import data_generator
import data_format

model = keras.models.load_model('first_model.hdf5')

def onehot2indices(onehot_mat):
    out= []
    for i in onehot_mat:
        ind = np.argmax(i)
        out.append(ind)

    return out

def test():
    for i, k in enumerate(data_generator.text_generator()):
        print(k[0].shape)

        indices = onehot2indices(k[0][0])
        final_string = data_format.index2string(indices, data_generator.TL)
        print(final_string)

        out = model.predict(k[0])
        indices = onehot2indices(out[0])
        final_string = data_format.index2string(indices, data_generator.EL)
        print(final_string)

        if i > 100:
            break


def tamilstring2onehot(tamil_line, TL):

    t_split = tamil_line.split(' ')
    tamil_sample_list = t_split
    batch_size = len(tamil_sample_list)

    input_mat = np.zeros((batch_size, TL.m_max, TL.n_classes), np.float32)
    for itr in range(len(tamil_sample_list)):
        t_encoded = np.zeros((TL.m_max, TL.n_classes), np.float32)
        t_word = tamil_sample_list[itr]
        t_word_list = data_format.string2Letter(t_word, TL)
        for i, w in enumerate(t_word_list):
            t_encoded[i][w.index] = 1

        input_mat[itr] = t_encoded

    return input_mat


def tamil2english(tamil_str):

    print(tamil_str)
    onehot_input = tamilstring2onehot(tamil_str, data_generator.TL)

    out = model.predict(onehot_input)

    out_sentence = []
    for i, out_itr in enumerate(out):
        indices = onehot2indices(out[i])
        final_string = data_format.index2string(indices, data_generator.EL)
        out_sentence.append(final_string)

    out_sentence = " ".join(out_sentence)
    print(out_sentence)
    return out_sentence


tamil2english(u"விண்மண் உண்டாக்கிய வித்தகனிடமிருந்து")
tamil2english(u"மனிதர் உன்னை வெறுத்தாலும்")
tamil2english(u"மாராத இயேசு இருக்கிறார்")
tamil2english(u"தனிமையான நேரத்திலும் உன்")
tamil2english(u"தந்தையாய் வந்து தேற்றிடுவார்")
tamil2english(u"நீர் பேசினால் அது வேதம்")
tamil2english(u"உம் வார்த்தையே பிரசாதம்")
tamil2english(u"உம் வல்ல செயல்கள் பிரமாதம்")
tamil2english(u"போதும் போதும் நீர் போதும்")
tamil2english(u"இன்றே எம் பந்தியில் சேரும்")
tamil2english(u"வாரும் நீர் விரைவில் வாரும்")
