#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 10632057))
    API_HASH = os.environ.get("API_HASH", "6b343fdad5be6551cf29ab874079a680")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5294843580:AAHcjgzILHE0STujSVY6FvksJslxLPeCO1s") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@lokidatabase")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", 2112087070)
    LIMIT = int(os.environ.get("LIMIT", "500000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "AQCojYdZjB_ucXz-jsd_Hcu5MwEGU_-ssGNU2I2-lFOh5aGhAQooY5W1ar9pD-qzyjzg-QLVgeV1ylwrnmiVbROhwf39gqm42-kMtGGs7qKueaRcJ4JRjWTGZNAOXyKz0KBYakIEMqtcBQKMkYG-ynWa101VMZJc5x3P62JFrmoH5XILvADvF_6cMzdaVw6mY0H-VhsCy-FrT5qDTi6rz4lgNCZfDBW5jUiEJj4seIZqvxnXXY8S3tEs6OIPgaWo3KZ0-hAdtI6mTVC0LxKYa4u6H8U2duJybSfRNtN_e42tkGscVKv6UAiIMq4EyAUxtLdSdCUOfq3zhpFpj30QLR9ifePkHgA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", -1001490715667))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
