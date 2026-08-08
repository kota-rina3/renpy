# Ren'Py视觉小说引擎

[English](https://github.com/renpy/renpy/blob/master/README.rst) 简体中文

![Logo](https://img.shields.io/github/stars/kota-rina3/renpy) ![Logo](https://img.shields.io/badge/platform-Windows%20%7C%20MacOS%20%7C%20Linux%20%7C%20FreeBSD%20%7C%20HaikuOS-yellow) ![Logo](https://img.shields.io/badge/CPU_architecture-x64%20%7C%20arm64%20%7C%20loong64-%23ea4300) ![Logo](https://img.shields.io/badge/deepin_package_name-otohime.renpy.ayasaki.otome-0050ff) ![Logo](https://img.shields.io/github/v/release/kota-rina3/renpy) ![Logo](https://img.shields.io/github/downloads/kota-rina3/renpy/total)

[https://www.renpy.org](https://www.renpy.org)

## 分支

以下分支你可能会感兴趣：

`fix`

>fix 分支用于修复当前版本的 Ren'Py，无需做出危险更改。fix 分支也是[https://www.renpy.org](https://www.renpy.org)上文档的来源。这个分支会定期自动合并到 master 分支。\
包含修复或文档改进的合并请求应该提交到 fix 分支。当发布新特性版本时（例如从 8.6.x 到 8.7.0），master 分支会同步到 fix 分支。\
fix 版本会从该分支构建。

`master`

> master 分支是开发的主要焦点所在。这个分支最终将成为 Ren'Py 的下一个版本。\
包含新特性、需要不兼容变更或对 Ren'Py 内部进行重大修改的拉取请求应该指向 master 分支。\
新特性版本用这个分支构建。

## 入门

Ren'Py 依赖许多用 Cython 和 C 编写的 Python 模块。对于仅涉及 Python 模块的 Ren'Py 更改，你可以使用每夜构建中的模块。否则，你得自行编译这些模块。

假设开发脚本的运行环境为符合 POSIX 标准的类 Unix 系统。这些脚本应在 Linux 或 macOS 上运行，Windows 可在 MSYS 等环境上运行。

## 夜间构建

夜间构建可从以下地址获得：

> [https://nightly.renpy.org](https://nightly.renpy.org)

请注意最新的夜间构建位于列表底部。解压夜间构建后，切换到此仓库，并执行：

> ./after_checkout.sh <path-to-nightly>

一旦此脚本执行完成，就能使用 renpy.sh、renpy.app 或 renpy.exe 来运行 Ren'Py，具体取决于你的平台。

如果当前的夜间构建版本无法运行，请等待 24 小时等待新的构建。如果新的构建仍无法运行，请联系 Tom（pytom at bishoujo.us，或在 Twitter/X 上 @renpytom）报告bug。

`doc` 符号链接将空着，直到按下文所述构建文档。

## 编译模块

构建模块需要在系统上安装许多依赖项。在 Ubuntu 和 Debian 上，这些依赖可通过apt安装：

> sudo apt install python3-dev libassimp-dev libavcodec-dev libavformat-dev \
libswresample-dev libswscale-dev libharfbuzz-dev libfreetype6-dev libfribidi-dev libsdl3-dev \
libsdl3-image-dev libsdl3-mixer-dev libsdl3-ttf-dev libjpeg-dev pkg-config \
python3-legacy-cgi

Ren'Py 需要 SDL_image 3.2 以上。如果你的发行版不包含该版本，从以下链接下载：

> [https://github.com/libsdl-org/SDL_image](https://github.com/libsdl-org/SDL_image)

我们强烈建议使用包管理器来创建虚拟环境和管理依赖项。我们测试过 [uv](https://docs.astral.sh/uv/)，但其他包管理器也应该可以正常工作。要创建虚拟环境并安装依赖项，右键终端并执行：

> uv sync

之后，编译扩展模块并使用命令运行 Ren'Py：

> ./run.sh --build

## 其他平台

在支持的情况下，Ren'Py 会尝试使用 pkg-config 查找目录和库路径。如果 pkg-config 不存在，可配置 CFLAGS 和 LDFLAGS 指定查找目录和库路径。

如果环境变量中存在 RENPY_CFLAGS 而没有 CFLAGS，setup.py 会将 CFLAGS 设置为 RENPY_CFLAGS。对 RENPY_LDFLAGS、RENPY_CC、RENPY_CXX 和 RENPY_LD 也一样。

setup.py 不支持交叉编译。请查看 [https://github.com/renpy/renpy-build](https://github.com/renpy/renpy-build) 获取为多个平台交叉编译的 Ren'Py 。renpy-build 还包含Android、iOS 和 Web 的运行时组件。

## 文档

### 构建

构建文档需要 Ren'Py 能运行。你需要链接到夜间构建版本，或者按照上述说明编译模块。还需要 [Sphinx](https://www.sphinx-doc.org/) 文档生成器。如果安装了 pip，可通过下面命令安装 Sphinx：

> pip install -U sphinx sphinx_rtd_theme sphinx_rtd_dark_mode sphinx-tabs

装完 Sphinx 后，cd进 Ren'Py 代码库中的 `sphinx` 目录并执行：

> ./build.sh

## 格式

Ren'Py 的文档由位于 sphinx/source 中的 reStructuredText 文件和散布在整个代码中的函数文档字符串生成的文档组成。不能直接编辑 `sphinx/source/inc` 文件夹中的文件，因为它们将被覆盖。

文档字符串在开始的几行可能包含标签：

***:doc: section kind***

表示这个函数需要被文档化。section 给出该函数将被文档化的包含文件的名称，而 kind 指示要文档化的对象的类型（ `function` 、 `method` 或 `class` 。如果省略，kind 将自动检测。

***:name: name***

要文档化的函数的名称。函数名称通常会被检测到，因此只有在函数有多个别名时才需要指定。

***:args: args***

这会覆盖检测到的参数列表。如果函数的某些参数已弃用，可以使用它。

例如：

```python
def warp_speed(factor, transwarp=False):
    """
    :doc: warp
    :name: renpy.warp_speed
    :args: (factor)

    Exceeds the speed of light.

    `factor`
        The warp factor. See Sternbach (1991) for details.

    `transwarp`
        If True, use transwarp. This does not work on all platforms.
    """

    renpy.engine.warp_drive.engage(factor)
```

## 本地化

在翻译启动器和模板游戏方面，最佳实践请阅读：

[https://lemmasoft.renai.us/forums/viewtopic.php?p=321603#p321603](https://lemmasoft.renai.us/forums/viewtopic.php?p=321603#p321603)

## 贡献

对于错误修复、文档改进和简单变更，只需提交拉取请求。对于重要变更，先开issue，以便讨论变更计划。

## 效率工具（包括AI模型）

Ren'Py 的目标是提供能够体现人类创造力的工具，用于制作视觉小说和类似类型的游戏。为实现这一目标，开发者可以使用提高效率的工具，包括使用AI模型。

对 Ren'Py 的任何更改都必须由理解更改内容、受此更改影响的 Ren'Py 部分以及更改版权影响的人类创建。我们认为适当的效率工具使用示例包括：人类仅接受他们理解且正确的建议的补全，以及导致人类可以立即审查以确认正确性的提示。较大的更改可以通过提示进行较小的更改，并在每一步进行审查来创建。

我们不接受人类不完全理解更改及其对 Ren'Py 影响的情况。使用最小人类审查进行的大规模更改（“氛围编程”）是不可接受的。如果您想进行此类更改，最好直接在 GitHub 上提出想法，让我们更改。未经人类审查由代理进行的更改是不可接受的。

我们使用 AI 的目的无需在[ Steam 内容调查](https://partner.steamgames.com/doc/gettingstarted/contentsurvey#5)中披露。具体来说，我们不使用扩散模型或其他技术来生成玩家消费的游戏内容，并且不要求创作者使用任何 AI 工具，也不为创作者提供任何此类工具。

有个例外，当没有人为该语言提供翻译时，我们允许机翻。当有人提供翻译时，翻译者的工作将优先。这种例外允许系统消息被翻译，以改善可访问性。

## 许可证

有关完整的许可证条款，请阅读：

[https://www.renpy.org/doc/html/license.html](https://www.renpy.org/doc/html/license.html)

通过为 Ren'Py 做出贡献，你同意根据 MIT 许可证对你的贡献进行许可。做出贡献时，你可以选择：

* 保留您贡献的版权。如果您选择这种方式，请在您修改的任何文件的版权声明中注明"版权 (年份) 您的名字 <您的邮箱>"。

* 将您的贡献版权授予 Tom Rothamel < [pytom@bishoujo.us](pytom@bishoujo.us)>。如果您没有特别说明，默认选这种。