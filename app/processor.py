import os

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
class Processor:
    def __init__(self):
        self.df = None
        self.id = None
        self.sentiment = None
        self.tweets_df = None
        self.rarest_word = None
        self.original_text = None
        self.weapons_detected = None

    def process(self, df):
        """
        Enable all the process functions.
        :return:
        """
        self.df = df
        self.id = self.df["TweetID"]
        self.original_text = self.df["Text"]
        self.tweets_df = self.convert_text_to_rows_df()
        self.sentiment = self.find_emotional_status_text()
        self.rarest_word = self.find_rare_word()
        self.weapons_detected = self.find_weapon()
        return self.join_series()

    def convert_text_to_rows_df(self):
        """
        Converting the columns `Text` to df, that each row
        is one tweet text.
        Each Statement is a word.
        :return: DataFrame
        """
        return self.original_text.str.split(" ", expand=True)

    def find_rare_word(self):
        """
        Run on each text.
        Find the rarely word, adding it to a new column.
        By:
         1. Split each text to new df column.
         2. Do value_counts.
         3. Sort By.
         4. Get the first.
         5. Add the result to the original df to a rare_word column.
        :return:

        """
        rares_words = pd.Series()
        for i in range(self.tweets_df.shape[0]):
            series = self.tweets_df.iloc[i]
            counts_word = series.value_counts().sort_values().head(1)
            rares_words = pd.concat([rares_words, counts_word], axis=0)
        return rares_words

    def find_emotional_status_text(self):
        """
        Calculate an emotional ttype of a text.
        By using external Module.
        The emotion can be one of them: negative, positive, neutral.
        :return:
        """
        def absolute_emotion(_emotion_index):
            """
            Receive a dictionary of emotients, and return an emotion.
            :param _emotion_index:
            :return: Series
            """
            compound = _emotion_index["compound"]
            if compound > 0.5:
                return pd.Series("positive")
            elif compound > -0.49:
                return pd.Series("neutral")
            else:
                return pd.Series("negative")

        nltk.download('vader_lexicon', download_dir="../data/")
        emotional = pd.Series()
        for i in range(self.original_text.size):
            emotion_index = SentimentIntensityAnalyzer().polarity_scores(self.original_text.iloc[i])
            emotional = pd.concat([emotional, absolute_emotion(emotion_index)])
        return emotional

    def find_weapon(self):
        """
        Search a weapon in a text.
        By:
        1. Split each text to new df column.
         2. Do value_counts.
         3. Match them.
         4. Get the first.
         5. Add the result to the original df to a weapon column.
        :return:
        """
        return self.original_text

    def join_series(self):
        df = pd.DataFrame()
        df["id"] = self.id
        df["original_text"] = self.original_text
        df["rarest_word"] = self.rarest_word
        df["sentiment"] = self.sentiment
        df["weapons_detected"] = self.weapons_detected
        return df




