from github import Github


class GithubIntegration:

    def __init__(self, githubAccessToken, githubRepo):
        """
        Both github_access_token and github_repo_name are required in the configuration file
        to use the github integration
        """
        self.githubAccessToken = githubAccessToken
        self.repoName = githubRepo
        try:
            self.github = Github(self.githubAccessToken)
            self.githubRepo = self.github.get_repo(self.repoName)
        except Exception as e:
            raise Exception("Unable to authenticate access token or find github repo " + str(e))

    def closeIssue(self, issueNumber):
        """
        Close an open issue

        :param issueNumber: The id corresponding to an issue
        :return: An exception if an error occurs while closing
        """
        try:
            issue = self.githubRepo.get_issue(number=issueNumber)
            issue.edit(state="closed")
        except Exception as e:
            raise Exception("Error closing issue: " + str(issueNumber) + " " + str(e))

    def getAllOpenIssues(self):
        """
        Gets all open issues for the given repo

        :return: All open Issues for the provided repo in the configuration file
        """
        try:
            openIssues = []
            openIssuesWithPRs = self.githubRepo.get_issues(state='open')
            for issue in openIssuesWithPRs:
                if not issue.pull_request:
                    openIssues.append(issue)
            return openIssues
        except Exception as e:
            raise Exception("Error retrieving all open issues: " + str(e))

    def getLabels(self, labelsFromRequest):
        """
        Checks if the given label is a valid label and then returns
        the github label to create an issue with

        :param labelsFromRequest: The wanted labels for an issue
        The labels must be in the format "label1,label2,label3"
        :return: the converted string label to github label
        """
        labelsList = []
        labels = labelsFromRequest.split(',')
        try:
            for label in labels:
                labelsList.append(self.githubRepo.get_label(label))
            return labelsList
        except Exception as e:
            raise Exception("Unable to retrieve label(s): " + labelsFromRequest + " " + str(e))

    # before adding to database it should catch for duplicate
    def createIssue(self, githubIssue):
        """
        Creates an issue to the given repo

        :param githubIssue: The github issue object to send to github
        :return: The created issue's information
        """
        try:
            if not githubIssue.title:
                raise Exception("Title is needed for a github issue")

            if (not githubIssue.body) and (not githubIssue.labels) and \
                    (not githubIssue.assignee) and (not githubIssue.milestone):
                return self.githubRepo.create_issue(title=githubIssue.title)

            if (not githubIssue.labels) and (not githubIssue.assignee) and \
                    (not githubIssue.milestone):
                return self.githubRepo.create_issue(title=githubIssue.title, body=githubIssue.body)

            if (not githubIssue.assignee) and (not githubIssue.milestone):
                labelsFromRequest = self.getLabels(githubIssue.labels)
                return self.githubRepo.create_issue(title=githubIssue.title, body=githubIssue.body,
                                                    labels=labelsFromRequest)
            if not githubIssue.milestone:
                labelsFromRequest = self.getLabels(githubIssue.labels)
                return self.githubRepo.create_issue(title=githubIssue.title, body=githubIssue.body,
                                                    labels=labelsFromRequest, milestone=githubIssue.milestone)
        except Exception as e:
            raise Exception("Error creating issue for Github Repo: " + str(self.githubRepo) +
                            " with Exception " + str(e))
