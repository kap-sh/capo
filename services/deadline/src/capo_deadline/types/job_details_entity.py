"""Generated from Smithy shape ``com.amazonaws.deadline#JobDetailsEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

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
    """<p>The job ID.</p>"""
    job_attachment_settings: NotRequired[
        "capo_deadline.types.job_details_job_attachment_settings.JobDetailsJobAttachmentSettings"
    ]
    """<p>The job attachment settings.</p>"""
    job_run_as_user: NotRequired["capo_deadline.types.job_run_as_user.JobRunAsUser"]
    """<p>The user name and group that the job uses when run.</p>"""
    log_group_name: "capo_deadline.types.string.String"
    """<p>The log group name.</p>"""
    queue_role_arn: NotRequired["capo_deadline.types.iam_role_arn.IamRoleArn"]
    """<p>The queue role ARN.</p>"""
    parameters: NotRequired["capo_deadline.types.job_parameters.JobParameters"]
    """<p>The parameters.</p>"""
    schema_version: "capo_deadline.types.string.String"
    """<p>The schema version.</p>"""
    extensions: NotRequired[
        "capo_deadline.types.openjd_extension_name_list.OpenjdExtensionNameList"
    ]
    """<p>The Open Job Description extensions that the job template uses. This value is used by the worker agent.</p>"""
    path_mapping_rules: NotRequired[
        "capo_deadline.types.path_mapping_rules.PathMappingRules"
    ]
    """<p>The path mapping rules.</p>"""


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
        raise DeserializationError("JobDetailsEntity.job_id required")
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
        raise DeserializationError("JobDetailsEntity.log_group_name required")
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
        raise DeserializationError("JobDetailsEntity.schema_version required")
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
