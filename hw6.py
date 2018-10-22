import re
import unittest

def sumNums(fileName):
    inFile = open(fileName,'r')
    read_line = inFile.readlines()
    inFile.close()
    sumNum = 0
    finalList = []
    for line in read_line:
        line = line.rstrip()
        num_lists = re.findall('[0-9]+', line)

        for word in num_lists:
            finalList.append(int(word))

    for item in finalList:
        sumNum += item

    #print(finalList)
    #print(sumNum)

    return sumNum

def countWord(fileName, word):
    inFile = open(fileName, 'r')
    read_line = inFile.readlines()
    inFile.close()
    count = 0

    for line in read_line:
        word_list = re.findall(word + ('\\b'), line, re.IGNORECASE)
        for words in word_list:
            count += 1
    return count 

def listURLs(fileName):
    inFile = open(fileName, 'r')
    read_line = inFile.readlines()
    inFile.close()
    URLlist = []

    for line in read_line:
        line = line.rstrip()
        urls = re.findall(',*www.[a-zA-Z0-9]+.[a-z]{3}\S*', line)
        for url in urls:
            URLlist.append(url)

    return URLlist


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)

