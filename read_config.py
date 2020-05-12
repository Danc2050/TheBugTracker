import os
from pathlib import Path
import json

'''
	Config reader: Open config file, if none exist create it
				If file exists read it and leave as placeholder for now
				If not, then create with placeholders and template style
'''

BUGTRACKER = ".bt_config"


class readConfig():

    def __init__(self, user_info=None):
        self.configPath = None
        self.userHome = None
        self.config = {
            "name": {
                "first": "",
                "last": ""
            },
            "email": "",
            "placeholder1": "",
            "placeholder2": "",
            "placeholder3": "",
            "placeholder4": "",
            "placeholder5": "",
        }
        try:
            self.userHome = Path(Path.home())
            self.configPath = os.path.join(self.userHome, BUGTRACKER)
            if Path(self.configPath).is_file() is False:
                self.createDefault()
                print("Created new bug tracker default config file: {0}".format(
                    self.configPath))
            self.config = json.load(open(self.configPath, 'r'))
        except Exception as e:
            print("Unable to load  config file".format())
            raise e

    def createDefault(self, user_info=None):
        """
        Creates a new default config file from the user information
        provided.

        param: user_info: 
                (PLACEHOLDER FOR FUTURE IMPL, I SEE IT BEING A STRUCT OR DICT)

        """
        if user_info is None:
            name = dict(first="John", last="Doe")
            rec = dict(name=name, email="johndoe@doe.com", placeholder1="",
                       placeholder2="", placeholder3="",
                       placeholder4="", placeholder5="")
            print(rec)
            json.dump(rec, fp=open(self.configPath, 'w'), indent=4)

    def showConfig(self):
        """
        Displays the current user configuration file
        """
        if not self.config is None:
            print(self.config)


if __name__ == '__main__':
    # If wanted for testing purposes
    rc = readConfig()
    rc.showConfig()
