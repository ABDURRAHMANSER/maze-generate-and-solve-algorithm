import random
import time
import matplotlib.pyplot as plt
from PIL import Image
class slow_one():
    RIGHT = [0, 1]  # deteermain the move busetion
    DOWN = [1, 0]
    LEFT = [0, -1]
    UP = [-1, 0]
    l1 = [RIGHT, DOWN, LEFT, UP]
    def __init__(self):
        self.numOfCol, self.NumOfRow = 50,50
        self.image_color = [(0, 0, 128), (250, 1, 1), (204, 0, 204), (255, 236, 139), (255, 105, 180), (119, 172, 152),
                            (0, 100, 0), (238, 232, 170), (240, 189, 122), (220, 225, 219), (238, 59, 59),
                            (0, 255, 255), (139, 139, 0), (127, 255, 0), (0, 238, 238), (255, 105, 180), (255, 52, 179),
                            (255, 255, 0)]
        self.mainArray1=[]
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
        self.process_time=[[] for one in range(self.roadinput)]
        return  self.int1x,self.int1y,self.endx,self.endy,  self.roadinput
    def evolve(self):
        self.int1x, self.int1y, self.endx,self.endy, self.roadinput= self.take_inputs() #pass inputs
        for i in range( self.roadinput):              #generat my mazes
            self.mainArray =[[0 for one in range(self.NumOfRow)] for tow in range(self.numOfCol) ]#creat our list
            start = time.time()
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
            self.mainArray1.append(self.mainArray)
            end = time.time()
            self.process_time[i].append(end - start)
            print('process time generat',end-start)
    def plot_dataa(self): #creat my plot function
        plt.boxplot(self.process_time)
        plt.show()
    def photo_outout (self,drow,location) :  #NOT:the left sidre of the image in the batume in our foto
        img1 = Image.new('RGB', (len(drow),len(drow[0])), color=0)  # midean filter images
        for x in range(len(drow)):
            for y in range(len(drow[0])):
                if drow[x][y]!=0:
                    img1.putpixel((x,y),self.image_color[drow[x][y]])
                else:
                    img1.putpixel((x, y), 0)
        img1.save(location)
        img1.show()

SO= slow_one()
SO.evolve()
SO.plot_dataa()
SO.photo_outout(SO.mainArray1,'C:\\Users\\Abdulrrahman\\GMT203\\maze1234.tif')