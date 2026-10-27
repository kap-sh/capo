"""Generated from Smithy shape ``com.amazonaws.deadline#JobDetailsEntity``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.iam_role_arn
    import capo_deadline.types.job_details_job_attachment_settings
    import capo_deadline.types.job_id
    import capo_deadline.types.job_parameters
    import capo_deadline.types.job_run_as_user
    import capo_deadline.types.openjd_extension_name_list
    import capo_deadline.types.path_mapping_rules
    import capo_deadline.types.string


class JobDetailsEntity(TypedDict, closed=True):
    job_id: "capo_deadline.types.job_id.JobId"
    """The job ID."""
    job_attachment_settings: NotRequired[
        "capo_deadline.types.job_details_job_attachment_settings.JobDetailsJobAttachmentSettings"
    ]
    """The job attachment settings."""
    job_run_as_user: NotRequired["capo_deadline.types.job_run_as_user.JobRunAsUser"]
    """The user name and group that the job uses when run."""
    log_group_name: "capo_deadline.types.string.String"
    """The log group name."""
    queue_role_arn: NotRequired["capo_deadline.types.iam_role_arn.IamRoleArn"]
    """The queue role ARN."""
    parameters: NotRequired["capo_deadline.types.job_parameters.JobParameters"]
    """The parameters."""
    schema_version: "capo_deadline.types.string.String"
    """The schema version."""
    extensions: NotRequired[
        "capo_deadline.types.openjd_extension_name_list.OpenjdExtensionNameList"
    ]
    """The Open Job Description extensions that the job template uses. This value is used by the worker agent."""
    path_mapping_rules: NotRequired[
        "capo_deadline.types.path_mapping_rules.PathMappingRules"
    ]
    """The path mapping rules."""


# --- restJson1 ser/de ---
def serialize_json(value: JobDetailsEntity) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    if "job_attachment_settings" in value:
        import capo_deadline.types.job_details_job_attachment_settings

        out["jobAttachmentSettings"] = (
            capo_deadline.types.job_details_job_attachment_settings.serialize_json(
                value["job_attachment_settings"]
            )
        )
    if "job_run_as_user" in value:
        import capo_deadline.types.job_run_as_user

        out["jobRunAsUser"] = capo_deadline.types.job_run_as_user.serialize_json(
            value["job_run_as_user"]
        )
    out["logGroupName"] = value["log_group_name"]
    if "queue_role_arn" in value:
        out["queueRoleArn"] = value["queue_role_arn"]
    if "parameters" in value:
        import capo_deadline.types.job_parameters

        out["parameters"] = capo_deadline.types.job_parameters.serialize_json(
            value["parameters"]
        )
    out["schemaVersion"] = value["schema_version"]
    if "extensions" in value:
        import capo_deadline.types.openjd_extension_name_list

        out["extensions"] = (
            capo_deadline.types.openjd_extension_name_list.serialize_json(
                value["extensions"]
            )
        )
    if "path_mapping_rules" in value:
        import capo_deadline.types.path_mapping_rules

        out["pathMappingRules"] = capo_deadline.types.path_mapping_rules.serialize_json(
            value["path_mapping_rules"]
        )
    return out


def deserialize_json(data: dict) -> JobDetailsEntity:
    out: JobDetailsEntity = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("jobAttachmentSettings") is not None:
        import capo_deadline.types.job_details_job_attachment_settings

        out["job_attachment_settings"] = (
            capo_deadline.types.job_details_job_attachment_settings.deserialize_json(
                data["jobAttachmentSettings"]
            )
        )
    if data.get("jobRunAsUser") is not None:
        import capo_deadline.types.job_run_as_user

        out["job_run_as_user"] = capo_deadline.types.job_run_as_user.deserialize_json(
            data["jobRunAsUser"]
        )
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        out["log_group_name"] = ""
    if data.get("queueRoleArn") is not None:
        out["queue_role_arn"] = data["queueRoleArn"]
    if data.get("parameters") is not None:
        import capo_deadline.types.job_parameters

        out["parameters"] = capo_deadline.types.job_parameters.deserialize_json(
            data["parameters"]
        )
    if data.get("schemaVersion") is not None:
        out["schema_version"] = data["schemaVersion"]
    else:
        out["schema_version"] = ""
    if data.get("extensions") is not None:
        import capo_deadline.types.openjd_extension_name_list

        out["extensions"] = (
            capo_deadline.types.openjd_extension_name_list.deserialize_json(
                data["extensions"]
            )
        )
    if data.get("pathMappingRules") is not None:
        import capo_deadline.types.path_mapping_rules

        out["path_mapping_rules"] = (
            capo_deadline.types.path_mapping_rules.deserialize_json(
                data["pathMappingRules"]
            )
        )
    return out


def redact_sensitive(value: JobDetailsEntity) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    if "path_mapping_rules" in value:
        import capo_deadline.types.path_mapping_rules

        out["path_mapping_rules"] = (
            capo_deadline.types.path_mapping_rules.redact_sensitive(
                value["path_mapping_rules"]
            )
        )
    return out
