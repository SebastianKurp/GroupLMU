import unittest
from report_by_symbol import *
from search import *
from topological_sort import *

class testNotes(unittest.TestCase):
    def testSearchTerm(self):
        fileContents = ['this is a sentence.\nSentences verbalize a thought.\nI like the letter a.\n', 'a a\na\n']
        fileNames = ['file1','file2']
        output =    [
                        [
                            'file1', 
                            ['a', '...  is a sen ...', 0, 8, 8], 
                            ['a', '... ize a tho ...', 1, 8, 8], 
                            ['a', '... letter a.', 2, 11, 11]
                        ], 
                        [
                            'file2', 
                            ['a', 'a a', 0, 0, 0],
                            ['a', 'a a', 0, 2, 2],
                            ['a', 'a', 1, 0, 0]
                        ]
                    ]
        assert search(fileContents,fileNames,'a',10), 'search for [a]: incorrect output.'

    def testHighlightSearch(self):
        fileContents = ['this is a sentence.\nSentences verbalize a thought.\nI like the letter a.\n', 'a a\na\n']
        fileNames = ['file1','file2']
        hl = [
                [
                    [0,10],
                    [20,45]
                ],
                [
                ]
            ]
        output =    [
                        [
                            'file1',
                            ['a', 'this is a ', 0, 8, 8],
                            ['a', '... ize a tho ...', 1, 8, 8]
                        ]
                    ]
        assert search(fileContents, fileNames, 'a', 10, highlight = hl) == output, 'search for [a] with highlights: incorrect output.'

    def testReportSymbol(self):
        fileContents = ['line1\n#topic1\nline2\non line 4 we have @id1\nline3\n','line1\nline2\nline3\nOn line 4 @id2 is here.\nOn line 5 @id3 is here\n']
        fileNames = ['file1','file2']
        output =    [
                        [
                            'file1',
                            ['@id1', '... have @id1',3,9,12]
                        ],
                        [
                            'file2',
                            ['@id2', '...  4 @id2 is ...',3,7,10],
                            ['@id3', '...  5 @id3 is ...',4,7,10]
                        ]
                    ]
        assert reportBySymbol(fileContents,fileNames,'@',10, style = 'by note') == output, "report mentions by note: incorrect output."

    def testOrganizeBySymbol(self):
        fileContents = ['line1\n#topic1\nline2\non line 4 we have #topic2\nline3\n','line1\nline2\nline3\nOn line 4 #topic2 is here.\nOn line 5 @id3 is here\n']
        fileNames = ['file1','file2']
        output =    [
                        [
                            '#topic1',
                            ['file1']
                        ],
                        [
                            '#topic2',
                            ['file1','file2']
                        ]
                    ]
        assert reportBySymbol(fileContents,fileNames,'#',style = 'by symbol') == output, "report notes by keyword: incorrect output."

    def testTopologicalSort(self):
        fileContents = ['!id1, ^id2 and ^id3 also ^id4','!id2 is connected to ^id1 and ^id4','!id3 is also connected to ^id1','!id4']
        fileNames = ['file1','file2','file3','file4']
        output =    [
                        ['file4', 2, 0],
                        ['file2', 1, 2],
                        ['file3', 1, 1],
                        ['file1', 0, 3]
                    ]
        assert topologicalSort(fileContents, fileNames) == output, "topologicalSort: incorrect output."

unittest.main()