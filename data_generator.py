import numpy as np
import data_format as df


def load_texts():
    with open('data/tamil_lines.txt', 'r', encoding="utf8") as f:
        tamil_lines = f.readlines()

    with open('data/english_lines.txt', 'r', encoding="utf8") as f:
        english_lines = f.readlines()

    return tamil_lines, english_lines


tamil_lines, english_lines = load_texts()

batch_size = 8
indices = np.random.choice(range(0, len(tamil_lines)), batch_size)

for ind in indices:
    tamil = tamil_lines