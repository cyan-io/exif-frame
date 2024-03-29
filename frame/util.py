from PIL import Image
from PIL.ExifTags import TAGS


def _print_in_color(color: str, *args, **kwargs):
    args = [str(_) for _ in args]
    args[0] = color + args[0]
    args[-1] = args[-1] + "\033[0m"
    print(*args, **kwargs)


def print_in_red(*args, **kwargs):
    _print_in_color("\033[0;31m", *args, **kwargs)


def print_in_green(*args, **kwargs):
    _print_in_color("\033[0;32m", *args, **kwargs)


def print_in_yellow(*args, **kwargs):
    _print_in_color("\033[0;33m", *args, **kwargs)


def get_exif_data(image_path):
    exif_data = {}
    try:
        with Image.open(image_path) as img:
            info = img._getexif()
            if info is not None:
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    exif_data[decoded] = value
    except (IOError, AttributeError, KeyError, IndexError) as e:
        print("Failed to extract EXIF data:", str(e))

    return exif_data


def get_camera_info(exif_data):
    camera_info = {}

    if "Make" in exif_data:
        camera_info["Make"] = exif_data["Make"]

    if "Model" in exif_data:
        camera_info["Model"] = exif_data["Model"]

    if "ExposureTime" in exif_data:
        exposure_time = exif_data["ExposureTime"]
        camera_info["ExposureTime"] = (
            f"1/{1 // exposure_time}s" if exposure_time < 1.0 else f"{exposure_time}s"
        )

    if "FNumber" in exif_data:
        f_number = exif_data["FNumber"]
        camera_info["FNumber"] = f_number

    if "ISOSpeedRatings" in exif_data:
        camera_info["ISO"] = exif_data["ISOSpeedRatings"]

    if "DateTimeOriginal" in exif_data:
        camera_info["DateTimeOriginal"] = exif_data["DateTimeOriginal"]

    if "LensModel" in exif_data:
        camera_info["LensModel"] = exif_data["LensModel"]

    if "FocalLength" in exif_data:
        camera_info["FocalLength"] = exif_data["FocalLength"]

    return camera_info


TEXT_PRINTABLE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "


def get_printalbe_text(string):
    cnt = 0
    for c in string:
        if c in TEXT_PRINTABLE:
            cnt += 1
        else:
            return string[:cnt]
    return string
