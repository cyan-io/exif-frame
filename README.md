<h1><center>Exif Frame</center></h1>

<center>无 <del>PhotoShop、小程序</del> 快速✨ 生成 Exif 水印相框🌌</center>

![sample](./docs/sample.avif)

| 版本  | 日期       | 更新日志                                        |
| ----- | ---------- | ----------------------------------------------- |
| 1.0.0 | 2024-03-03 | 增加署名支持<br />优化边框样式<br />支持pip安装 |
| 0.93  |            | 增加焦距信息                                    |

## 使用方式

有以下使用方式：

1. 使用`pip`安装（推荐）



1. 使用预构建的`release`文件 
2. 直接运行脚本（不推荐）

### 小 tip

#### ① 拖拽文件

> 将文件拖拽到`frame.exe`上，推荐建立桌面快捷方式

![drag](./docs/drag.avif)

#### ② 命令行方式

> 利用环境变量，可以在任意位置使用命令

![cmd](./docs/cmd.avif)

#### ③ 添加自己的Logo文件

> 仓库默认只提供`尼康`的品牌logo，其它品牌请根据提示，下载`.png`格式的logo文件并以`<相机品牌>.png`的文件名存放在`./logo`文件夹内

样张来源：[Fujifilm X-H2 review samples: Digital Photography Review (dpreview.com)](https://www.dpreview.com/sample-galleries/4783322917/fujifilm-x-h2-review-samples/8533287587)


![logo](./docs/logo.avif)

## 自定义

`./font`	放置自己喜欢的字体

`./config.yml`	配置字体、边距等信息

`./signature.png`	署上自己的大名，可使用https://onlinepngtools.com/convert-text-to-png 快速生成

## 捐赠作者

你的支持是我继续前行的动力！

![donate.png (886×443) (cyan-io.github.io)](https://cyan-io.github.io/donate.png)

---

## Usage

#### Approach① Installation

```bash
pip install exif-frame
```

---

<u>OR</u> clone this repo

```bash
git clone git@github.com:cyan-io/exif-frame.git
```

install

```bash
pip install .
```

#### Approach② Pre-built Distribution

download prebuilt release

```bash
frame.exe path1 path2 ...
```

## Build

See [Makefile](.\Makefile)

## Donate

![donate.png (886×443) (cyan-io.github.io)](https://cyan-io.github.io/donate.png)