import os
import zipfile
 
def make_zip(source_dir, desc_dir):
    zfile = zipfile.ZipFile(desc_dir, "w")
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
make_zip("D:/大学/青年大学习/大三/12.23","217.zip")