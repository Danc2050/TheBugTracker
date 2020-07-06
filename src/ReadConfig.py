import os
from pathlib import Path
import json

BUGTRACKER = ".autobug.ini"


class readConfig:

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
            print("Unable to load config file".format())
            raise e

    def createDefault(self, user_info=None):
        """
        Creates a new default config file from the user information
        provided.

        param: user_info:
                (PLACEHOLDER FOR FUTURE IMPL, I SEE IT BEING A STRUCT OR DICT)

        """
        if user_info is None:
            rec = dict(first="John", last="Doe", email="johndoe@doe.com",
                       create_debug_log=True, overwrite_previous_entry=False, log_file="log.txt",
                       github_integration=False, github_access_token="",
                       github_repo_name="", send_email=True, send_github_issue=False)
            json.dump(rec, fp=open(self.configPath, 'w'), indent=4)

    def showConfig(self):
        """
        Displays the current user configuration file
        """
        if self.config is not None:
            print(self.config)

    def getConfig(self, key=None):
        """

        Returns a configuration value depending on the key
        provided. If invalid key provided returns None.
        *CURRENT VALID KEYS: name,email,overwrite_previous_entry,create_debug_log,
                             log_file, github_integration, github_access_token,
                             github_repo_name
        param: key:config file Key
        return: config key value
        """
        if self.config is not None:
            try:
                return self.config[key]
            except KeyError:
                print("Invalid configuration key provided")
                return None

    def addToConfig(self, **kwargs):
        """
        addToConfig adds key/value pair entries to current loaded config
        param: **kwargs: varied size key/value dict
        EXAMPLE: **kwargs usage example:
        k = {'Download': True, 'UploadTime': 12, 'ValueName': 'Config1'}
            addToConfig(**k)
        """
        if kwargs is not None:
            if self.config is not None:
                self.config = {**self.config, **kwargs}
                json.dump(self.config, fp=open(self.configPath, 'w'), indent=4)

    def changeConfigValue(self, key=None, value=None):
        """
        Changes the current configuration based on the key and value parameters
        param: key: config key to change
        value: new config key's value
        return: old config key value
        """
        if not self.getConfig(key) is None:
            old_value = self.config[key]
            self.config[key] = value
            json.dump(self.config, fp=open(self.configPath, 'w'), indent=4)
            return old_value
