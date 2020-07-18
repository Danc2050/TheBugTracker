from configparser import ConfigParser
import os


def config(section):
    filename = os.path.abspath("../resource/Database.ini")

    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found on the {1} file '.format(section, filename))

    return db
