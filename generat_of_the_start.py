import random
import time
class slow_one():
    RIGHT = [0, 1]  # deteermain the move busetion
    DOWN = [1, 0]
    LEFT = [0, -1]
    UP = [-1, 0]
    l1 = [RIGHT, DOWN, LEFT, UP]
    def __init__(self):
        self.numOfCol, self.NumOfRow = 10,10
    def take_inputs(self): #take start,end inputs
        self.int1 = str(input("write the start cordinate in the format num of colume,numer of the row: "))
        self.int1=self.int1.split(',')
        self.int1x = int(self.int1[0])
        self.int1y = int(self.int1[1])
        self.int2 = str(input("write the End cordinate in the format num of colume,numer of the row: "))
        self.int2=self.int2.split(',')
        self.endx = int(self.int2[0])
        self.endy = int(self.int2[1])
        self.roadinput=int(input('please enter the number of the rouds that you want to generat: '))
        return  self.int1x,self.int1y,self.endx,self.endy,  self.roadinput
    def evolve(self):
        self.int1x, self.int1y, self.endx,self.endy, self.roadinput= self.take_inputs() #pass inputs
        start = time.time()
        for i in range( self.roadinput):              #generat my mazes
            self.mainArray =[[0 for one in range(self.NumOfRow)] for tow in range(self.numOfCol) ]#creat our list
            break1 = True
            self.l2 = []  # creat strt move coor. list
            self.num_row_end = self.endy
            self.num_col_end = self.endx
            while break1==True:
                try:
                    self.mainArray[self.num_row_end][self.num_col_end] = 1
                    self.l2.append([self.num_row_end, self.num_col_end])
                except:
                    pass
                self.end_rand = random.choice(slow_one.l1)
                self.num_col_end=self.num_col_end+self.end_rand[0]
                self.num_row_end = self.num_row_end + self.end_rand[1]
                if self.num_col_end <0 :
                    self.num_col_end=self.num_col_end*-1
                elif  self.num_col_end>self.numOfCol-1:
                    self.num_col_end = self.num_col_end -1
                if self.num_row_end <0 :
                    self.num_row_end = self.num_row_end * -1
                elif  self.num_row_end >self.numOfCol-1:
                    self.num_row_end = self.num_row_end  -1
                for item in range( len(self.l2)):
                    if self.l2[item][0]== self.int1x and self.l2[item][1]== self.int1y:           #SO I HAVE WROUD!!!!!!!
                        print('done',i+1)                                        #NOT we start from the front  and the back
                        for t in range (len(self.mainArray)):
                            print(self.mainArray[t])
                        break1=False
                        break
            end = time.time()
            print('process time generat',end-start)

SO= slow_one()
SO.evolve()