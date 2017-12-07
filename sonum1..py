import random
from Stack import *
import time
from PIL import Image
class rowde:
    RIGHT =[0,1] #deteermain the move busetion
    DOWN =[1,0]
    LEFT =[0,-1]
    UP =[-1,0]
    l1=[RIGHT,DOWN,LEFT,UP]
    def __init__(self):
        self.numOfCol,self.NumOfRow = 50,50 #the leghnt of our maze
        self.threeDlist=[]
        self.image_color=[(0, 0, 128),(255,236,139),(119, 172, 152),(238,59,59),(0,255,255),(139,139,0),(127,255,0),(0,238,238),(255,105,180),(255,52,179),(255,255,0)]
        self.image_roud1=[]
        self.god_one = [['*' for one in range(self.NumOfRow)] for tow in range(self.numOfCol)]
        self.mainArray1 = [[0 for one in range(self.NumOfRow)] for tow in range(self.numOfCol)]#the final list for generat more then one rowde
    def take_inputs(self): #take start,end inputs
        self.int1 = str(input("write the start cordinate in the format num of colume,numer of the row: "))
        self.int1=self.int1.split(',')
        self.int1x = int(self.int1[0])
        self.int1y = int(self.int1[1])
        self.int2 = str(input("write the End cordinate in the format num of colume,numer of the row: "))
        self.int2=self.int2.split(',')
        self.endx = int(self.int2[0])
        self.endy = int(self.int2[1])
        self.roudinput=int(input('please enter the number of the rouds that you want to generat: '))
        return  self.int1x,self.int1y,self.endx,self.endy,  self.roudinput
    def evolve(self):
        self.int1x, self.int1y, self.endx,self.endy, self.roudinput= self.take_inputs() #pass inputs
        for i in range( self.roudinput):              #generat my mazes
            start = time.time()
            self.mainArray =[[0 for one in range(self.NumOfRow)] for tow in range(self.numOfCol) ]#creat our list
            break1 = True
            self.l2 = []  # creat strt move coor. list
            self.l3 = []  # creat the end move coor list
            self.num_row_start = self.int1y
            self.num_col_start = self.int1x
            self.num_row_end = self.endy
            self.num_col_end = self.endx
            while break1==True:
                try:
                    self.mainArray[self.num_row_end][self.num_col_end] = 1
                    self.l2.append([self.num_row_end, self.num_col_end])
                    self.mainArray[self.num_row_start][self.num_col_start] = 1
                    self.l3.append([self.num_row_start, self.num_col_start])
                except:
                    pass
                self.end_rand = random.choice(rowde.l1)
                self.start_rand = random.choice(rowde.l1)
                self.num_col_end=self.num_col_end+self.end_rand[0]
                self.num_row_end = self.num_row_end + self.end_rand[1]
                self.num_col_start = self.num_col_start + self.start_rand[0]
                self.num_row_start = self.num_row_start + self.start_rand[1]
                if self.num_row_start <0 : # all this probebilty to make the brogram stay in the list range
                    self.num_row_start=self.num_row_start*-1
                elif  self.num_row_start>self.numOfCol-1:
                    self.num_row_start = self.num_row_start -1
                if self.num_col_start <0 :
                    self.num_col_start=self.num_col_start*-1
                elif  self.num_col_start>self.numOfCol -1   :
                    self.num_col_start = self.num_col_start -1
                if self.num_col_end <0 :
                    self.num_col_end=self.num_col_end*-1
                elif  self.num_col_end>self.numOfCol-1:
                    self.num_col_end = self.num_col_end -1
                if self.num_row_end <0 :
                    self.num_row_end = self.num_row_end * -1
                elif  self.num_row_end >self.numOfCol-1:
                    self.num_row_end = self.num_row_end  -1
                check_tgret1=-1
                for tagret1 in self.l2 :
                    check_tgret1+=1
                    if [self.num_row_end ,self.num_col_end] ==tagret1:
                        #we make this bart of the code for make the progarm do not over go to the same coordinate
                        recoord=self.l2[len(self.l2)-1]
                        self.num_row_end=recoord[0]
                        self.num_col_end=recoord[1]
                        del self.l2[check_tgret1]
                check_tgret=-1
                for tagret in self.l3:
                    check_tgret+=1
                    if[self.num_row_start,self.num_col_start] == tagret:
                        recoord2=self.l3[len(self.l3)-1]
                        self.num_row_start=recoord2[0]
                        self.num_col_start=recoord2[1]
                        del self.l3[check_tgret]
                for item in range( len(self.l2)):
                    if self.l2[item] in self.l3 or self.l2[-item] in self.l3 :           #SO I HAVE WROUD!!!!!!!
                        print('done',i+1)                                        #NOT we start from the front  and the back
                        for t in range (len(self.mainArray)):
                            print(self.mainArray[t])
                        break1=False
                        self.threeDlist.append(self.mainArray)
                        break
            end = time.time()
            print('process time',end-start)
    def solve(self):
        self.finaly = 0
        SK = Stack()
        for  the3dchecker in self.threeDlist:
            self.finaly+=1
            SK.push([self.endy, self.endx])
            self.break2 = True
            self.endx1=self.endy
            self.endy1 = self.endx
            the3dchecker[self.endx1][self.endy1]=2
            while self.break2 == True:              # maze solver ^_^ ^_^ ^_^
                passes = 0
                for dir in rowde.l1:                # RIGHT,DOWN,LEFT,UP
                    try:                          # using try.. to  except ringe out of the list error
                        if the3dchecker[dir[0] + self.endx1][dir[1] + self.endy1] == 1:
                            self.endx1 += dir[0] # change endx1 and endy1 !!!!!!!!
                            self.endy1 += dir[1]
                            the3dchecker[ self.endx1][ self.endy1] = 2  # pass wroud 2
                            if self.endx1 < 0:
                                self.endx1 = self.endx1 * -1
                            elif self.endy1 < 0:
                                self.endy1 = self.endy1 * -1
                            SK.push([self.endx1, self.endy1]) #push to my STACK !!!!
                            if (self.endx1==self.int1y) and (self.endy1==self.int1x):
                                self.break2 = False
                                break
                        else:
                            passes += 1          # increse pass
                        if passes == 4:          # close rowde
                            SK.pop()             #popo of my STACK  !!!!!!
                            the3dchecker[self.endx1][self.endy1] = '!' # close wroud
                            peek=SK.peek()
                            self.endx1 = peek[0]
                            self.endy1 = peek[1]
                            the3dchecker[peek[0]][peek[1]]=2
                        if SK.isEmpty == True:
                            print('no wroud')
                    except:                     # increse passes
                        passes += 1
                        if passes == 4:  # close rowde
                            SK.pop()  # popo of my STACK  !!!!!!
                            the3dchecker[self.endx1][self.endy1] = '!'  # close wroud
                            peek = SK.peek()
                            self.endx1 = peek[0]
                            self.endy1 = peek[1]
                            the3dchecker[peek[0]][peek[1]] = 2
                        if SK.isEmpty == True:
                            print('no wroud')
                            break
            for SK_adder in range(SK.size()):
                SKpeeker=SK.peek()
                row11=SKpeeker[0]
                col11 = SKpeeker[1]
                self.mainArray1[row11][col11]=self.finaly
                self.god_one[row11][col11] = str(self.finaly)
                SK.pop()                       #pop of my STACK !!!!
            print('finally one',self.finaly)
            self.image_roud1.append(self.finaly)
            for one in self.god_one:
                print(''.join((x for x in one)))
    def photo_outout (self,drow,location) :  #NOT:the left sidre of the image in the batume in our foto
        img1 = Image.new('RGB', (self.NumOfRow,self.numOfCol), color=0)  # midean filter images
        image_row=-1
        for x in drow:
            image_row+=1
            image_col = -1
            for y in x:
                image_col+=1
                for image_roud in self.image_roud1:
                    if y==image_roud:
                        img1.putpixel((image_row,image_col),self.image_color[y])
        img1.save(location)
        img1.show()



row=rowde()
row.evolve()
row.solve()
row.photo_outout(row.mainArray1,'C:\\Users\\Abdulrrahman\\python\\maze.tif')