#coding=utf-8
'''
@author: DMao
@time: 14.09.18    11:41
'''
from bs4 import BeautifulSoup

html = """ 
    <html>
        <head>
            <title> here is a Website title </title>
            <style type="text/css">
                .some {
                    color: red;
                }
                #test123 {
                    color: orange;
                }
                span{
                    color: green;
                }
                
                .paragraph1 p {
                    font-weight: bold;
                }
                
                .paragraph3 .thing {
                    font-weight: bold;
                }
            </style> 
        </head>
        <body>
            <div class="paragraph1"> 
                <p> a paragraph in div tag </p>
            </div>
            
            <div class="paragraph2">
                <p> another paragraph in div tag </p>
            </div>
            
            <div class="paragraph3">
                <p> another paragraph in div tag </p>
                <p class="thing"> the first paragraph </p>
            </div>
        
        
            <p class="some"> the first paragraph </p>
            <p class="some"> the second paragraph </p>
            <p id="test123"> the third paragraph </p>
            <p> another paragraph </p>
            <p> a paragraph </p>
            <span> paragraph with span tag </p>
        </body>
    </html>
    """

doc = BeautifulSoup(html, "html.parser")

print(doc)

for i in doc.find_all("p"):
    #print(i.text)
    print(i.attrs)
