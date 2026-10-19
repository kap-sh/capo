"""Generated from Smithy shape ``com.amazonaws.fis#CreateExperimentTemplateLogConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_cloud_watch_logs_log_configuration_input
    import capo_fis.types.experiment_template_s3_log_configuration_input
    import capo_fis.types.log_schema_version


class CreateExperimentTemplateLogConfigurationInput(TypedDict, closed=True):
    cloud_watch_logs_configuration: NotRequired[
        "capo_fis.types.experiment_template_cloud_watch_logs_log_configuration_input.ExperimentTemplateCloudWatchLogsLogConfigurationInput"
    ]
    """<p>The configuration for experiment logging to Amazon CloudWatch Logs.</p>"""
    s3_configuration: NotRequired[
        "capo_fis.types.experiment_template_s3_log_configuration_input.ExperimentTemplateS3LogConfigurationInput"
    ]
    """<p>The configuration for experiment logging to Amazon S3.</p>"""
    log_schema_version: "capo_fis.types.log_schema_version.LogSchemaVersion"
    """<p>The schema version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExperimentTemplateLogConfigurationInput) -> dict:
    out: dict = {}
    if "cloud_watch_logs_configuration" in value:
        import capo_fis.types.experiment_template_cloud_watch_logs_log_configuration_input

        out["cloudWatchLogsConfiguration"] = (
            capo_fis.types.experiment_template_cloud_watch_logs_log_configuration_input.serialize_json(
                value["cloud_watch_logs_configuration"]
            )
        )
    if "s3_configuration" in value:
        import capo_fis.types.experiment_template_s3_log_configuration_input

        out["s3Configuration"] = (
            capo_fis.types.experiment_template_s3_log_configuration_input.serialize_json(
                value["s3_configuration"]
            )
        )
    out["logSchemaVersion"] = value["log_schema_version"]
    return out


def deserialize_json(data: dict) -> CreateExperimentTemplateLogConfigurationInput:
    out: CreateExperimentTemplateLogConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudWatchLogsConfiguration") is not None:
        import capo_fis.types.experiment_template_cloud_watch_logs_log_configuration_input

        out["cloud_watch_logs_configuration"] = (
            capo_fis.types.experiment_template_cloud_watch_logs_log_configuration_input.deserialize_json(
                data["cloudWatchLogsConfiguration"]
            )
        )
    if data.get("s3Configuration") is not None:
        import capo_fis.types.experiment_template_s3_log_configuration_input

        out["s3_configuration"] = (
            capo_fis.types.experiment_template_s3_log_configuration_input.deserialize_json(
                data["s3Configuration"]
            )
        )
    if data.get("logSchemaVersion") is not None:
        out["log_schema_version"] = data["logSchemaVersion"]
    else:
        out["log_schema_version"] = 0
    return out
