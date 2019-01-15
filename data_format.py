import pandas as pd
import string


class Letter:
    def __init__(self, str, index, unicode, utf_8_hex, description):
        self.str = str
        self.unicode = unicode
        self.utf_8_hex = utf_8_hex
        self.description = description
        self.index = index

    def __repr__(self):
        return "<%s str:%s unicode:%s>" \
               % (self.index, self.str, self.unicode)


class BaseLetters(object):
    def __init__(self):
        self.m_index_letter_dict = dict()
        self.m_letter_index_dict = dict()
        self.m_letter_list = list()
        self.m_max = 30


class TamilLetters(BaseLetters):
    def __init__(self):
        super().__init__()
        self.__dataframe = pd.read_excel('tamil_unicode.xlsx')
        self.__load()
        self.n_classes = len(self.m_letter_index_dict)

    def __load(self):
        for index, row in self.__dataframe.iterrows():
            oneLetter = Letter(row['character'], index, row['Unicode'], row['UTF-8'], row['description'])
            self.m_index_letter_dict[index] = oneLetter
            self.m_letter_index_dict[row['character']] = index
            self.m_letter_list.append(row['character'])

        self.m_index_letter_dict[85] = Letter(' ', 85, 'U+0020', '0x20', 'SPACE')
        self.m_index_letter_dict[86] = Letter('-', 86, 'U+0000', '0x20', 'OTHERS')
        self.m_index_letter_dict[87] = Letter('-1', 87, 'U+0001', '0x20', 'EOS')

        self.m_letter_index_dict[' '] = 85
        self.m_letter_index_dict['-'] = 86
        self.m_letter_index_dict['-1'] = 87
        self.m_letter_list.append(' ')


class EnglishLetters(BaseLetters):
    def __init__(self):
        super().__init__()
        self.__load()
        self.n_classes = len(self.m_letter_index_dict)

    def __load(self):

        english_letters_list = list(string.ascii_lowercase)
        for index, ltr in enumerate(english_letters_list):
            oneLetter = Letter(ltr, index, ltr, ltr, ltr)
            self.m_index_letter_dict[index] = oneLetter
            self.m_letter_index_dict[ltr] = index
            self.m_letter_list.append(ltr)

        self.m_index_letter_dict[26] = Letter(' ', 26, 'U+0020', '0x20', 'SPACE')
        self.m_index_letter_dict[27] = Letter('-', 27, 'U+0000', '0x20', 'OTHERS')
        self.m_index_letter_dict[28] = Letter('-1', 28, 'U+0001', '0x20', 'EOS')

        self.m_letter_index_dict[' '] = 26
        self.m_letter_index_dict['-'] = 27
        self.m_letter_index_dict['-1'] = 28
        self.m_letter_list.append(' ')


def data_aggregation():
    n_datasheets = 25

    tamil_lines = []
    english_lines = []
    for i in range(1, n_datasheets+1):
        filename = 'data/%02d.txt'%(i)
        gt_file = 'data/%02d_gt.txt' % (i)
        with open(filename, 'r', encoding="utf8") as f:
            lines = f.readlines()

        with open(gt_file, 'r', encoding="utf8") as f:
            gt_lines = f.readlines()

        tamil_lines.extend(lines)
        english_lines.extend(gt_lines)

    with open('data/tamil_lines_new.txt', 'w', encoding="utf8") as f:
        f.writelines(tamil_lines)

    with open('data/english_lines_new.txt', 'w', encoding="utf8") as f:
        f.writelines(english_lines)


def string2Letter(f_str, f_letters=BaseLetters()):
    out_list = []

    for s in f_str:
        if s in f_letters.m_letter_list:
            out_list.append(f_letters.m_index_letter_dict[f_letters.m_letter_index_dict[s]])
        else:
            out_list.append(f_letters.m_index_letter_dict[f_letters.m_letter_index_dict['-']])

    out_list.append(f_letters.m_index_letter_dict[f_letters.m_letter_index_dict['-1']])
    return out_list


def index2string(f_indices, f_letters=BaseLetters()):
    out_list = []

    for i in f_indices:
        out_str = f_letters.m_index_letter_dict[i].str
        if out_str == '-1':
            break
        out_list.append(out_str)

    out_str = "".join(out_list)
    return out_str


if __name__ == "__main__":
    TL = TamilLetters()
    print('Tamil Letters: ', TL.m_index_letter_dict)

    EL = EnglishLetters()
    print('English Letters: ', EL.m_index_letter_dict)
    # print(lines[0][2])

    out = string2Letter(u'தகப்பன் தன் பிள்ளைகள் மேல்', TL)

    print(out)