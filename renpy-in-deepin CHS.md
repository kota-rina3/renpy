### deepin编译、运行renpy
---
老规矩，先安装下列依赖：
`sudo apt install virtualenv python3-dev libassimp-dev libavcodec-dev libavformat-dev libswresample-dev libswscale-dev libharfbuzz-dev libfreetype6-dev libfribidi-dev libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libjpeg-dev pkg-config zenity python3-tk`
> 安装了星火应用商店的用户可用**aptss**加速下载

创建python虚拟环境：
`virtualenv renpy-deepin`

赋权启动脚本：
`sudo chmod u+x renpy-deepin/bin/activate`

激活（进入）虚拟环境：
`source renpy-deepin/bin/activate`

在虚拟环境内，安装模块：
`pip install -U setuptools cython future six typing pefile requests ecdsa assimp legacy-cgi`
> *可以**追加镜像源**加速下载：`-i https://mirrors.aliyun.com/pypi/simple/`*

把renpy和pygame_sdl2给git下来：
`git clone https://github.com/kota-rina3/renpy.git`

`cd renpy && git clone https://github.com/kota-rina3/pygame_sdl2.git`

进入pygame_sdl2，并执行下列编译命令：
`cd pygame_sdl2 && python setup.py install`

退回到renpy，重复执行编译命令：
`popd && python setup.py install`

执行renpy.py，若能调用，说明编译安装成功：
`python renpy.py`

### 游戏 in renpy壳
---
回到桌面，我们创建文件夹，用于放置renpy有关文件：
`cd ~/Desktop && mkdir renpy-box`

回到renpy文件夹，复制.git renpy renpy.py这三样：
pushd renpy && cp -R .git renpy renpy.py ~/Desktop/renpy-box
> .git用于检验renpy的，renpy文件夹包含了运行游戏所需脚本，renpy.py负责启动游戏

就这样，一个renpy壳就此诞生。
将game文件夹扔进renpy壳里，执行renpy.py。这样游戏就能跑起来了。
> .git renpy renpy.py是常量，game是变量。
想玩其他renpy游戏，只需删除原来的game文件夹，把新的game文件夹扔进去，再执行renpy.py即可。

####注：请在虚拟环境下执行游戏！
