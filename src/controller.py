import os

from repository import *
from model import ConfigPipelineHelper, ConfigPipeline


class ConfigRepositoryController:

    def __init__(self, github_auth, github_reposiroty):
        self.config_manager = CyberConfigRepositoryManager(github_auth=github_auth)
        self.github_repository = github_reposiroty

    def execute_configuration(self):
        config_json = self.config_manager.get_config_json(owner_and_repo_name=self.github_repository)
        if config_json is not None:
            # print(config_json)
            config_pipeline = ConfigPipelineHelper.parse_config_pipeline_from_json(config_json)
            if config_pipeline is None:
                print(f"::error:Json of configuration is not valid for {self.github_repository}.")
                return
        else:
            config_pipeline = ConfigRepositoryController.create_default_config()
        ConfigRepositoryController.export_output(config_pipeline)

    @staticmethod
    def create_default_config():
        return ConfigPipeline.create_default()

    @staticmethod
    def export_output(task: ConfigPipeline):
        GITHUB_OUTPUT = os.getenv('GITHUB_OUTPUT')
        with open(GITHUB_OUTPUT, "a") as myfile:
            for key in task.config:
                value = task.config[key]
                myfile.write(f"{key}={str(value)}\n")
                print(f"{key}={str(value)}")

