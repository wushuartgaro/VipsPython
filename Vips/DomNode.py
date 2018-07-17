# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 15:11:00 2018

@author: Hard-
"""

class DomNode:
    __slots__ = ('nodeType','tagName', 'nodeName' , 'nodeValue', 'visual_cues', 'attributes', 'childNodes','parentNode')
    
    def __init__(self, nodeType):
        self.nodeType = nodeType
        self.attributes = dict()
        self.childNodes = []
        self.visual_cues = dict()
        
    def createElement(self, tagName):
        self.nodeName = tagName
        self.tagName = tagName
             
    def createTextNode(self, nodeValue, parentNode):
        self.nodeName = '#text'
        self.nodeValue = nodeValue
        self.parentNode = parentNode
        
    def createComment(self, nodeValue, parentNode):
        self.nodeName = "#comment"
        self.nodeValue = nodeValue
        self.parentNode = parentNode
    
    def setAttributes(self, attribute):
        self.attributes = attribute
    
    def setVisual_cues(self, visual_cues):
        self.visual_cues = visual_cues
    
    def appendChild(self, childNode):
        self.childNodes.append(childNode)
        
        