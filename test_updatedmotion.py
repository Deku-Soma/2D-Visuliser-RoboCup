import unittest
import tkinter as tk
import updatedmotion as motion

class MotionTest(unittest.TestCase):

    def test_loadJSONFile(self):
        testdata=motion.loadJSONFile(4, 1)
        checkdata=[]
        checkdata.append({"BallPosition":[0.0,0.0],"CurrGameTime":3.68,"CurrPlayMode":0,"CurrTime":3.68,"IsFallen":False,"MyPosition":[0.0,0.0],"OpponentPositions":{"OPP1":[0.0,0.0],"OPP10":[0.0,0.0],"OPP11":[0.0,0.0],"OPP2":[0.0,0.0],"OPP3":[0.0,0.0],"OPP4":[0.0,0.0],"OPP5":[0.0,0.0],"OPP6":[0.0,0.0],"OPP7":[0.0,0.0],"OPP8":[0.0,0.0],"OPP9":[0.0,0.0]},"TeamMateDistanceToBall":{"1":0.0,"10":0.0,"11":0.0,"2":0.0,"3":0.0,"4":0.0,"5":0.0,"6":0.0,"7":0.0,"8":0.0,"9":0.0},"TeamMatePositions":{"TEAM1":[0.0,0.0],"TEAM10":[0.0,0.0],"TEAM11":[0.0,0.0],"TEAM2":[0.0,0.0],"TEAM3":[0.0,0.0],"TEAM4":[0.0,0.0],"TEAM5":[0.0,0.0],"TEAM6":[0.0,0.0],"TEAM7":[0.0,0.0],"TEAM8":[0.0,0.0],"TEAM9":[0.0,0.0]}})
        checkdata.append({"Action":{"location":[-14.941847227983244,-0.07915494486260229],"type":"SKILL_STAND"},"BallPosition":[5.265403173197079,-2.5145983250388113],"CurrGameTime":617.16,"CurrPlayMode":8,"CurrTime":617.16,"IsFallen":False,"IsOffensive":True,"MyPosition":[-14.965486141009452,0.030141149615426927],"OpponentPositions":{"OPP1":[14.97822176899842,0.09688302974513263],"OPP10":[4.982725906758077,-4.950292158352977],"OPP11":[4.950529919297331,5.03233488270642],"OPP2":[7.448514282471695,0.01795116751300352],"OPP3":[8.439338833110622,-0.9397283189723344],"OPP4":[8.494916356592391,1.124516559473148],"OPP5":[1.5204942224800035,-2.9172882363461348],"OPP6":[1.4357015691653885,2.103351639892189],"OPP7":[3.9603513538610997,0.09597962541025096],"OPP8":[11.273557482813452,0.10230134404585112],"OPP9":[12.225658457864117,0.08917176313420683]},"TeamMateDistanceToBall":{"1":20.39030647277832,"10":9.953299522399902,"11":6.043966770172119,"2":3.740431070327759,"3":4.739761829376221,"4":4.389556884765625,"5":1.7131140232086182,"6":1.9880598783493042,"7":0.45446160435676575,"8":11.314191818237305,"9":14.222305297851563},"TeamMatePositions":{"TEAM1":[-14.965486141009452,0.030141149615426927],"TEAM10":[-0.4045335713138787,5.665865461449619],"TEAM11":[7.3090247674268305,0.9749972368773454],"TEAM2":[1.5715042655214937,-1.9264362443145728],"TEAM3":[1.1037364432191765,-0.2461465800859508],"TEAM4":[1.292269989057914,-4.380723305793494],"TEAM5":[4.723852399441512,-4.139862170588506],"TEAM6":[4.004480395568667,-0.9775700435204242],"TEAM7":[5.0125725169886834,-2.8922383910019467],"TEAM8":[-5.956084160193473,-1.0692079957637604],"TEAM9":[-8.7678370587818,-0.20329416405138823]},"isClosestTeam":False})
        self.assertEqual(checkdata[0], testdata[0])
        self.assertEqual(checkdata[1], testdata[len(testdata)-1])
    def test_convert(self):
        
        leftx=-15
        rightx=15
        topy=-10
        bottomy=10
        centrex=0
        centrey=0

        bottomleft=[]
        convLeftx=(leftx*24.6667)+395-10
        convLefty=(bottomy*23.5)+250-10
        bottomleft.append(convLeftx)
        bottomleft.append(convLefty)
        testdata=motion.convert(leftx,bottomy)
        self.assertEqual(bottomleft, testdata)

        topleft=[]
        convLeftx=(leftx*24.6667)+395-10
        convLefty=(topy*23.5)+250-10
        topleft.append(convLeftx)
        topleft.append(convLefty)
        testdata=motion.convert(leftx,topy)
        self.assertEqual(topleft, testdata)

        centreleft=[]
        convLeftx=(leftx*24.6667)+395-10
        convLefty=(centrey*23.5)+250-10
        centreleft.append(convLeftx)
        centreleft.append(convLefty)
        testdata=motion.convert(leftx,centrey)
        self.assertEqual(centreleft, testdata)

        bottomright=[]
        convRightx=(rightx*24.6667)+395-10
        convRighty=(bottomy*23.5)+250-10
        bottomright.append(convRightx)
        bottomright.append(convRighty)
        testdata=motion.convert(rightx,bottomy)
        self.assertEqual(bottomright, testdata)

        topRight=[]
        convRightx=(rightx*24.6667)+395-10
        convRighty=(topy*23.5)+250-10
        topRight.append(convRightx)
        topRight.append(convRighty)
        testdata=motion.convert(rightx,topy)
        self.assertEqual(topRight, testdata)
        
        centreRight=[]
        convRightx=(rightx*24.6667)+395-10
        convRighty=(centrey*23.5)+250-10
        centreRight.append(convRightx)
        centreRight.append(convRighty)
        testdata=motion.convert(rightx,centrey)
        self.assertEqual(centreRight, testdata)

        topMiddle=[]
        convMiddlex=(centrex*24.6667)+395-10
        convMiddley=(topy*23.5)+250-10
        topMiddle.append(convMiddlex)
        topMiddle.append(convMiddley)
        testdata=motion.convert(centrex,topy)
        self.assertEqual(topMiddle, testdata)
        
        bottomMiddle=[]
        convMiddlex=(centrex*24.6667)+395-10
        convMiddley=(bottomy*23.5)+250-10
        bottomMiddle.append(convMiddlex)
        bottomMiddle.append(convMiddley)
        testdata=motion.convert(centrex,bottomy)
        self.assertEqual(bottomMiddle, testdata)
        
        centreMiddle=[]

        convMiddlex=(centrex*24.6667)+395-10
        convMiddley=(centrey*23.5)+250-10
        centreMiddle.append(convMiddlex)
        centreMiddle.append(convMiddley)
        testdata=motion.convert(centrex,centrey)
        self.assertEqual(centreMiddle, testdata)

    
    def test_getAverageOpponentPosition(self):
        
        oppxPos=[14.959110351222593,7.448582009226044,8.429862050512012,8.480149913395248,1.5187971596584902,1.4436112303668935,3.9495223142934237,11.25790594910636,12.206695997356542,4.960377770904344,4.937213540568097]
        oppyPos=[0.028867057151962652,0.009058812369707887,-1.0147713231845763,1.0663328976821724,-3.0017380818630612,2.0221582858160367,0.061360912967456945,0.05666153017467856,0.021884447514461402,-5.002934403771056,4.967900134815649]
        oppAvgPos=[oppxPos,oppyPos]
        playerDataList=motion.writeGlobalJSONFile(4)
        testcase=motion.getAverageOpponentPosition(len(playerDataList)-1,playerDataList)
        self.assertEqual(oppAvgPos, testcase)
        

    def test_getAverageBallPosition(self):
        avgBallPos=[-0.12889475439030737, -0.02734743095369824]
        playerDataList=motion.writeGlobalJSONFile(4)
        testcase=motion.getAverageBallPosition(2,playerDataList)
        self.assertEqual(avgBallPos, testcase)

        avgBallPos=[[5.253981910171334, -2.5822221153879763]]
        playerDataList=motion.writeGlobalJSONFile(4)
        testcase=motion.getAverageBallPosition(len(playerDataList)-1,playerDataList)
        self.assertEqual(avgBallPos, testcase)

    

    if __name__ == '__main__':
        unittest.main()
