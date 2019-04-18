from xml.dom import minidom
import os
import uuid
import time


class XML(object):

    def __init__(self):
        self.crul_path = os.path.dirname(os.path.dirname(__file__))
        self.xml_path = self.crul_path + "/xml_dir/base.xml"

    def createUUID(self):
        uuidContent = uuid.uuid5(uuid.uuid1(), str(time.time()))
        newuuid = str(uuidContent).split('-')
        delimiter = ''
        code = delimiter.join(newuuid)
        return code.upper()

    # 创建INDEX.xml
    def create_xml(self):
        dom = minidom.parse(self.xml_path)
        root = dom.documentElement                                                       # 元素对象
        name = root.getElementsByTagName('DATASET')[1]                                   # 获取第二个标签为dataset
        add_xml_data = self.update_xml()                                                 # 调用update_xml方法
        for j in range(len(add_xml_data)):
            name.appendChild(add_xml_data[j])                                            # 插入修改后的xml，添加元素子节点
        str_xml = root.toxml()                                                           # 输入紧凑格式的xml文本，及编码
        with open(os.path.join(self.crul_path + "/xml_dir/", "INDEX.xml"), 'w+', encoding='utf-8') as f:   # 在生成bcp文件夹下创建及打开xml
            f.write(str_xml)                                                             # 写入xml信息保存

    # 读取及修改xml中对应的bcp名称
    def update_xml(self):
        xml_data = []
        xml_name = "template.xml"                                                          # xml名称
        xml_file = self.crul_path + "/xml_dir/"                                            # xml文件夹路径
        dom = minidom.parse(os.path.join(xml_file, xml_name))                              # 打开xml
        root1 = dom.documentElement
        data = root1.getElementsByTagName('DATA')[0]
        node_name = root1.getElementsByTagName("DATA")[1].getElementsByTagName("ITEM")[0]
        if node_name.attributes['key'].value == 'PK_ID':                                    # 判断属性为key的值为xxx
            node_name.attributes['val'] = self.createUUID()
        xml_data.append(data)
        return xml_data                                                                     # 返回 修改后的xml信息


if __name__ == "__main__":
    xml_test = XML()
    xml_test.create_xml()
