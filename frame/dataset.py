import pandas as pd


class Dataset(object):
    def __init__(self, df_train, df_test, label_col_name):
        """
        :param df_train:DataFrame, contain the column of label
        :param df_test: Dataframe, don't contain label
        :param label_col_name: string, the name of label
        """
        self.label_name = label_col_name
        self.len_train = len(df_train)
        self.len_test = len(df_test)

        df_train = self.drop_cols(df_train, [label_col_name])

        self.df_all = pd.concat([df_train, df_test], ignore_index=True)

    @staticmethod
    def drop_cols(df, list_cols):
        return df.drop(labels=list_cols, axis=1)

    def get_df_train(self):
        """
        get train data set from the concat of train and test
        :return:
        """
        return self.df_all.loc[:self.len_train, :]

    def get_df_test(self):
        """
        get test data set from the concat of train and label
        :return:
        """
        return self.df_all.loc[self.len_train:, :]
