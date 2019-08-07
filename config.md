# 常用配置

## pip设置

### pip国内的一些镜像源

  阿里云 https://mirrors.aliyun.com/pypi/simple/
  中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
  豆瓣(douban) http://pypi.douban.com/simple/
  清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
  中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

修改源方法：

临时使用：
可以在使用pip的时候在后面加上-i参数，指定pip源
eg: pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple

永久修改：
linux:
修改 ~/.pip/pip.conf (没有就创建一个)， 内容如下：

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

windows:
直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下

[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple



### pip 设置代理

基本命令
有三种常用方式： 
①永久设置：

vim /etc/profile：
    export http_proxy='http://代理服务器IP:端口号'
    export https_proxy='http://代理服务器IP:端口号'
source /etc/profile
②临时设置（重连后失效）： 
也可以直接运行export http_proxy='http://代理服务器IP:端口号 
export https_proxy='http://代理服务器IP:端口号'

注意：设置之后可能使用ping时还是无法连接外网，但是pip时可以的，因为ping的协议不一样不能使用这个代理

③单次设置： 
直接在pip时设置代理也是可以的： 
pip install -r requirements.txt --proxy=代理服务器IP:端口号
