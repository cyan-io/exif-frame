from PIL import Image, ImageDraw, ImageFont, ImageOps
from PIL.ExifTags import TAGS
from .util import (
    get_exif_data,
    get_camera_info,
    get_printalbe_text,
    print_in_red,
)
import pathlib
import argparse
import pkg_resources
import yaml


config_path = pkg_resources.resource_filename(__name__, "config.yaml")
with open(config_path, "r", encoding="utf-8") as yml:
    config = yaml.load(yml, Loader=yaml.FullLoader)
font_size = config.get("FONT_SIZE")
signature_path = pkg_resources.resource_filename(__name__, "signature.png")
font_bold_path = pkg_resources.resource_filename(
    __name__, "font/" + config.get("FONT_BOLD")
)
font_norm_path = pkg_resources.resource_filename(
    __name__, "font/" + config.get("FONT_NORM")
)
logo_path = pkg_resources.resource_filename(__name__, "logo/")
font_norm = ImageFont.truetype(
    font_norm_path,
    size=font_size,
)
font_bold = ImageFont.truetype(
    font_bold_path,
    size=font_size,
)

# 边距
PADDING = config.get("PADDING")
DEFAULT_EXIF_MESSAGE = config.get("DEFAULT_EXIF_MESSAGE")

PADDING_LEFT = 0
COLOR_BLACK = (0, 0, 0)
COLOR_GREY = (100, 100, 100)

EXIF_CONTENT_HEIGHT = 256


def exec(image_path):
    # extract Exif
    exif_data = get_exif_data(image_path)
    camera_info = get_camera_info(exif_data)
    a, b, c, d = (
        camera_info.get("FocalLength", DEFAULT_EXIF_MESSAGE),
        camera_info.get("ISO", DEFAULT_EXIF_MESSAGE),
        camera_info.get("FNumber", DEFAULT_EXIF_MESSAGE),
        camera_info.get("ExposureTime", DEFAULT_EXIF_MESSAGE),
    )
    text_ise = (
        DEFAULT_EXIF_MESSAGE
        if DEFAULT_EXIF_MESSAGE in (a, b, c, d)
        else "{}mm ISO{} f{} {}".format(int(a), b, c, d)
    )
    make = camera_info.get("Make")
    text_model = "{}".format(camera_info.get("Model", DEFAULT_EXIF_MESSAGE))
    text_lens = "{}".format(camera_info.get("LensModel", DEFAULT_EXIF_MESSAGE))
    text_datetime = "{}".format(
        camera_info.get("DateTimeOriginal", DEFAULT_EXIF_MESSAGE)
    )

    make = get_printalbe_text(make)
    text_model = get_printalbe_text(text_model)
    text_lens = get_printalbe_text(text_lens)
    text_datetime = get_printalbe_text(text_datetime)
    # log
    print(make, text_model, text_lens, text_datetime, sep="\n")

    # sketchpad
    photo = Image.open(image_path).convert("RGBA")
    photo = ImageOps.exif_transpose(photo)
    photo_width, photo_height = photo.size

    sketchpad = Image.new(
        "RGB", (photo_width, photo_height + EXIF_CONTENT_HEIGHT), (255, 255, 255)
    )
    sketchpad.paste(photo, (0, 0), photo)
    draw = ImageDraw.Draw(sketchpad)

    PADDING_TOP = PADDING + photo_height  # - 20

    # draw signature
    try:
        signature = Image.open(signature_path)
    except Exception as e:
        print_in_red("JUMP: signature not exists")
        signature = None
    finally:
        if signature:
            width, height = signature.size
            new_width = int((154 / height) * width)
            signature = signature.resize((new_width, 154), Image.LANCZOS).convert(
                "RGBA"
            )
            sketchpad.paste(
                signature,
                (
                    PADDING_LEFT,
                    PADDING_TOP,
                ),
                signature,
            )

    # draw text
    draw.text(
        (
            PADDING_LEFT + (0 if not signature else signature.size[0] + PADDING),
            PADDING_TOP,
        ),
        text_ise,
        fill=COLOR_BLACK,
        font=font_bold,
    )

    draw.text(
        (
            PADDING_LEFT + (0 if not signature else signature.size[0] + PADDING),
            PADDING_TOP + 80,
        ),
        text_datetime,
        fill=COLOR_GREY,
        font=font_norm,
    )

    max_len = max(font_bold.getlength(text_model), font_norm.getlength(text_lens))
    position_make = (photo_width - max_len, PADDING_TOP)
    position_lens = (photo_width - max_len, PADDING_TOP + 80)

    draw.text(
        position_make,
        text_model,
        fill=COLOR_BLACK,
        font=font_bold,
        align="left",
    )

    draw.line(
        (
            (position_make[0] - PADDING // 2, position_make[1] + 10),
            (position_lens[0] - PADDING // 2, PADDING_TOP + 154),
        ),
        fill=COLOR_GREY,
        width=4,
    )

    draw.text(
        position_lens,
        text_lens,
        fill=COLOR_GREY,
        font=font_norm,
    )

    # draw logo
    try:
        logo = Image.open(pkg_resources.resource_filename(__name__, f"logo/{make}.png"))
    except Exception as e:
        print_in_red(f"请存放 {make}.png 至 {logo_path}\nMissing {make}.png in {logo_path}")
        logo = None
    finally:
        if logo:
            width, height = logo.size
            new_width = int((154 / height) * width)
            logo = logo.resize((new_width, 154), Image.LANCZOS).convert("RGBA")
            sketchpad.paste(
                logo,
                (
                    int(photo_width - max_len - logo.size[0] - PADDING),
                    PADDING_TOP,
                ),
                logo,
            )

    # TODO
    final_image = Image.new(
        "RGB", (sketchpad.size[0] + 128, sketchpad.size[1] + 64), (255, 255, 255)
    )
    final_image.paste(sketchpad, (64, 64), sketchpad.convert("RGBA"))

    # 保存
    ori_path = pathlib.Path(image_path)
    final_image.save(ori_path.parent / f"{ori_path.stem}_exif_frame{ori_path.suffix}")


def main():
    print(
        "=" * 64,
        "Exif-Frame v1.0.0",
        "\thttps://github.com/cyan-io/exif-frame",
        "\thttps://space.bilibili.com/266211787",
        "-" * 64,
        sep="\n",
    )
    print(
        f"CONFIG    {config_path}",
        f"FONT_NORM {font_norm_path}",
        f"FONT_BOLD {font_bold_path}",
        f"LOGO_DIR  {logo_path}",
        f"SIGNATURE {signature_path}",
        "-" * 64,
        sep="\n",
    )
    argparser = argparse.ArgumentParser(prog="frame")
    argparser.add_argument("photographs", nargs="+", help="input file paths")
    args = argparser.parse_args()

    for photo in args.photographs:
        print(f">>> {photo}", sep="\n")
        try:
            exec(photo)
        except Exception as e:
            print_in_red("Failed: Try to Check the EXIF Infomation", e, sep="\n")
        print("-" * 64)
