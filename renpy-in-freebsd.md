# FreeBSD编译运行Renpy

####-> 编译

先更新软件源：`pkg update`

接下来安装python3.12：`pkg install python312`

由于FreeBSD没有打包python3.12用的pip，只好曲线救国：`python3.12 -m ensurepip`

从系统源里安装编译所需依赖：`pkg install assimp sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_sound sdl2_ttf pkgconf freetype2 harfbuzz fribidi`

从pip里安装renpy所需模块：`~/.local/bin/pip3.12 install setuptools cython future six typing pefile requests ecdsa assimp legacy-cgi`
> 速度慢？可挂镜像源加速下载：-i https://mirrors.aliyun.com/pypi/simple/

使用git拉取源码：`git clone https://github.com/kota-rina3/renpy.git`
> 国内用户执行：`git clone https://gitee.com/ricervm-cn/renpy.git`

拉取后，进入renpy文件夹，解压renpy-FREEBSD（记得**“全部替换”**！）

终端里执行编译命令：`python setup.py build_ext --inplace`

最后，执行`python3.12 renpy.py`，等待一会，就能看到窗口出现

---
####-> renpy壳

返回桌面，创建renpy-box文件夹
把renpy文件夹、renpy.py和三个.so库都放进renpy-box里
将game文件夹放进renpy-box并执行renpy.py，等待一会就能玩了
