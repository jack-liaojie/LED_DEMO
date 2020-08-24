# -*- coding: utf-8 -*-
"""
Module: xml的读取、更新和写入
Date: 2020-5-12

"""
# 1
from xml.etree.ElementTree import ElementTree, Element

def get_root(in_path):
    """    1.
    读取并解析xml文件
    in_path: xml路径
    return: ElementTree
    例如："./Localization/en.xml
    tree = ET.parse("../student.xml")
    root = tree.getroot()
    print(root.tag)
    print(root.text)
    print(root.attrib)
    """
    tree = ElementTree()
    tree.parse(in_path)
    root = tree.getroot()
    return root

def find_element(root, path):
    """    2.
    查找某个路径匹配的所有节点
    root: xml树
    path: 节点路径
    例如：find_element(root, "OVRLogin/Server")
    for element in root.findall('student/age'):
        tag = element.tag
        text = element.text
        attrib = element.attrib
    """
    return root.findall(path)

def get_node_by_keyvalue(nodelist, kv_map):
    """    3.
    根据属性及属性值定位符合的节点，返回节点（该项目xml文件中没有属性，所有没有此项功能。）
    nodelist: 节点列表
    kv_map: 匹配属性及属性值map
    例如：get_node_by_keyvalue(nodes, {"name": "BProcesser"})
    """
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes

def if_match(node, kv_map):
    """     3.1
    判断某个节点是否包含所有传入参数属性
    node: 节点
    kv_map: 属性及属性值组成的map
    """
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True

def get_node_text(nodelist):
    """    4.
    根据属性及属性值定位符合的节点,返回给节点内容
    nodelist: 节点列表
    kv_map: 匹配属性及属性值map
    例如：get_node_text(nodes)
    """
    x = []
    for node in nodelist:
        x.append(node.text)
    return x

def write_xml(tree, out_path):
    """将xml文件写出
       tree: xml树
       out_path: 写出路径"""
    tree.write(out_path, encoding="utf-8", xml_declaration=True)

def change_node_properties(nodelist, kv_map, is_delete=False):
    """修改/增加 /删除 节点的属性及属性值
       nodelist: 节点列表
       kv_map:属性及属性值map"""
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
            else:
                node.set(key, kv_map.get(key))

def change_node_text(nodelist, text, is_add=False, is_delete=False):
    """改变/增加/删除一个节点的文本
       nodelist:节点列表
       text : 更新后的文本"""
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text
    return node.text

def create_node(tag, property_map, content):
    """新造一个节点
       tag:节点标签
       property_map:属性及属性值map
       content: 节点闭合标签里的文本内容
       return 新节点"""
    element = Element(tag, property_map)
    element.text = content
    return element

def add_child_node(nodelist, element):
    """给一个节点添加子节点
       nodelist: 节点列表
       element: 子节点"""
    for node in nodelist:
        node.append(element)

def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    """同过属性及属性值定位一个节点，并删除之
       nodelist: 父节点列表
       tag:子节点标签
       kv_map: 属性及属性值列表"""
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and if_match(child, kv_map):
                parent_node.remove(child)

def get_xml_text(strpath,strSection, strItem):
    tree = get_root(strpath)
    nodes = get_node_by_keyvalue(strSection,strItem)
    # nodes = find_element(tree, strSection + "/" + strItem)
    return get_node_text(nodes)

def update_xml_text(strpath,strSection, strItem, strVolue):
    tree = get_root(strpath)
    nodes = find_element(tree, strSection + "/" + strItem)
    change_node_text(nodes,strVolue)
    write_xml(tree, strpath)
    return True

def new_xml_file():
    pass


if __name__ == "__main__":
    # 1、读出xml
    tree = get_root("student.xml")
    # 2、找节点
    node = find_element(tree,'students')

    value = get_node_by_keyvalue(node,'name')
    
    print(value)

    # print(get_node_by_keyvalue(node,{'page':'name'}))
    # print(get_xml_text("student.xml",'student','name'))
    # print(get_root('./Localization/en.xml'))
    # print(update_xml_text('OVRLogin', 'Server', '234234234'))
    # writeXMLFile()

    # # 1. 读取xml文件
    # tree = get_root("test_02.xml")
    #
    # # 2. 属性修改
    # nodes = find_element(tree, "processers/processer")  # 找到父节点
    # result_nodes = get_node_by_keyvalue(nodes, {"name": "BProcesser"})  # 通过属性准确定位子节点
    # x = get_node_text(nodes)
    # print(x)
    # change_node_properties(result_nodes, {"age": "1"})  # 修改节点属性
    # change_node_properties(result_nodes, {"value": ""}, True)  # 删除节点属性
    #
    # #  3. 节点修改 #
    # a = create_node("person", {"age": "15", "money": "200000"}, "this is the firest content")  # 新建节点
    # add_child_node(result_nodes, a)  # 插入到父节点之下
    #
    # # 4. 删除节点 #
    # del_parent_nodes = find_element(tree, "processers/services/service")  # 定位父节点
    # target_del_node = del_node_by_tagkeyvalue(del_parent_nodes, "chain", {"sequency": "chain1"})  # 准确定位子节点并删除之
    #
    # # 5. 修改节点文本 #
    # text_nodes = get_node_by_keyvalue(find_element(tree, "processers/services/service/chain"),
    #                                   {"sequency": "chain3"})  # 定位节点
    # change_node_text(text_nodes, "new text")
    #
    # # 6. 输出到结果文件
    # write_xml(tree, "./xiugai.xml")
