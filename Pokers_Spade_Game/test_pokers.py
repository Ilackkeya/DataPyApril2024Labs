import unittest
import pokers

SA = 'SA'
SK = 'SK'
SQ = 'SQ'
SJ = 'SJ'
S2 = 'S2'
S3 = 'S3'
S4 = 'S4'
S5 = 'S5'
S6 = 'S6'
S7 = 'S7'
S8 = 'S8'
S9 = 'S9'
S10 = 'S10'


class MyTestCase(unittest.TestCase):
    #def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here
    def test_check_straight1(self):
         self.assertEqual(pokers.check_straight(S5, S6, S7), 7)
    def test_check_straight2(self):
        self.assertEqual(pokers.check_straight(S4, S6, S5), 6)
    def test_check_straight3(self):
        self.assertEqual(pokers.check_straight(SQ, SA, SK), 14)
    def test_check_straight4(self):
        self.assertEqual(pokers.check_straight(S5, S9, SA), 0)
    def test_check_straight5(self):
        self.assertEqual(pokers.check_straight(S2, S3, S5), 0)
    def test_check_3ofakind1(self):
        self.assertEqual(pokers.check_3ofa_kind(S2, S2, S2), 2)
    def test_check_3ofakind2(self):
        self.assertEqual(pokers.check_3ofa_kind(S4, S2, S6), 0)
    def test_check_3ofakind3(self):
        self.assertEqual(pokers.check_3ofa_kind(S4, S4, S6), 0)
    def test_check_3ofakind4(self):
        self.assertEqual(pokers.check_3ofa_kind(S5, S5, S5), 5)
    def test_royal_flush1(self):
        self.assertEqual(pokers.check_royal_flush(SQ, SK, SA), 14)
    def test_royal_flush2(self):
        self.assertEqual(pokers.check_royal_flush(S2, S3, S5), 0)
    def test_royal_flush3(self):
        self.assertEqual(pokers.check_royal_flush(SJ, SQ, SK), 0)
    def test_royal_flush4(self):
        self.assertEqual(pokers.check_royal_flush(SA, SA, SA), 0)

    def test_play_cards1(self):
        self.assertEqual(pokers.play_cards(S5, S5, S5, S2, S2, S2), -1)
    def test_play_cards2(self):
        self.assertEqual(pokers.play_cards(S4, S4, S4, S7, S7, S7), 1)
    def test_play_cards3(self):
        self.assertEqual(pokers.play_cards(S3, S4, S5, S2, S2, S2), -1)
    def test_play_cards4(self):
        self.assertEqual(pokers.play_cards(S3, S4, S5, S3, S4, S5), 0)
    def test_play_cards5(self):
        self.assertEqual(pokers.play_cards(SK, SQ, SA, S2, S2, S2), -1)
    def test_play_cards6(self):
        self.assertEqual(pokers.play_cards(S6, S5, S7, SK, SQ, SA), 1)
    def test_play_cards7(self):
        self.assertEqual(pokers.play_cards(S4, S5, S3, SK, SQ, SA), 1)

    def test_play_cards8(self):
        self.assertEqual(pokers.play_cards(S5, S5, S5, S4, S2, SK), 0)

    def test_play_cards9(self):
        self.assertEqual(pokers.play_cards(S2, S5, S4, SK, S10, S6), 0)

if __name__ == '__main__':
    unittest.main()
