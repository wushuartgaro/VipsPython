# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:40:03 2018

@author: Hard-
"""

class BlockRule:
    threshold = 40000
       
    @staticmethod
    def initialize(passed_nodeList):
        global nodeList 
        nodeList =  passed_nodeList
    
    @staticmethod
    def dividable(block):                 
        box = block.boxs[0]
        #print(box.tag_name)
        if box.nodeType == 3:
            return False
        name = box.nodeName
    
        if(name == "img"):
            return False
        if not BlockRule.isBlock(name):
            return BlockRule.inlineRules(block)
        elif (name == 'table'):
            return BlockRule.tableRules(block)
        elif (name == 'tr'):
            return BlockRule.trRules(block)
        elif (name == 'td'):
            return BlockRule.tdRules(block)
        elif (name == 'p'):
            return BlockRule.pRules(block)
        else:
            return BlockRule.otherRules(block)
    
    @staticmethod
    def otherRules(block):
        if BlockRule.rule1(block):
            return True
        if BlockRule.rule2(block):
            return True
        if BlockRule.rule3(block):
            return True
        if BlockRule.rule4(block):
            return True
        if BlockRule.rule6(block):
            return True
        if BlockRule.rule7(block):
            return True
        if BlockRule.rule9(block):
            return True
        if BlockRule.rule10(block):
            return True
        if BlockRule.rule12(block):
            return True    
        return False
    
    @staticmethod
    def pRules(block):
        if BlockRule.rule1(block):
            return True
        if BlockRule.rule2(block):
            return True
        if BlockRule.rule3(block):
            return True
        if BlockRule.rule4(block):
            return True
        if BlockRule.rule5(block):
            return True
        if BlockRule.rule6(block):
            return True
        if BlockRule.rule7(block):
            return True
        if BlockRule.rule9(block):
            return True
        if BlockRule.rule10(block):
            return True    
        if BlockRule.rule12(block):
            return True   
        return False
    
    @staticmethod
    def tdRules(block):
        if BlockRule.rule1(block):
            return True
        if BlockRule.rule2(block):
            return True
        if BlockRule.rule3(block):
            return True
        if BlockRule.rule4(block):
            return True
        if BlockRule.rule9(block):
            return True
        if BlockRule.rule10(block):
            return True
        if BlockRule.rule11(block):
            return True
        if BlockRule.rule13(block):
            return True
        return False
    
    @staticmethod
    def trRules(block):
        if BlockRule.rule1(block):
            return True
        if BlockRule.rule2(block):
            return True
        if BlockRule.rule3(block):
            return True
        if BlockRule.rule7(block):
            return True
        if BlockRule.rule8(block):
            return True
        if BlockRule.rule10(block):
            return True
        if BlockRule.rule13(block):
            return True
        return False
    
    @staticmethod
    def tableRules(block):
        if BlockRule.rule1(block):
            return True
        if BlockRule.rule2(block):
            return True
        if BlockRule.rule3(block):
            return True
        if BlockRule.rule8(block):
            return True
        if BlockRule.rule10(block):
            return True
        if BlockRule.rule13(block):
            return True
        return False
    
    @staticmethod    
    def inlineRules(block):
        if BlockRule.rule1(block):
            return True
        if BlockRule.rule2(block):
            return True
        if BlockRule.rule3(block):
            return True
        if BlockRule.rule4(block):
            return True
        if BlockRule.rule5(block):
            return True
        if BlockRule.rule6(block):
            return True
        if BlockRule.rule7(block):
            return True
        if BlockRule.rule9(block):
            return True
        if BlockRule.rule10(block):
            return True
        if BlockRule.rule12(block):
            return True
        return False
    
    
    """ 
    Rule 1: If the DOM node is not a text node and it has no valid children, 
    then this node cannot be divided and will be cut.
    """
    @staticmethod
    def rule1(block):
        node = block.boxs[0]
        if not BlockRule.isTextNode(node) and not BlockRule.hasValidChildNode(node):
            print('Rule 1 violated')
            #question
            #block.parent.children.remove(block)
        return False
    
    """ 
    Rule 2:If the DOM node has only one valid child and the child is not a text node, 
    then divide this node..
    """
    @staticmethod
    def rule2(block):
        if(len(block.children) == 1):
            node = block.children[0].boxs[0]
            if(BlockRule.isValidNode(node) and not BlockRule.isTextNode(node)):
                return True        
        return False
    
    """ 
    Rule 3: If the DOM node is the root node of the sub-DOM tree (corresponding to the block), 
    and there is only one sub DOM tree corresponding to this block, divide this node.
    """
    @staticmethod
    def rule3(block):
        node = block.boxs[0]
        #question
        result = True
        cnt = 0
        
        for vipsBlock in block.children:
            if vipsBlock.boxs[0].nodeName == node.nodeName:
                result = True
                BlockRule.isOnlyOneDomSubTree(node, vipsBlock.boxs[0],result)
                
                if result:
                    cnt+=1
        
        return True if cnt == 1 else False
        
    """
    Rule 4: If all of the child nodes of the DOM node are text nodes or virtual text nodes,
    do not divide the node.
    If the font size and font weight of all these child nodes are same, 
    set the DoC of the extracted block to 10.
    Otherwise, set the DoC of this extracted block to 9.
    """
    @staticmethod
    def rule4(block):
        node = block.boxs[0]
        subBoxList = node.childNodes
        count = 0
        for box in subBoxList:
            if(BlockRule.isTextNode(box) or BlockRule.isVirtualTextNode(box)):
                count+=1
        if(count == len(subBoxList)):
            fontSize = 0
            for box in subBoxList:
                childSize = box.visual_cues['font-size']
                if fontSize != 0:
                    if fontSize != childSize:
                        block.Doc = 9
                        return False
                    else:
                        fontSize = childSize               
               
            fontWeight = None
            for box in subBoxList:
                childWeight = box.visual_cues['font-weight']
                if fontWeight != None:
                    if fontWeight != childWeight:
                        block.Doc = 9
                        return False
                    else:
                        fontWeight = childWeight      
               
            block.Doc = 10
            return False      
        return True
            
    """
    Rule 5:  If one of the child nodes of the DOM node is line-break node, then divide this DOM node
    """
    @staticmethod
    def rule5(block):
        node = block.boxs[0]
        subBoxList = node.childNodes
        for box in subBoxList:
            #question
            if not BlockRule.isBlock(box.nodeName):
                return True

        return False
    
    """
    Rule 6: If one of the child nodes of the DOM node has HTML tag <HR>, 
    then divide this DOM node
    """
    @staticmethod
    def rule6(block):
        node = block.boxs[0]
        subBoxList = node.childNodes
        
        for box in subBoxList:
            if box.nodeName == 'hr':
                return True

        return False
    
    """
    Rule 7: If the sum of all the child nodes' size is greater than this DOM node's size, 
    then divide this node.
    """
    @staticmethod
    def rule7(block):
        node = block.boxs[0]
        x = node.visual_cues['bounds']['x']
        y = node.visual_cues['bounds']['y'] 
        width = node.visual_cues['bounds']['width']
        height = node.visual_cues['bounds']['height']
        
        subBoxList = node.childNodes
        #question
        for box in subBoxList:
            if(box.visual_cues['bounds']['x']< x):
                return True
            if(box.visual_cues['bounds']['y']  < y):
                return True
            if((x+width) < (box.visual_cues['bounds']['x']  + box.visual_cues['bounds']['width'] )):
                return True
            if((y+height) < (box.visual_cues['bounds']['y'] + box.visual_cues['bounds']['height'])):
                return True
        return False
        
    """
    Rule 8: If the background color of this node is different from one of its children's, 
    divide this node and at the same time, 
    the child node with different background color will not be divided in this round.
    Set the DoC value (6-8) for the child node based on the html tag of the child node and the size of the child node.
    """
    @staticmethod
    def rule8(block):
        ret = False
        node = block.boxs[0]
        bColor = node.visual_cues['background-color']
        for b in block.children:
            child = b.boxs[0]
            childColor = child.visual_cues['background-color']
            if bColor != childColor:
                b.isDividable = False
                b.Doc = BlockRule.getDocByTagSize("",0)
                ret = True
        return ret

    """
    Rule 9: If the node has at least one text node child or at least one virtual text node child, 
    and the node's relative size is smaller than a threshold, then the node cannot be divided
    Set the DoC value (from 5-8) based on the html tag of the node
    """
    @staticmethod
    def rule9(block):
        ret = True
        node = block.boxs[0]

        subBoxList = node.childNodes
        count = 0
        for box in subBoxList:
            if(BlockRule.isTextNode(box) or BlockRule.isVirtualTextNode(box)):
                count+=1
        if count > 0:
            if (node.visual_cues['bounds']['x'] * node.visual_cues['bounds']['y'] < BlockRule.threshold):
                ret = False
                block.Doc = BlockRule.getDocByTagSize("",0)
        
        return ret
    
    """
    Rule 10: If the child of the node with maximum size are smaller than a threshold (relative size), 
    do not divide this node.
    Set the DoC based on the html tag and size of this node.
    """
    @staticmethod
    def rule10(block):
        node = block.boxs[0]
        subBoxList = node.childNodes
        maxSize = 0
        for box in subBoxList:
            childSize = box.visual_cues['bounds']['x'] * box.visual_cues['bounds']['y'] 
            maxSize = childSize if maxSize < childSize else maxSize
        if maxSize < BlockRule.threshold:
            block.Doc = BlockRule.getDocByTagSize("",0)
            return False
        return True
    
    """
    Rule 11: If previous sibling node has not been divided, do not divide this node
    """
    @staticmethod
    def rule11(block):
        children = block.parent.children
        index  = children.index(block)
        count = 0
        for i in range(0,index):
            if not children[i].isDividable:
                count+=1
        return not count == index

    
    """
    Rule 12: Divide this node.
    """
    @staticmethod
    def rule12(block):
        return True
    
    """
    Rule 13: Do not divide this node 
    Set the DoC value based on the html tag and size of this node.
    """
    @staticmethod
    def rule13(block):
        block.Doc = BlockRule.getDocByTagSize("",0)
        return False
    
    @staticmethod
    def hasValidChildNode(node):
        subBoxList = node.childNodes
        for box in subBoxList:
            if(BlockRule.isValidNode(box)):
                return True
        return False
    
    """
    a node that can be seen through the browser. 
	 The node's width and height are not equal to zero.
    """    
    @staticmethod
    def isValidNode(node): 
        display = node.visual_cues['display']
        visibility = node.visual_cues['visibility']
        
        if display == 'none' or visibility == 'hidden':
            return False
        height = node.visual_cues['bounds']['height']
        width = node.visual_cues['bounds']['width']
        if height == '0px' or width == '0px':
            return False
        return True
    
    """
    the DOM node corresponding to free text, which does not have an html tag
    """   
    @staticmethod
    def isTextNode(node):
        return node.nodeType == 3

    
    """
    Virtual text node (recursive definition):
	 Inline node with only text node children is a virtual text node.
	 Inline node with only text node and virtual text node children is a virtual text node.
    """
    @staticmethod
    def isVirtualTextNode(node):
        subBoxList = node.childNodes
        count = 0
        for box in subBoxList:
            if(BlockRule.isTextNode(box) or BlockRule.isVirtualTextNode(box)):
                count+=1
        if(count == len(subBoxList)):
            return True
        return False
    
    
    @staticmethod
    def isBlock(name):
        if (name == 'a' or
            name == 'abbr' or
            name == 'acronym' or
            name == 'b' or
            name == 'bdo' or
            name == 'big' or
            name == 'br' or
            name == 'button' or
            name == 'cite' or
            name == 'code' or
            name == 'dfn' or
            name == 'em' or
            name == 'i' or
            name == 'img' or
            name == 'input' or
            name == 'kbd' or
            name == 'label' or
            name == 'map' or
            name == 'object' or
            name == 'q' or
            name == 'samp' or
            name == 'script' or
            name == 'select' or
            name == 'small' or
            name == 'span' or
            name == 'strong' or
            name == 'sub' or
            name == 'sup' or
            name == 'textarea' or
            name == 'time' or
            name == 'tt' or
            name == 'var'):
            return False
        else:
            return True  
        
    @staticmethod
    def isOnlyOneDomSubTree(pattern, node, result):
        if pattern.nodeName != node.nodeName:
            result = False
        pattern_child = pattern.childNodes
        node_child = node.childNodes
        if len(pattern_child) != len(node_child):
            result = False
        if not result:
            return 
        for i in range(0,len(pattern_child)):
            BlockRule.isOnlyOneDomSubTree(pattern_child[i],node_child[i],result)
                   
    @staticmethod
    def getDocByTagSize(tag, size):
        return 7
        