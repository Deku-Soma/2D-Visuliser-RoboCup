import unittest
import tkinter as tk
import updatedmotion as motion

class MotionTest(unittest.TestCase):

    def test_loadJSONFile(self):
        testdata = motion.loadJSONFile('matches/match4/1')
        checkdata = [
            {
                "BallPosition": [0.0, 0.0],
                "CurrGameTime": 3.68,
                "CurrPlayMode": 0,
                "CurrTime": 3.68,
                "IsFallen": False,
                "MyPosition": [0.0, 0.0],
                "OpponentPositions": {
                    "OPP1": [0.0, 0.0],
                    "OPP10": [0.0, 0.0],
                    "OPP11": [0.0, 0.0],
                    "OPP2": [0.0, 0.0],
                    "OPP3": [0.0, 0.0],
                    "OPP4": [0.0, 0.0],
                    "OPP5": [0.0, 0.0],
                    "OPP6": [0.0, 0.0],
                    "OPP7": [0.0, 0.0],
                    "OPP8": [0.0, 0.0],
                    "OPP9": [0.0, 0.0]
                },
                "TeamMateDistanceToBall": {
                    "1": 0.0,
                    "10": 0.0,
                    "11": 0.0,
                    "2": 0.0,
                    "3": 0.0,
                    "4": 0.0,
                    "5": 0.0,
                    "6": 0.0,
                    "7": 0.0,
                    "8": 0.0,
                    "9": 0.0
                },
                "TeamMatePositions": {
                    "TEAM1": [0.0, 0.0],
                    "TEAM10": [0.0, 0.0],
                    "TEAM11": [0.0, 0.0],
                    "TEAM2": [0.0, 0.0],
                    "TEAM3": [0.0, 0.0],
                    "TEAM4": [0.0, 0.0],
                    "TEAM5": [0.0, 0.0],
                    "TEAM6": [0.0, 0.0],
                    "TEAM7": [0.0, 0.0],
                    "TEAM8": [0.0, 0.0],
                    "TEAM9": [0.0, 0.0]
                }
            },
            {
                "Action": {
                    "location": [-14.941847227983244, -0.07915494486260229],
                    "type": "SKILL_STAND"
                },
                "BallPosition": [5.265403173197079, -2.5145983250388113],
                "CurrGameTime": 617.16,
                "CurrPlayMode": 8,
                "CurrTime": 617.16,
                "IsFallen": False,
                "IsOffensive": True,
                "MyPosition": [-14.965486141009452, 0.030141149615426927],
                "OpponentPositions": {
                    "OPP1": [14.97822176899842, 0.09604822818654839],
                    "OPP10": [10.154198694956923, 17.671242827365364],
                    "OPP11": [12.752794597105344, 25.115067147215547],
                    "OPP2": [13.865471153797417, -3.6094544188297976],
                    "OPP3": [10.239588614420335, -11.154562304733983],
                    "OPP4": [9.081452005392038, -16.063609726535603],
                    "OPP5": [4.702365662442694, -19.696469979739683],
                    "OPP6": [0.001779180964224614, -20.0],
                    "OPP7": [-4.696807300514805, -19.699278675352965],
                    "OPP8": [-9.073473869505103, -16.07093645007153],
                    "OPP9": [-10.216668100919347, -11.165487756496955]
                },
                "TeamMateDistanceToBall": {
                    "1": 14.978173618342868,
                    "10": 11.481062734356044,
                    "11": 11.253692157179043,
                    "2": 13.880497987280679,
                    "3": 11.42220831570364,
                    "4": 10.405988973366022,
                    "5": 6.142469277107269,
                    "6": 0.001779180964224614,
                    "7": 6.13406310278362,
                    "8": 10.40586893515049,
                    "9": 11.387993879496225
                },
                "TeamMatePositions": {
                    "TEAM1": [14.941847227983244, -0.07915494486260229],
                    "TEAM10": [10.154198694956923, 17.671242827365364],
                    "TEAM11": [12.752794597105344, 25.115067147215547],
                    "TEAM2": [13.865471153797417, -3.6094544188297976],
                    "TEAM3": [10.239588614420335, -11.154562304733983],
                    "TEAM4": [9.081452005392038, -16.063609726535603],
                    "TEAM5": [4.702365662442694, -19.696469979739683],
                    "TEAM6": [0.001779180964224614, -20.0],
                    "TEAM7": [-4.696807300514805, -19.699278675352965],
                    "TEAM8": [-9.073473869505103, -16.07093645007153],
                    "TEAM9": [-10.216668100919347, -11.165487756496955]
                }
            }
        ]

        self.assertEqual(testdata, checkdata)

    def test_getAverageOpponentPosition(self):
        oppxPos = [10.0, 15.0, 20.0]
        oppyPos = [5.0, 10.0, 15.0]
        testdata = motion.getAverageOpponentPosition(oppxPos, oppyPos)
        checkdata = (15.0, 10.0)
        self.assertEqual(testdata, checkdata)

    def test_gui(self):
        root = tk.Tk()
        testdata = motion.gui(root)
        self.assertIsNone(testdata)

if __name__ == '__main__':
    unittest.main()
