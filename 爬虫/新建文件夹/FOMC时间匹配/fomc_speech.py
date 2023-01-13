import pandas as pd
from tensorflow import keras
import numpy as np
from model import speech_model
from bert_serving.client import BertClient
from sklearn.decomposition import pca
import pickle
import os
import xlrd


class FomcSpeech:
    mode = "train"
    max_len = 25
    words_dic = {}
    vocab_file = "./glove/glove.twitter.27B.25d.txt"
    speech_model = None
    text = None
    signal = None

    def __init__(self, mode, max_len):
        self.mode = mode
        self.max_len = max_len
        self.bc = BertClient()
        self.speech_model = speech_model(self.max_len + 1, self.mode)
        with open(self.vocab_file, 'r', encoding='utf-8') as f:
            words = [x.rstrip().split(' ') for x in f.readlines()]
            self.words_dic = {item[0]: item[1:] for item in words}
            words = None
        t = []
        s = []

        for item in os.listdir("./FOMC时间匹配"):
            df = pd.read_csv("./FOMC时间匹配/" + item)
            for sub in df['speech'].tolist():
                t.append(sub)
            for sub in df['finalover'].tolist():
                if sub == 1:
                    s.append(1)
                elif sub == 4:
                    s.append(2)
                else:
                    s.append(0)

        self.text = t
        self.signal = s
        self.pca = pca.PCA(n_components=25)

    # need to change !!!!!!
    def get_data(self, glove_words_dic, max_len):
        vector = []
        for item in self.text:
            temp = []
            word_tokens = keras.preprocessing.text.text_to_word_sequence(item)
            if len(word_tokens) < max_len:
                while len(word_tokens) < max_len:
                    word_tokens.append('-')
            for sub in word_tokens[:max_len]:
                if sub in glove_words_dic:
                    temp.append(glove_words_dic[sub])
                else:
                    temp.append(glove_words_dic['-'])
            vector.append(temp)
        label = self.signal
        '''
        for i in range(len(label)):
            if label[i] == -1:
                label[i] = 0
        '''
        return np.array(vector), np.array(label)

    def get_bert_vector(self, text):
        vec = self.bc.encode(text)
        if self.mode == 'test':
            with open('./pca.pickle', 'rb') as f:
                pca_model = pickle.load(f)
            vec = pca_model.transform(vec)
        else:
            pca_model = self.pca.fit(vec)
            with open('./pca.pickle', 'wb') as f:
                pickle.dump(pca_model, f)
            vec = pca_model.transform(vec)
        # with open('./pca.pickle', 'rb') as f:
        # self.pca_model = pickle.load(f)
        return vec

    def glove_bert_combine(self, g_vector, b_vector):
        temp = []
        for i, item in enumerate(g_vector):
            temp.append(np.vstack([item, b_vector[i]]))
        return np.array(temp)

    def get_real_data(self, text, glove_words_dic, max_len):
        vector = []
        assert type(text) == str
        word_tokens = keras.preprocessing.text.text_to_word_sequence(text)
        if len(word_tokens) < max_len:
            while len(word_tokens) < max_len:
                word_tokens.append('-')
        for sub in word_tokens[:max_len]:
            if sub in glove_words_dic:
                vector.append(glove_words_dic[sub])
            else:
                vector.append(glove_words_dic['-'])
        return np.array([vector])

    def train(self):
        vector, label = self.get_data(self.words_dic, self.max_len)
        bert_vector = self.get_bert_vector(self.text)
        print(bert_vector.shape)
        final_vec = self.glove_bert_combine(vector, bert_vector)
        print(final_vec.shape)
        label = keras.utils.to_categorical(label, num_classes=3)
        for i in label:
            # print(label)
            print(i)
        print(label)
        self.speech_model.train(final_vec[:int(0.8 * len(final_vec))], label[:int(0.8 * len(final_vec))],
                                final_vec[int(0.8 * len(final_vec)):],
                                label[int(0.8 * len(final_vec)):])

    def test(self, data):
        # print(data)
        vec = self.get_real_data(data, self.words_dic, self.max_len)
        bert_vec = self.get_bert_vector([data])
        final_vec = self.glove_bert_combine(vec, bert_vec)
        # print(final_vec)
        return self.speech_model.test(final_vec)


# x = FomcSpeech('train', 25)
# x.train()
if __name__ == '__main__':
    '''
    y = FomcSpeech('train', 25)
    y.train()
    exit()
    '''
    workspace = xlrd.open_workbook("./test_data/2019_10_31.xlsx")
    sheet = workspace.sheet_by_index(0)
    rows = sheet.col_values(1)[1:]
    y = FomcSpeech('test', 25)
    # y.train()
    signal = []
    for item in rows:
        res = y.test(item)
        signal.append(np.argmax(res[0]))
    print(signal)
    df = pd.DataFrame()
    df['signal'] = signal
    df.to_csv("signal.csv")
    # import re
    # pat = re.compile(r'[A-Za-z]')
    # '''

    exit()
