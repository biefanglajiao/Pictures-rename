import pytesseract
from PIL import Image
import os
####
#### 文件下不要有其他非图片文件


#print(pytesseract.get_languages(config=''))
#  找到文件位置（绝对路径）
images="D:/大学/青年大学习/大三/11.18"
#  定义成员库
names=['常兆海','吕泽阳','杨融亦','孙剑锋','刘宇达','刘浩']
#遍历文件夹下文件
for image in os.listdir(images):
        imageinfo = Image.open(images+"/"+image)#找到对应文件
        word = pytesseract.image_to_string(imageinfo, lang='chi_sim')#识别
        #去掉空格
        words =word.split()
        word  = "".join(words)
        #匹配重命名对应成员库
        for name in names:
                if(name in word):
                        print("识别到文件所属为："+name)
                        #重命名
                        os.rename(images+"/"+image,images+"/软件2028班-"+name+".jpg")
                        print("图片成功改名为:软件2028班-"+name)
        #print(word)

print("任务完成")
