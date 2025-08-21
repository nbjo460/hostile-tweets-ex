import os

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
class Processor:
    def __init__(self):
        self.df = None

    def process(self, df):
        """
        Enable all the process functions.

        :return:
        """
        self.df = df
        self.find_rare_word()
        self.get_emotional_status_text()

    def find_rare_word(self):
        """
        Run on each text.
        Find the rarely word, adding it to a new column.
        By:
         1. Split each text to new df column.
         2. Do value_counts.
         3. Sort By.
         4. Get the first
         5. Add the result to the original df.
        :return:

        """

    def find_emotional_status_text(self):
        """
        Calculate an emotional ttype of a text.
        By using external Module.
        The emotion can be one of them: negative, positive, neutral.
        :return:
        """
        nltk.download('vader_lexicon', download_dir="../data/",q)
        tweet = 'i dont love to kill, but i have to kill'
        result = SentimentIntensityAnalyzer().polarity_scores(tweet)
        print(result, "../../data")

    def find_weapon(self):
        """
        Search a weapon in a text.
        By:
        :return:
        """
p = Processor()
p.process()