#!/usr/bin/env python3

# region * Imports

from captcha.image import ImageCaptcha
from random import choices
from root.constant.captcha import CAPTCHA, CAPTCHA_LENGTH

# endregion


def generate_random_string():
    return "".join(choices(CAPTCHA, k=CAPTCHA_LENGTH))


def generate_image_data(captcha_text: str):
    image: ImageCaptcha = ImageCaptcha(150, 100)
    data = image.generate(captcha_text)
    return data
