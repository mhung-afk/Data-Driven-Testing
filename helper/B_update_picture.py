from helper.base import DDT_edge
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import os


class Update_Piicture_DDT_edge(DDT_edge):

    def drop_files(self, element, files, offsetX=0, offsetY=0):
        JS_DROP_FILES = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"
        driver = element.parent
        isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
        paths = []

        # ensure files are present, and upload to the remote server if session is remote
        for file in (files if isinstance(files, list) else [files]):
            if not os.path.isfile(file):
                raise FileNotFoundError(file)
            paths.append(file if isLocal else element._upload(file))

        value = '\n'.join(paths)
        elm_input = driver.execute_script(
            JS_DROP_FILES, element, offsetX, offsetY)
        elm_input._execute('sendKeysToElement', {
                           'value': [value], 'text': value})

    def check_loading(self):
        try:
            self.find_ele(
                By.XPATH, '//input[@disabled and @id="id_submitbutton"]')
            return True
        except:
            return False

    def check_file(self):
        try:
            self.find_ele(By.ID, 'fp-msg-labelledby')
            return False
        except:
            return True

    def updtate_picture(self, record):
        # print(record)
        try:
            tick = self.find_ele(By.ID, 'id_deletepicture')
            self.click(tick)
        except:
            a = 1
        temp = self.find_ele(
            By.CSS_SELECTOR, '.filemanager-container')
        self.wait(1)
        self.drop_files(temp, os.getcwd()+'/test-data/'+str(record[1]))

        if not self.check_file():
            clo = self.find_ele(
                By.XPATH, '//button[@class="fp-msg-butok btn-primary btn"]')
            self.click(clo)

        temp = self.find_ele(By.ID, 'id_imagealt')
        self.text(temp, str(record[2]))

        while True:
            check = self.check_loading()
            if check == False:
                break
            self.wait(1)

        temp = self.find_ele(By.ID, f'id_submitbutton')

        self.click(temp)
