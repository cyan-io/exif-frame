<h1><center>Exif Frame</center></h1>

<center>
    无 <del>PhotoShop、小程序</del> 快速✨ 生成 Exif 水印相框🌌 <br/>
    exif frame in an instant without any external dependence
</center>

![sample](https://github.com/cyan-io/exif-frame/raw/main/docs/sample.avif)

| 版本  | 日期       | 更新日志                                        |
| ----- | ---------- | ----------------------------------------------- |
|1.0.5|2024-03-23|支持生成图像质量调整 eg. `-q 95` |
| 1.0.0 | 2024-03-03 | 增加署名支持<br />优化边框样式<br />支持pip安装 |
| 0.93  |            | 增加焦距信息                                    |

## USAGE

Just do it.

```bash
frame [-h] photographs [photographs ...]
```

```text
>frame
================================================================

    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    ██░▄▄▄█▄▀█▀▄█▄░▄██░▄▄▄█████░▄▄▄██░▄▄▀█░▄▄▀██░▄▀▄░██░▄▄▄██
    ██░▄▄▄███░████░███░▄▄██▄▄██░▄▄███░▀▀▄█░▀▀░██░█░█░██░▄▄▄██
    ██░▀▀▀█▀▄█▄▀█▀░▀██░████████░█████░██░█░██░██░███░██░▀▀▀██
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

         v1.0.0 | https://github.com/cyan-io/exif-frame
----------------------------------------------------------------
You can customize your OWN exif frame by modifying these files:
 -CONFIG    <path to exif-frame>\config.yaml
 -FONT_NORM <path to exif-frame>\font\NotoSansSC-Regular.otf
 -FONT_BOLD <path to exif-frame>\font\NotoSansSC-Bold.otf
 -LOGO_DIR  <path to exif-frame>\logo\
 -SIGNATURE <path to exif-frame>\signature.png
----------------------------------------------------------------
usage: frame [-h] photographs [photographs ...]
frame: error: the following arguments are required: photographs
```

## INSTALLATION

以下方法任选其一

1. 使用`pip`安装（推荐√）

```bash
pip install exif-frame -i https://pypi.org/simple
```

2. 下载[release](https://github.com/cyan-io/exif-frame/releases)页面预构建的`exe`文件

3. 使用`python`运行脚本（不推荐×）

4. 从源安装

```bash
git clone git@github.com:cyan-io/exif-frame.git
cd exif-frame
pip install .
```

## CUSTOMIZATION

`<path to exif-frame>` will be displaced by simply running `frame` command

```text
You can customize your OWN exif frame by modifying these files:
 -CONFIG    <path to exif-frame>\config.yaml
 -FONT_NORM <path to exif-frame>\font\NotoSansSC-Regular.otf
 -FONT_BOLD <path to exif-frame>\font\NotoSansSC-Bold.otf
 -LOGO_DIR  <path to exif-frame>\logo\
 -SIGNATURE <path to exif-frame>\signature.png
```

## DONATE

![donate.png (886×443) (cyan-io.github.io)](https://cyan-io.github.io/donate.png)
