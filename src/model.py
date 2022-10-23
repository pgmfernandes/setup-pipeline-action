import json


class ConfigPipeline:

    SECRET_SCAN_CONFIG_GITLEKAS = "secret_scan_gitleaks"
    SECRET_SCAN_CONFIG_SEMGREP = "secret_scan_semgrep"
    SECRET_SCAN_CONFIG_TRIVY = "secret_scan_trivy"
    # GENERAL FIELDS
    ORGANIZATION_LBL = 'organization'
    NAME_LBL = 'name'
    PREVIOUS_NAME_LBL = 'previous_names'
    HISTORY_LBL = 'history'
    CONFIG_LBL = 'config'
    PUBLIC_LBL = 'public'
    ARCHIVED_LBL = 'archived'
    EXCEPTION_LBL = 'exception'

    def __init__(self, json_obj):
        self.org = json_obj[ConfigPipeline.ORGANIZATION_LBL]
        self.name = json_obj[ConfigPipeline.NAME_LBL]
        self.previous_names = json_obj[ConfigPipeline.PREVIOUS_NAME_LBL]
        self.history = json_obj[ConfigPipeline.HISTORY_LBL]
        self.config = json_obj[ConfigPipeline.CONFIG_LBL]
        self.public = json_obj[ConfigPipeline.PUBLIC_LBL]
        self.archived = json_obj[ConfigPipeline.ARCHIVED_LBL]

    @staticmethod
    def create_default():
        json_obj = {
              ConfigPipeline.NAME_LBL: None,
              ConfigPipeline.ORGANIZATION_LBL: None,
              ConfigPipeline.ARCHIVED_LBL: None,
              ConfigPipeline.PUBLIC_LBL: None,
              ConfigPipeline.PREVIOUS_NAME_LBL: [],
              ConfigPipeline.CONFIG_LBL: {},
              ConfigPipeline.EXCEPTION_LBL: {},
              ConfigPipeline.HISTORY_LBL: []
        }
        default_object = ConfigPipeline(json_obj=json_obj)
        return default_object


class ConfigPipelineHelper:
    @staticmethod
    def parse_config_pipeline_from_json(json_content) -> ConfigPipeline:
        resultDict = json.loads(json_content)
        obj = ConfigPipeline(resultDict)
        return obj
