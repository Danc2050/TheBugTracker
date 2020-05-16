import os
from pathlib import Path
import json


BUGTRACKER = ".autobug.ini"


class readConfig():

    def __init__(self, user_info=None):
        self.configPath = None
        self.config = None
        try:
            self.configPath = os.path.join(Path.home(), BUGTRACKER)
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
            json.dump(rec, fp=open(self.configPath, 'w'), indent=4)

    def showConfig(self):
        """
        Displays the current user configuration file
        """
        if not self.config is None:
            print(self.config)

    def getConfig(self, key=None):
        """
        Returns a configuration value depending on the key 
        provided. If invalid key provided returns None.
                (NOTE: Getting name key returns dict of first
                                        and last name)
        *CURRENT VALID KEYS: name,email,placeholder1,plaaceholder2,
                                                         placeholder3, placeholder4, placeholder5
        param: key:config file Key
        """
        if not self.config is None:
            try:
                return self.config[key]
            except KeyError:
                print("Invalid configuration key provided")
                return None
