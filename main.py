import dagger


def main(infile):
    myDagger = dagger.dagger(infile)
    myDagger.makeTopo()
    myDagger.backTrace()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('test.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
