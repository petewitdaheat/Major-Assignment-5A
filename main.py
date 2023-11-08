from node import *

def main():
    # 1
    head = node('2', None)
    head = node('=', head)
    head = node('1', head)
    head = node('+', head)
    head = node('1', head)

    #2 
    operator = head

    # 3
    operator = operator.getLink()

    #4 
    result = head

    # 5
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()

    # 6
    operator.setData('-')

    # 7
    operator.setData('*')

    # 8
    operator.setData('/')\
    
    # 9
    head.setData('7')
    result.setData('7')

    # 10
    operator = operator.getLink()

    # 11
    head.removeNodeAfter()
    operator.removeNodeAfter()

    # 12
    print("Head contains", node.listLength(head), "Nodes")
    print("Operator contains", node.listLength(operator), "Nodes")
    print("Result contains", node.listLength(result), "Node")
    
    # 13
    if (node.listSearch(head, '1') != None):
        print("Head contains character", node.listSearch(head, '1').getData())
    else:
        print("Head doesn't contain character 1")

    if (node.listSearch(operator, '1') != None):
        print("Operator contains character", node.listSearch(operator, '1').getData())
    else:
        print("Operator doesn't contain character 1")

    if (node.listSearch(result, '1') != None):
        print("Result contains character", node.listSearch(result, '1').getData())
    else:
        print("Result doesn't contain character 1")

    # 14
    copy = node.listCopy(head)
    other_copy = node.listCopy(result)

    # 15
    print("Copy[0] contains", node.listLength(copy), "Nodes")
    print("Copy[1] contains", node.listLength(other_copy), "Node")

    # 16
    if (node.listSearch(copy, '1') != None):
        print("Head contains character", node.listSearch(copy, '1').getData())
    else:
        print("Head doesn't contain character 1")
    
    if (node.listSearch(other_copy, '1') != None):
        print("Head contains character", node.listSearch(other_copy, '1').getData())
    else:
        print("Head doesn't contain character 1")




if __name__ == "__main__":
    main()