
import pandas as pd

class Saving():
    def __init__(self):
        self.name = False
        self.difficulty = False
        self.score = 0

    def save(self):
        saving = pd.DataFrame([[self.name, self.difficulty, self.score]], columns=['name','difficulty','score'])
        saving.to_csv('savings/savings.csv', mode='a', header=False)
