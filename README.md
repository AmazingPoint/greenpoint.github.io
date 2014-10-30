项目概述 （Description）
====================
我在做一个社交网站，这个网站将采用python来实现。
这是一个针对退伍老兵的网站，老兵可以在上边寻找曾经的战友，发表状态，私信聊天
网站最后就像一个由老兵组成的生态圈一样

I am writting a site with python.
The site first group is old soldier, Users can find old friends who is in force with u, tell others what are you doing, chat with others.
at the last we have a biosphere from old soldier.

文档结构（Structure）
=====================
文件结构说明：
design_doc是设计文档（目前只有中文）
design_psd是设计页面的PSD效果图
templates是最初的html静态页面
osdj是django的项目，之力才是真正的代码和你感兴趣的东西

the manual:
the folder dedign_doc include documents for old soldier project
the folder design_psd include preview psd file for web site page
the folder templates include static html and css file it can be run just static
the folder osdj is the base folder with django It can be run with django1.7

安装说明 (How to install)
========================
请先安装django1.7，这个django项目是基于django1.7的
当你下载到代码时，真正要被你运行的东西是osdj文件夹
你可以在osdj文件夹内找到manager.py 然后你就可以使用它 
我在开发中使用sqlite数据库，数据库路径是osdj文件夹内的database下的db.os
也就是说，你可以这么做：
   git clone https://github.com/AmazingPoint/greenpoint.github.io.git ospro
   cd ospro/osdj
   python manager.py runserver
然后在浏览器输入 http://127.0.0.1:8000/osb

If you want to run site on your computer, just download django1.7
When you get the code, the true path is the folder wich is named 'osdj'
You can get manager.py file in osdj folder, and then you can run it
I use sqlite database for develop, you also can see it in osdj/databses/db.os
   so, you can do like this:
   git clone https://github.com/AmazingPoint/greenpoint.github.io.git ospro
   cd ospro/osdj
   python manager.py runserver
then type the address http://127.0.0.1:8000/osb in your browser
