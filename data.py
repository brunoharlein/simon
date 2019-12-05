
import pandas as pd

if __name__ == '__main__':
    savings = pd.read_csv('savings/savings.csv')

    print("\n-------- Liste des parties sauvegardées -----------\n")
    print(savings.to_string(index=False))


    print("\n-------- Statistiques -----------\n")
    print("Score moyen : {}".format(round(savings['score'].mean())))
    print("Score médian : {}".format(savings['score'].median()))

    print("\nMoyenne par difficulté :\n")
    difficulties = sorted(savings['difficulty'].unique())
    for difficulty in difficulties:
        savings_by_dif = savings[savings['difficulty']==difficulty]
        print("Difficulté de niveau {} -> score moyen : {}".format(difficulty, round(savings_by_dif['score'].mean())))

    print("\nMoyenne par joueur :\n")
    names = sorted(savings['name'].unique())
    for name in names:
        savings_by_name = savings[savings['name']==name]
        print("Joueur : {} -> score moyen : {}".format(name, savings_by_name['score'].mean()))
