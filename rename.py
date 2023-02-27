import pytesseract
from PIL import Image
import os
####
#### 文件下不要有其他非图片文件


#print(pytesseract.get_languages(config=''))
#  找到文件位置（绝对路径）
images="D:/大学/青年大学习/大三/12.23"







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

print("改名任务完成")
#####打包

import zipfile

def make_zip(source_dir, desc_dir):
    zfile = zipfile.ZipFile(file=images+"/"+desc_dir,mode="w")
    try:
        for root, dirnames, filenames in os.walk(source_dir):
            file_path = root.replace(source_dir, '')  # 去掉根路径，只对目标文件夹下的文件及文件夹进行压缩
            # 循环出一个个文件名
            for filename in filenames:
                zfile.write(os.path.join(root, filename), os.path.join(file_path, filename))
        return True
    except Exception as e:
        print(e)
    zip.close()

make_zip(images,"217.zip")###打包路径与重命名路径相同 第二个选项为新文件名称
print("打包任务完成")