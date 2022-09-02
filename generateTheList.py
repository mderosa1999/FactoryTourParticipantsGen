import pickle
import random


def initPartLists():
    listAugust = [4, 5, 6, 7, 12, 13, 14, 16, 17, 18, 20, 21, 23, 25, 26, 27, 28, 29, 30, 33, 35, 36, 39, 40, 43, 45,
                  48, 49, 53, 57, 58, 59, 61, 62, 63, 65, 70, 71, 72, 76, 77, 80]
    listSeptember = [1, 2, 3, 8, 9, 10, 11, 15, 19, 22, 24, 31, 32, 34, 37, 38, 41, 42, 44, 46, 47, 50, 51, 52, 54, 55,
                     56, 60, 64, 66, 67, 68, 69, 73, 74, 75, 78, 79, 81, 82]
    random_august = random.sample(listAugust, 20)
    random_september = random.sample(listSeptember, 20)

    with open('apAug', 'wb') as aug:
        pickle.dump(random_august, aug)

    with open('apSep', 'wb') as sep:
        pickle.dump(random_september, sep)

    with open('ListAug', 'wb') as laug:
        pickle.dump(listAugust, laug)

    with open('ListSep', 'wb') as lsep:
        pickle.dump(listSeptember, lsep)


def showParticipants():
    with open('apAug', 'rb') as aug:
        partAug = pickle.load(aug)

    with open('apSep', 'rb') as sep:
        partSep = pickle.load(sep)

    print('Die Teilnehmer für den Termin im August besitzen die IDs     ' + str(partAug))
    print('Die Teilnehmer für den Termin im September besitzen die IDs  ' + str(partSep))

initPartLists()
showParticipants()

