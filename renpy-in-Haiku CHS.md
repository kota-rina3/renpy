## HaikuOS编译运行renpy的法子

进入Haiku后，先更新系统：`pkgman update`，更新完后重启系统
打开终端，安装python3.12和pip：`pkgman install python3.12 pip_python312`
>renpy最低要求**必须**python3.12

接下来安装编译renpy所需依赖：
`pkgman install pkgconf hydrogen_devel freetype_devel ffmpeg6_avdevice ffmpeg6_devel fribidi_devel assimp_devel libsdl2_devel sdl2_gfx_devel sdl2_image_devel sdl2_mixer_devel sdl2_sound_devel sdl2_ttf_devel`

安装所需python模块：
`pip3.12 install assimp cython ecdsa future legacy-cgi pefile requests six typing`
> 可以**追加镜像源**加速下载：-i https://mirrors.aliyun.com/pypi/simple/

上述工作OK后，先进入pygame_sdl2文件夹编译pygame_sdl2模块：
`cd ~/renpy/pygame_sdl2` `python3.12 setup.py install`

> 如果提示**<pygame_sdl2/pygame_sdl2.h>**找不到，请把 **pygame_sdl2.h、pygame.display_api.h、pygame.rwobject_api.h**和**pygame.surface_api.h**放至**/renpy/src/pygame_sdl2**里

装好pygame_sdl2后，退回到renpy文件夹编译renpy模块：
`cd ~/renpy/` `python3.12 setup.py install`

> 如果提示<libhydrogen/impl/random.h>不支持此系统，请编辑random.h（就是加入这两段代码）：
```c
#elif defined(__HAIKU__)
# include "random/unix.h"
```

做完这些，静静等待renpy编译完成
最后输入`python3.12 renpy.py`并等待窗口出现
