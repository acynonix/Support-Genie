from main_functions import agent_available, random_agent, avail_since_long, data, issue_category
import unittest

class Test_main_functions(unittest.TestCase):
    def test_agent_available(self):
        self.assertEqual(agent_available(data, issue_category), [('agent_1', [11, 59, 0], ['Spanish Speaker', 'Support']), ('agent_2', [12, 0, 0], ['Spanish Speaker'])])

    def test_avail_since(self):
        self.assertEqual(avail_since_long(), ('agent_1', [11, 59, 0], ['Spanish Speaker', 'Support']))

if __name__=='__main__':
    unittest.main()