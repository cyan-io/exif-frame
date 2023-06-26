from PIL import Image, ImageDraw, ImageFont, ImageOps
from PIL.ExifTags import TAGS
from util import (
    get_exif_data,
    get_camera_info,
    get_printalbe_text,
    print_Y,
    print_R,
    print_G,
)
import yaml
import sys
import pathlib
import os

# For Distribution
os.chdir(pathlib.Path(sys.executable).parent)

print_Y("------------------------------------------------")
print_Y(
    "\n  Exif-Frame v0.91\n\n\thttps://github.com/cyan-io/exif-frame\n\thttps://space.bilibili.com/266211787\n"
)
print_Y("------------------------------------------------\n")


# 加载配置
with open("config.yml", encoding="utf-8") as _:
    config = yaml.load(_, Loader=yaml.FullLoader)
# 字体大小
font_size = config.get("font_size", 0)
# 字体文件
font_regular = ImageFont.truetype(
    config.get("font_regular", "./font/NotoSansSC-Regular.otf"), size=font_size
)
font_bold = ImageFont.truetype(
    config.get("font_bold", "./font/NotoSansSC-Bold.otf"), size=font_size
)
# 边距
PADDING = int(config.get("padding", 0))


PADDING_LEFT = PADDING
COLOR_BLACK = (0, 0, 0)
COLOR_GREY = (100, 100, 100)


def exec(image_path):
    print(f"\n>>> {image_path}")

    # 获取Exif
    exif_data = get_exif_data(image_path)
    camera_info = get_camera_info(exif_data)

    text_ise = "ISO{} f{} {}".format(
        camera_info.get("ISO", "N/A"),
        camera_info.get("FNumber", "N/A"),
        camera_info.get("ExposureTime", "N/A"),
    )
    text_model = "{}".format(camera_info.get("Model", "N/A"))
    text_lens = "{}".format(camera_info.get("LensModel", "N/A"))
    text_datetime = "{}".format(camera_info.get("DateTimeOriginal", "N/A"))
    text_lens = get_printalbe_text(text_lens)

    # 绘图
    image_original = Image.open(image_path).convert("RGBA")
    image_original = ImageOps.exif_transpose(image_original)
    image_size = image_original.size

    image = Image.new("RGB", (image_size[0], image_size[1] + 450), (255, 255, 255))
    image.paste(image_original, (0, 0), image_original)
    draw = ImageDraw.Draw(image)

    PADDING_TOP = PADDING + image_size[1]  # - 20

    draw.text(
        (PADDING_LEFT, PADDING_TOP), text_ise, fill=COLOR_BLACK, font=font_bold,
    )

    draw.text(
        (PADDING_LEFT, PADDING_TOP + 120),
        text_datetime,
        fill=COLOR_GREY,
        font=font_regular,
    )

    max_len = max(font_bold.getlength(text_model), font_regular.getlength(text_lens))
    position_make = (image_size[0] - PADDING - max_len, PADDING_TOP)
    position_lens = (image_size[0] - PADDING - max_len, PADDING_TOP + 120)

    draw.text(
        position_make, text_model, fill=COLOR_BLACK, font=font_bold, align="left",
    )

    draw.line(
        (
            (position_make[0] - PADDING // 2, position_make[1] + 10),
            (position_lens[0] - PADDING // 2, PADDING_TOP + 20 + 210),
        ),
        fill=COLOR_GREY,
        width=4,
    )

    draw.text(
        position_lens, text_lens, fill=COLOR_GREY, font=font_regular,
    )

    make = camera_info.get("Make")
    try:
        logo = Image.open(f"./logo/{make}.png")
        width, height = logo.size
        new_width = int((210 / height) * width)
        logo = logo.resize((new_width, 210), Image.LANCZOS).convert("RGBA")

    except Exception as e:
        print_R(f"请存放 {make}.png 至 logo 文件夹\nMissing {make}.png in ./logo folder")
        return

    image.paste(
        logo,
        (
            int(image_size[0] - max_len - PADDING - logo.size[0] - PADDING),
            PADDING_TOP + 20,
        ),
        logo,
    )

    # 保存
    ori_path = pathlib.Path(image_path)
    image.save(ori_path.parent / f"{ori_path.stem}_with_frame{ori_path.suffix}")


if __name__ == "__main__":
    argv = sys.argv[1:]
    if not argv:
        print_R("使用方式：frame 路径1 ... | Usage: frame path1 ...")
    for image_path in argv:
        exec(image_path)

    print_G("\n\n回车键退出 | Enter to exit")
    input()
