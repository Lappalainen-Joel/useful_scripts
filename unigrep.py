#!/usr/bin/python3.5
#
#   "Poor mans version of grep, for windows"
#   Can be used with multiple keywords,
#   and with multiple files.
#
#   Searches given text file(s) from line-to-
#   line, and tries to match given keyword(s).
#
#   Match all keywords:
#   $ unigrep.py <keyword1, keyword2> <filename>
#
#   Match any of the given keywords:
#   $ unigrep.py -or <keyword1, keyword2> <filename>
#
#   With multiple files:
#
#   Match all given keywords in given filenames:
#   $ unigrep.py <keyword1, keyword2> -f <filename1> <filename2>
#
#   By default with multiple files, matching filename is printed out
#   with matching line. This can be disabled with:
#   $ unigrep.py -q <keyword1> -f <filename1> <filename2>
#
#   Searching via regex:
#   $ unigrep.py -r <regex_pattern> <filename>
#
#   Author Joel Lappalainen


from sys import argv
from re import match, compile

def createRegexPattern(argslist):
    pattern = ""
    for i in argslist:
        if i == '-f':
            return pattern
        elif i != '-o' and i != '-q' and i != '-r':
            pattern = i
    pattern = argslist[-2]
    return pattern


def createKeywordList(argslist):
    keywordList = []
    for i in argslist:
        if i == '-f':
            return keywordList
        elif i != '-o' and i != '-q' and i != '-r':
            keywordList.append(i)
    return keywordList[:-1]


def createFileList(argslist):
    start = 0
    fileList = []
    for i in argslist:
        if i == '-f':
            start = 1
        elif start == 1:
            fileList.append(i)
    if start == 0:
        fileList.append(argslist[-1])
        return fileList
    return fileList


def listanymatches(file, keywordList, mfiles):
    for row in file.readlines():
        if any(keyword in row for keyword in keywordList):
            print_checker(file, row, mfiles)
    file.close()


def listallmatches(file, keywordList, mfiles):
    for row in file.readlines():
        if argslistl(keyword in row for keyword in keywordList):
            print_checker(file, row, mfiles)
    file.close()


def listregexmatches(file, pattern, mfiles):
    pat = compile('%s' % pattern)
    for row in file.readlines():
        if match(pattern,row):
            print_checker(file, row, mfiles)
    file.close()


def print_checker(file, row, mfiles):
    if mfiles == 1:
        print(file.name + ': ' + row)
    else:
        print(row)


def main():
    listany = 0
    mfiles = 0
    regex = 0

    if '-f' in argv:
        mfiles = 1
    else:
        fileList = []
        fileList.append(argv[-1])
    if '-or' in argv:
        listany = 1
    if '-q' in argv:
        mfiles = 0
    if '-r' in argv:
        regex = 1
    fileList = createFileList(argv[1:])

    if regex == 1:
        regexPattern = createRegexPattern(argv[1:])
    else:
        keywordList = createKeywordList(argv[1:])

    for file in fileList:
        f = open(file, 'r')
        if listany == 1:
            listanymatches(f, keywordList, mfiles)
            exit(0)
        elif regex == 1:
            listregexmatches(f, regexPattern, mfiles)
            exit(0)
        else:
            listallmatches(f, keywordList, mfiles)
            exit(0)


main()
