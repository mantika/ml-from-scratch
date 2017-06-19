import numpy as np


class BagOfWords:

    def __self__(self, vocab):
        self._vocab = vocab

    def __call__(self, text):
        vector = np.zeros((len(self._vocab),), dtype=np.float32)
        for w in text.split():
            self._vocab.get(w)
            if w is not None:
                vector[w] = 1.
        return vector
