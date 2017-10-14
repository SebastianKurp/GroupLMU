import unittest
from report_mentions import reportMentions
from organize_by_mention import organizeByMention
from report_keywords import reportKeywords
from search_term import searchTerm
from notes_by_keyword import notesByKeyword
from topological_sort import topologicalSort

class testNotes(unittest.TestCase):
    def testReportMentions(self):
        fileContents = [['line1','#topic1','line2','@id1','line3'],['line1','line2','line3','@id2','#topic2']]
        fileList = ['file1.txt','file2.txt']
        soln = ''
        soln += '+------------------+\n'
        soln += '| Mentions Report: |\n'
        soln += '+------------------+\n'
        soln += '\n'
        soln += 'file1.txt\n'
        soln += '\t@id1\n'
        soln += '\t#topic1\n'
        soln += 'file2.txt\n'
        soln += '\t@id2\n'
        soln += '\t#topic2\n'
        assert reportMentions(fileContents,fileList) == soln, "reportMentions: incorrect output"
        
    def testOrganizeByMention(self):
        fileContents = [['line1','#topic1','line2','@id1','line3'],['line1','line2','line3','@id2','#topic1']]
        fileList = ['file1.txt','file2.txt']
        soln = ''
        soln += '+-----------------------------+\n'
        soln += '| Notes organized by Mention: |\n'
        soln += '+-----------------------------+\n'
        soln += '\n'
        soln += '@id1\n'
        soln += '\tfile1.txt\n'
        soln += '@id2\n'
        soln += '\tfile2.txt\n'
        soln += '#topic1\n'
        soln += '\tfile1.txt\n'
        soln += '\tfile2.txt\n'
        assert organizeByMention(fileContents,fileList) == soln, "organizeByMention: incorrect output"
        
    def testReportKeywords(self):
        fileContents = [['word1 word2 word3','word4 word5 word6','word7 word8 word9'],['word1 word1 word1','word2 word3 word4']]
        fileList = ['file1.txt','file2.txt']
        assert reportKeywords(fileContents,fileList,'l',2,2) == ['word1','word2','word3','word4'], 'reportKeywords: incorrect output'
        assert reportKeywords(fileContents,fileList,'l',2,4) == ['word1'], 'reportKeywords: incorrect output'
        
    def testSearchTerm(self):
        fileContents = [['word1 word2 word3','word4 word5 word6','word7 word8 word9'],['word1 word1 word1','word2 word3 word4']]
        fileList = ['file1.txt','file2.txt']
        soln = ''
        soln += '+------------------------+\n'
        soln += '| Search for term: word1 |\n'
        soln += '+------------------------+\n'
        soln += '\n'
        soln += 'file1.txt\n'
        soln += '\tfound 1 times.\n'
        soln += 'file2.txt\n'
        soln += '\tfound 3 times.\n'
        assert searchTerm(fileContents,fileList,'word1') == soln, 'searchTerm: incorrect output'
        
    def testNotesByKeyword(self):
        fileContents = [['word1 word2 word3','word4 word5 word6','word7 word8 word9'],['word1 word1 word1','word2 word3 word4']]
        fileList = ['file1.txt','file2.txt']
        soln = ''
        soln += '+------------------------------------------------+\n'
        soln += '| Notes by Keyword (found in at least 2 file(s)) |\n'
        soln += '| (minimum 2 keyword occurrence(s)):             |\n'
        soln += '+------------------------------------------------+\n'
        soln += '\n'
        soln += 'word1\n'
        soln += '\tfile1.txt\n'
        soln += '\tfile2.txt\n'
        assert notesByKeyword(fileContents,fileList,2, 2) == soln, 'notesByKeyword: incorrect output'
        
    def testTopologicalSort(self):
        fileContents = [['!id1','^id2','^id3'],['!id2','^id3','word1 word2'],['!id3','word1 word2 word3']]
        fileList = ['file1.txt','file2.txt','file3.txt']
        soln = ''
        soln += '+----------------------------+\n'
        soln += '| Notes topologically sorted |\n'
        soln += '| (Sorted by indegree):      |\n'
        soln += '+----------------------------+\n'
        soln += '\n'
        soln += 'file3.txt\n'
        soln += '\tIndegree: 2; Outdegree: 0\n'
        soln += 'file2.txt\n'
        soln += '\tIndegree: 1; Outdegree: 1\n'
        soln += 'file1.txt\n'
        soln += '\tIndegree: 0; Outdegree: 2\n'
        assert topologicalSort(fileContents,fileList) == soln, 'topologicalSort: incorrect output'
        
unittest.main()
