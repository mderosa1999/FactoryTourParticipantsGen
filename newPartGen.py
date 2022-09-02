import pickle
import numpy as np

def newPartGen():
    with open('listAug', 'rb') as laug:
        listAugust = pickle.load(laug)

    with open('listAug', 'rb') as lsep:
        listSeptember = pickle.load(lsep)

    with open('apAug', 'rb') as aug:
        apAugust = sorted(pickle.load(aug))

    with open('apSep', 'rb') as sep:
        apSeptember = sorted(pickle.load(sep))

    with open('ListAug', 'wb') as laug:
        pickle.dump(list(set(listAugust) - set(apAugust)), laug)

    with open('ListSep', 'wb') as lsep:
        pickle.dump(list(set(listSeptember) - set(apSeptember)), lsep)

    print('August:      ' + str(apAugust))
    print('September:   ' + str(apSeptember))
    print('a=August, s=September')
    indicator = input('Aus welcher Teilnehmerliste hat jemand abgesagt ?')
    quit = 0

    if (indicator == 'a'):
        while quit == 0:
            enf = int(input('Welche ID hat der Teilnehmer der abgesagt hat ?'))
            if enf not in apAugust:
                quit = 1
            if enf in apAugust:
                apAugust.remove(enf)
                ins = np.random.choice(listAugust)
                listAugust.remove(ins)
                print('Der neue Teilnehmer ist -->', ins)
                apAugust = list(np.append(apAugust, ins))
                print(apAugust)

            a = input('Hat eine weitere Person abgesagt? Y/N')
            if a == 'N':
                with open('apAug', 'wb') as aug:
                    pickle.dump(apAugust, aug)
                print('August:      ' + str(apAugust))
                print('September:   ' + str(apSeptember))
                quit = 1

    if (indicator == 's'):
        while quit == 0:
            enf = int(input('Welche ID hat der Teilnehmer der abgesagt hat ?'))
            if enf not in apSeptember:
                quit = 1
            if enf in apSeptember:
                apSeptember.remove(enf)
                ins = np.random.choice(listSeptember)
                listSeptember.remove(ins)
                print('Der neue Teilnehmer ist -->', ins)
                apSeptember = list(np.append(apSeptember, ins))
                print(apSeptember)

            a = input('Hat eine weitere Person abgesagt? Y/N')
            if a == 'N':
                with open('apSep', 'wb') as sep:
                    pickle.dump(apSeptember, sep)
                print('August:      ' + str(apAugust))
                print('September:   ' + str(apSeptember))
                quit = 1


newPartGen()
