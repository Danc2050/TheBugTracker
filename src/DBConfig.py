from configparser import ConfigParser


def config(section):
    filename = 'Database.ini'
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section{0} mpt fpimd om tje {1} file'.format(section, filename))

    return db
