import unittest
import byzantine

class Tol(unittest.TestCase):
    def test_tol_00(self):
        self.assertEqual(byzantine.traitor_or_loyal(False, False), False)
    def test_tol_01(self):
        self.assertEqual(byzantine.traitor_or_loyal(False, True), True)
    def test_tol_10(self):
        self.assertEqual(byzantine.traitor_or_loyal(True, False), True)
    def test_tol_11(self):
        self.assertEqual(byzantine.traitor_or_loyal(True, True), False)

class TL(unittest.TestCase):
    def test_tl_40(self):
        self.assertEqual(byzantine.traitorous_lieutenants(4, False), 4)
    def test_tl_41(self):
        self.assertEqual(byzantine.traitorous_lieutenants(4, True), 3)

class CA(unittest.TestCase):
    def test_ca_0000(self):
        self.assertEqual(byzantine.count_actions(True, [False, False, False, False]), 0)
    def test_ca_0001(self):
        self.assertEqual(byzantine.count_actions(True, [False, False, False, True]), 1)
    def test_ca_0011(self):
        self.assertEqual(byzantine.count_actions(True, [False, False, True, True]), 2)
    def test_ca_0111(self):
        self.assertEqual(byzantine.count_actions(True, [False, True, True, True]), 3)

class Cons(unittest.TestCase):
    #TODO: Test sorting
    def test_cons_0000(self):
        self.assertEqual(byzantine.consensus([False, False, False, False]), False)
    def test_cons_0001(self):
        self.assertEqual(byzantine.consensus([False, False, False, True]), False)
    def test_cons_0011(self):
        self.assertEqual(byzantine.consensus([False, False, True, True]), False)
    def test_cons_0111(self):
        self.assertEqual(byzantine.consensus([False, True, True, True]), True)
    def test_cons_00000(self):
        self.assertEqual(byzantine.consensus([False, False, False, False, False]), False)
    def test_cons_00001(self):
        self.assertEqual(byzantine.consensus([False, False, False, False, True]), False)
    def test_cons_00011(self):
        self.assertEqual(byzantine.consensus([False, False, False, True, True]), False)
    def test_cons_00111(self):
        self.assertEqual(byzantine.consensus([False, False, True, True, True]), True)
    def test_cons_01111(self):
        self.assertEqual(byzantine.consensus([False, True, True, True, True]), True)

class Byz(unittest.TestCase):
    def test_byz_num_params(self):
        with self.assertRaises(IndexError):
            byzantine.byzantine(7, 8, False)
    #TODO: when number of generals is negative
    #TODO: when traitors are negative
    #TODO: when commander is traitor but 0 traitors

if __name__ == '__main__':
    unittest.main()
