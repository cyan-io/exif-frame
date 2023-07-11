## 介绍

无 PhotoShop、小程序<u>**一秒**</u>生成 Exif 水印相框

![sample](./readme/sample.jpg)

👆`v0.93`已增加焦距信息

## 使用方式

下载release并解压到任意位置

#### ① 拖拽文件

> 将文件拖拽到`frame.exe`上，推荐建立桌面快捷方式

![frame-drag](./readme/frame-drag.gif)

#### ② 命令行方式

> 利用环境变量，可以在任意位置使用命令

![frame-cmd](./readme/frame-cmd.gif)

#### ③ 添加自己的Logo文件

> 仓库默认只提供`尼康`的品牌logo，其它品牌请根据提示，下载`.png`格式的logo文件并以`<相机品牌>.png`的文件名存放在`./logo`文件夹内

样张来源：[Fujifilm X-H2 review samples: Digital Photography Review (dpreview.com)](https://www.dpreview.com/sample-galleries/4783322917/fujifilm-x-h2-review-samples/8533287587)


![frame-logo](./readme/frame-logo.gif)

## 自定义

`./font`	放置自己喜欢的字体

`./config.yml`	配置字体、边距等信息

## 捐赠作者

你的支持是我继续前行的动力！

![donate.png (886×443) (cyan-io.github.io)](https://cyan-io.github.io/donate.png)

---

## Usage

#### Approach① Installation

```bash
pip install -r requirments.txt
```

```bash
python index.py path1 path2 ...
```

#### Approach② Pre-built Distribution

```bash
frame path1 path2 ...
```

## Build

```bash
pip install pyinstaller
```

#### Windows

```bash
pyinstaller -D --add-data ./font;font --add-data ./logo;logo --add-data config.yml;. -n frame -i icon.ico index.py
```

#### Unix Like（untested）

```bash
pyinstaller -D --add-data ./font:font --add-data ./logo:logo --add-data config.yml:. -n frame index.py
```

## Donate

![donate.png (886×443) (cyan-io.github.io)](https://cyan-io.github.io/donate.png)