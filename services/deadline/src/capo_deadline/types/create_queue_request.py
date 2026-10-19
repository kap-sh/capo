"""Generated from Smithy shape ``com.amazonaws.deadline#CreateQueueRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.allowed_storage_profile_ids
    import capo_deadline.types.client_token
    import capo_deadline.types.default_queue_budget_action
    import capo_deadline.types.description
    import capo_deadline.types.farm_id
    import capo_deadline.types.iam_role_arn
    import capo_deadline.types.job_attachment_settings
    import capo_deadline.types.job_run_as_user
    import capo_deadline.types.required_file_system_location_names
    import capo_deadline.types.resource_name
    import capo_deadline.types.scheduling_configuration
    import capo_deadline.types.tags


class CreateQueueRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to connect to the queue.</p>"""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the queue.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The description of the queue.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    default_budget_action: NotRequired[
        "capo_deadline.types.default_queue_budget_action.DefaultQueueBudgetAction"
    ]
    """<p>The default action to take on a queue if a budget isn't configured.</p>"""
    job_attachment_settings: NotRequired[
        "capo_deadline.types.job_attachment_settings.JobAttachmentSettings"
    ]
    """<p>The job attachment settings for the queue. These are the Amazon S3 bucket name and the Amazon S3 prefix.</p>"""
    role_arn: NotRequired["capo_deadline.types.iam_role_arn.IamRoleArn"]
    """<p>The IAM role ARN that workers will use while running jobs for this queue.</p>"""
    job_run_as_user: NotRequired["capo_deadline.types.job_run_as_user.JobRunAsUser"]
    """<p>The jobs in the queue run as the specified POSIX user.</p>"""
    required_file_system_location_names: NotRequired[
        "capo_deadline.types.required_file_system_location_names.RequiredFileSystemLocationNames"
    ]
    """<p>The file system location name to include in the queue.</p>"""
    allowed_storage_profile_ids: NotRequired[
        "capo_deadline.types.allowed_storage_profile_ids.AllowedStorageProfileIds"
    ]
    """<p>The storage profile IDs to include in the queue.</p>"""
    tags: NotRequired["capo_deadline.types.tags.Tags"]
    """<p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>"""
    scheduling_configuration: NotRequired[
        "capo_deadline.types.scheduling_configuration.SchedulingConfiguration"
    ]
    """<p>The scheduling configuration for the queue. This configuration determines how workers are assigned to jobs in the queue.</p> <p>If not specified, the queue defaults to the <code>priorityFifo</code> scheduling configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "default_budget_action" in value:
        import capo_deadline.types.default_queue_budget_action

        out["defaultBudgetAction"] = (
            capo_deadline.types.default_queue_budget_action.serialize_json(
                value["default_budget_action"]
            )
        )
    if "job_attachment_settings" in value:
        import capo_deadline.types.job_attachment_settings

        out["jobAttachmentSettings"] = (
            capo_deadline.types.job_attachment_settings.serialize_json(
                value["job_attachment_settings"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "job_run_as_user" in value:
        import capo_deadline.types.job_run_as_user

        out["jobRunAsUser"] = capo_deadline.types.job_run_as_user.serialize_json(
            value["job_run_as_user"]
        )
    if "required_file_system_location_names" in value:
        import capo_deadline.types.required_file_system_location_names

        out["requiredFileSystemLocationNames"] = (
            capo_deadline.types.required_file_system_location_names.serialize_json(
                value["required_file_system_location_names"]
            )
        )
    if "allowed_storage_profile_ids" in value:
        import capo_deadline.types.allowed_storage_profile_ids

        out["allowedStorageProfileIds"] = (
            capo_deadline.types.allowed_storage_profile_ids.serialize_json(
                value["allowed_storage_profile_ids"]
            )
        )
    if "tags" in value:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.serialize_json(value["tags"])
    if "scheduling_configuration" in value:
        import capo_deadline.types.scheduling_configuration

        out["schedulingConfiguration"] = (
            capo_deadline.types.scheduling_configuration.serialize_json(
                value["scheduling_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateQueueRequest:
    out: CreateQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("defaultBudgetAction") is not None:
        import capo_deadline.types.default_queue_budget_action

        out["default_budget_action"] = (
            capo_deadline.types.default_queue_budget_action.deserialize_json(
                data["defaultBudgetAction"]
            )
        )
    if data.get("jobAttachmentSettings") is not None:
        import capo_deadline.types.job_attachment_settings

        out["job_attachment_settings"] = (
            capo_deadline.types.job_attachment_settings.deserialize_json(
                data["jobAttachmentSettings"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("jobRunAsUser") is not None:
        import capo_deadline.types.job_run_as_user

        out["job_run_as_user"] = capo_deadline.types.job_run_as_user.deserialize_json(
            data["jobRunAsUser"]
        )
    if data.get("requiredFileSystemLocationNames") is not None:
        import capo_deadline.types.required_file_system_location_names

        out["required_file_system_location_names"] = (
            capo_deadline.types.required_file_system_location_names.deserialize_json(
                data["requiredFileSystemLocationNames"]
            )
        )
    if data.get("allowedStorageProfileIds") is not None:
        import capo_deadline.types.allowed_storage_profile_ids

        out["allowed_storage_profile_ids"] = (
            capo_deadline.types.allowed_storage_profile_ids.deserialize_json(
                data["allowedStorageProfileIds"]
            )
        )
    if data.get("tags") is not None:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.deserialize_json(data["tags"])
    if data.get("schedulingConfiguration") is not None:
        import capo_deadline.types.scheduling_configuration

        out["scheduling_configuration"] = (
            capo_deadline.types.scheduling_configuration.deserialize_json(
                data["schedulingConfiguration"]
            )
        )
    return out


def redact_sensitive(value: CreateQueueRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
