from sklearn import tree
import pandas as pd


def prepocesing(datapath):
    d = pd.read_csv(datapath, sep=',')
    len(d)

    # shuffle data
    d = d.sample(frac=1)
    d_train = d[:3400]
    d_test = d[3000:]

    d_train_att = d_train.drop(['label'], axis=1)
    d_train_pass = d_train['label']

    d_test_att = d_test.drop(['label'], axis=1)
    d_test_pass = d_test['label']

    d_att = d.drop(['label'], axis=1)
    d_pass = d['label']
    return d_train_att, d_train_pass, d_test_att, d_test_pass, d_att, d_pass


def training(d_train_att, d_train_pass):
    t = tree.DecisionTreeClassifier(criterion="entropy", max_depth=5)
    t = t.fit(d_train_att, d_train_pass)
    return t


def testing(t, testdataframe):
    return t.predict(testdataframe)