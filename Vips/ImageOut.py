# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 20:45:02 2018

@author: Hard-
"""
import time

from PIL import Image, ImageDraw, ImageFont

class ImageOut:
       
    def outImg(self, browser, url, screenshot_path="screenshot.png"):
        print('-----------------------------Getting Screenshot------------------------------------')
        default_width=1920
        default_height=1080
        # 1. get dimensions
        print('getting dimensions...')
        browser.set_window_size(default_width, default_height)
        browser.get(url)
        print('loading...')  
        total_height = browser.execute_script("return document.body.parentNode.scrollHeight")
        #self.browser.quit()
    
        # 2. get screenshot
        print('getting screenshot...')
        browser.set_window_size(default_width, total_height)
        browser.get(url)
        #time.sleep(3) 
        browser.save_screenshot(screenshot_path+'.png')
        print('done')
    
    def outBlock(self, block, fileName, i=0):
        print(i)
        img = Image.open(fileName+'.png')
        dr = ImageDraw.Draw(img)
        for blockVo in block:
            if blockVo.isVisualBlock:               
                ################ Rectangle ###################
                cor = (blockVo.x,blockVo.y, blockVo.x + blockVo.width, blockVo.y + blockVo.height)
                line = (cor[0],cor[1],cor[0],cor[3])
                dr.line(line, fill="red", width=1)
                line = (cor[0],cor[1],cor[2],cor[1])
                dr.line(line, fill="red", width=1)
                line = (cor[0],cor[3],cor[2],cor[3])
                dr.line(line, fill="red", width=1)
                line = (cor[2],cor[1],cor[2],cor[3])
                dr.line(line, fill="red", width=1)
                ###############                ####################
                font = ImageFont.truetype("arial.ttf", 15)
                dr.text((blockVo.x,blockVo.y),blockVo.id,(255,0,0),font=font)
                #if blockVo.boxs[0].tag != None and blockVo.boxs[0].text != None and not blockVo.boxs[0].text.isspace():
                
        saved_path = fileName + '_Block_' + str(i) + '.png'
        img.save(saved_path)
    
    def outSeparator(self, List, fileName, direction, i=0):
        print(i)
        if (direction == '_vertica_'):
            img = Image.open(fileName + '_Block_' + str(i) + '.png')
        elif (direction == '_horizontal_'):
            img = Image.open(fileName + '_vertica_' + str(i) + '.png')
        dr = ImageDraw.Draw(img)
        for sep in List:             
            ################ Rectangle ###################
            dr.rectangle(((sep.x,sep.y),(sep.x + sep.width, sep.y + sep.height)),fill = "blue")
            """
            cor = (sep.x,sep.y, sep.x + sep.width, sep.y + sep.height)
            line = (cor[0],cor[1],cor[0],cor[3])
            dr.line(line, fill="blue", width=1)
            line = (cor[0],cor[1],cor[2],cor[1])
            dr.line(line, fill="blue", width=1)
            line = (cor[0],cor[3],cor[2],cor[3])
            dr.line(line, fill="blue", width=1)
            line = (cor[2],cor[1],cor[2],cor[3])
            dr.line(line, fill="blue", width=1)
            """
            ###############                ####################
        saved_path = fileName + direction + str(i) + '.png'
        img.save(saved_path)
    
    @staticmethod
    def outText(fileName, blockList, i=0):     
        f = open(fileName+'_text_output_'+str(i)+'.txt','a', encoding= 'utf-8')        
        for blockVo in blockList:
            write_line = str('\n=============================================================\nBlock-'+str(blockVo.id) +'\n')
            text_content = ""
            for box in blockVo.boxs:
                writable = False              
                if box.nodeType == 3:
                    if box.parentNode.nodeName != "script" and box.parentNode.nodeName != "noscript" and box.parentNode.nodeName != "style":
                        if not box.nodeValue.isspace() or box.nodeValue == None:
                            text_content += str(box.nodeValue+'\n')
                            writable = True
            write_line += text_content + str('\n=============================================================\n')                     
            if(writable):
                try:
                    f.write(write_line)
                except UnicodeEncodeError:
                    f.write(str(write_line.encode("utf-8").decode('utf-8')))
                    print(blockVo.id)
        f.close()
