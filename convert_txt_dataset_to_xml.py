import os
from PIL import Image

folder=""

file = os.listdir(folder)

foldername = folder.split("/")[-1]
#dosyanın içinde fotolar ve txt aynı anda olmalı
for i in file:
    name = i.split(".")
    name = name[0]


    if(i.endswith(".txt")):

        img = Image.open(folder + "/" + name +".jpg")
        imgWidth, imgHeight = img.size

        with open(folder+'/'+i,"r") as f:
            print(name)

            ## Buraya da xml i kaydediceğimiz dosya yolunu koyuyuoruz
            xml_file = open(folder + '/' + name + '.xml', 'w')
            xml_file.write('<annotation>\n')
            xml_file.write('    <folder>' + foldername + '</folder>\n')
            xml_file.write('    <filename>' + name + '.jpg' + '</filename>\n')
            xml_file.write('    <path>'+folder+'/'+name+".jpg" +'</path>\n')
            xml_file.write('    <source>\n')
            xml_file.write('        <database>Unknown</database>\n')
            xml_file.write('    </source>\n')
            xml_file.write('    <size>\n')
            xml_file.write('        <width>' + str(int(imgWidth)) + '</width>\n')
            xml_file.write('        <height>' + str(int(imgHeight)) + '</height>\n')
            xml_file.write('        <depth>' + str(1) + '</depth>\n')
            xml_file.write('    </size>\n')
            xml_file.write('    <segmented>0</segmented>\n')
            xml_file.write('')

            lines = f.readlines()

            for line in lines:
                line = line.strip()
                data = line.split()
                c_x = float(data[1])*imgWidth
                c_y = float(data[2])*imgHeight
                box_width = float(data[3])*imgWidth
                box_height = float(data[4])*imgHeight
                #xmin ymin xmax ymax
                xmin = (c_x - (box_width/2))
                ymin = (c_y - (box_height/2))
                xmax = (c_x + (box_width/2))
                ymax = (c_y + (box_height/2))

                xml_file.write('    <object>\n')
                xml_file.write('        <name>' + 'text' + '</name>\n')
                xml_file.write('        <pose>Unspecified</pose>\n')
                xml_file.write('        <truncated>0</truncated>\n')
                xml_file.write('        <difficult>0</difficult>\n')
                xml_file.write('        <bndbox>\n')
                xml_file.write('            <xmin>' + str(int(xmin)) + '</xmin>\n')
                xml_file.write('            <ymin>' + str(int(ymin)) + '</ymin>\n')
                xml_file.write('            <xmax>' + str(int(xmax)) + '</xmax>\n')
                xml_file.write('            <ymax>' + str(int(ymax)) + '</ymax>\n')
                xml_file.write('        </bndbox>\n')
                xml_file.write('    </object>\n')

            xml_file.write('</annotation>\n')
            xml_file.close()
            print(name+" xml'e dönüştürüldü.\n")







