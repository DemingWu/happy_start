import  gdal
from PIL import Image
import cv2
import numpy as np
import os

def getpartImg (file_path,count):
	
 #读取某一波段图片保存方便hough圆处理	
 dataset=gdal.Open(file_path)
 band=dataset.GetRasterBand(150)
 width=band.XSize
 height=band.YSize
 da=band.ReadAsArray(0,0,width,height)
 cv2.imwrite('circle.jpg',da*256)

 #将圆读出来并截成小图
 hhh=cv2.imread('circle.jpg')
 gray_img=cv2.cvtColor(hhh,cv2.COLOR_BGR2GRAY)
 #img=cv2.medianBlur(gray_img,5)#中值滤波
 circles=cv2.HoughCircles(gray_img,cv2.HOUGH_GRADIENT,1,320,param1=100,param2=30,minRadius=10,maxRadius=320)
 circles=np.uint16(np.around(circles))
 #start_x=circles[0][0][0]-circles[0][0][2]
 #start_y=circles[0][0][1]-circles[0][0][2]
 #num=circles[0][0][2]*2
 start_x=circles[0][0][0]-70
 start_y=circles[0][0][1]-70
 test_da=[]
 #print(num)
 for i in range(140):
	 temp=[]
	 start_y=start_y+1
	 for j in range(140):
	 	temp.append(da[start_y][start_x+j])
	 test_da.append(temp)	
 x=np.array(test_da)*256
 #print(str)
 #if count==102:
 # print(str)
 #str=str[28:len(str)-3]
 #str=str+"jpg"
 #print(str)
 file_path=str(count)+".jpg"
 cv2.imwrite(file_path,x)
 
 return x



file_path="D:/蔡骋苹果高光谱数据/红富士/"
bad_or_good=os.listdir("D:/蔡骋苹果高光谱数据/红富士/")
count=0
for i in range(2):	
 dir1=file_path+bad_or_good[i]+"/"
 temp=os.listdir(dir1)
 for j  in range(len(temp)-20):
	 temp1=dir1+temp[j]+"/"
	 temp2=os.listdir(temp1)
	 temp1=temp1+temp2[4]
	 count=count+1
	 getpartImg(temp1,count)
print(count)
 #X=getpartImg(str)


#cv2.imshow("HoughCircles",x)
#cv2.waitKey()
#cv2.destroyAllWindows()
#img=Image.fromarray((da*256)%256)
#img.show()
'''circles=cv2.HoughCircles(da*256,cv2.HOUGH_GRADIENT,1,320,param1=100,param2=30,minRadius=0,maxRadius=0)
circles=np.unit16(np.around(circles))
#画出圆
for i in circles[0,:]:
	cv2.circle(hhh,(i[0],i[1]),i[2],(0,255,0),2)
	cv2.circle(hhh,(i[0],i[1]),2,(0,0,255),3)'''

