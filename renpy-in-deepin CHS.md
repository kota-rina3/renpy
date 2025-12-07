### deepin编译、运行renpy
---
老规矩，先安装下列依赖：
`sudo apt update && sudo apt install python3-pip python3-dev libassimp-dev libavcodec-dev libavformat-dev libswresample-dev libswscale-dev libharfbuzz-dev libfreetype6-dev libfribidi-dev libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libjpeg-dev pkg-config zenity python3-tk`
> 安装了星火应用商店的用户可用**aptss**加速下载

安装uv模块：
`pip3 install uv -i https://mirrors.aliyun.com/pypi/simple/ --break-system-packages`

把renpy给git下来：
`git clone https://github.com/kota-rina3/renpy.git`
> *速度慢或失败了，尝试用**gitee**的镜像：`git clone https://gitee.com/ricervm-cn/renpy.git`*

进入renpy，执行uv同步，并执行编译脚本：
`pushd renpy && /home/你的用户名/.local/bin/uv sync && ./run.sh`
> “你的用户名”改为你安装系统时设的用户名

编译完后，会自行启动renpy。

若想再次启用renpy，请输入：
`python renpy.py`

### 游戏 in renpy壳
---
回到桌面，我们创建文件夹，用于放置renpy有关文件：
`cd ~/Desktop && mkdir renpy-box`

回到renpy文件夹，复制renpy renpy.py及动态库：
`pushd renpy && cp -R renpy renpy.py *.so ~/Desktop/renpy-box`

从pip里安装所需模块：`pip3 install setuptools cython future six typing pefile requests ecdsa assimp legacy-cgi --break-system-packages`
> 速度慢？可挂镜像源加速下载：-i https://mirrors.aliyun.com/pypi/simple/

就这样，一个renpy壳就此诞生。
将game文件夹扔进renpy壳里，执行renpy.py。这样游戏就能跑起来了。
> renpy文件夹、renpy.py是常量，game是变量。
想玩其他renpy游戏，只需删除原来的game文件夹，把新的game文件夹扔进去，再执行renpy.py即可。

