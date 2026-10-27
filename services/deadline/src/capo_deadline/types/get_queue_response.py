"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.allowed_storage_profile_ids
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.default_queue_budget_action
    import capo_deadline.types.description
    import capo_deadline.types.farm_id
    import capo_deadline.types.iam_role_arn
    import capo_deadline.types.job_attachment_settings
    import capo_deadline.types.job_run_as_user
    import capo_deadline.types.queue_blocked_reason
    import capo_deadline.types.queue_id
    import capo_deadline.types.queue_status
    import capo_deadline.types.required_file_system_location_names
    import capo_deadline.types.resource_name
    import capo_deadline.types.scheduling_configuration
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class GetQueueResponse(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID for the queue."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID."""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the queue.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    status: "capo_deadline.types.queue_status.QueueStatus"
    """<p>The status of the queue.</p> <ul> <li> <p> <code>ACTIVE</code>–The queue is active.</p> </li> <li> <p> <code>SCHEDULING</code>–The queue is scheduling.</p> </li> <li> <p> <code>SCHEDULING_BLOCKED</code>–The queue scheduling is blocked. See the provided reason.</p> </li> </ul>"""
    default_budget_action: (
        "capo_deadline.types.default_queue_budget_action.DefaultQueueBudgetAction"
    )
    """The default action taken on a queue if a budget wasn't configured."""
    blocked_reason: NotRequired[
        "capo_deadline.types.queue_blocked_reason.QueueBlockedReason"
    ]
    """The reason the queue was blocked."""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """The date and time the resource was created."""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """The user or system that created this resource."""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """The date and time the resource was updated."""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """The user or system that updated this resource."""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The description of the queue.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    job_attachment_settings: NotRequired[
        "capo_deadline.types.job_attachment_settings.JobAttachmentSettings"
    ]
    """The job attachment settings for the queue."""
    role_arn: NotRequired["capo_deadline.types.iam_role_arn.IamRoleArn"]
    """The IAM role ARN."""
    required_file_system_location_names: NotRequired[
        "capo_deadline.types.required_file_system_location_names.RequiredFileSystemLocationNames"
    ]
    """A list of the required file system location names in the queue."""
    allowed_storage_profile_ids: NotRequired[
        "capo_deadline.types.allowed_storage_profile_ids.AllowedStorageProfileIds"
    ]
    """The storage profile IDs for the queue."""
    job_run_as_user: NotRequired["capo_deadline.types.job_run_as_user.JobRunAsUser"]
    """The jobs in the queue ran as this specified POSIX user."""
    scheduling_configuration: NotRequired[
        "capo_deadline.types.scheduling_configuration.SchedulingConfiguration"
    ]
    """The scheduling configuration for the queue. This configuration determines how workers are assigned to jobs in the queue."""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueResponse) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["queueId"] = value["queue_id"]
    out["displayName"] = value["display_name"]
    import capo_deadline.types.queue_status

    out["status"] = capo_deadline.types.queue_status.serialize_json(value["status"])
    import capo_deadline.types.default_queue_budget_action

    out["defaultBudgetAction"] = (
        capo_deadline.types.default_queue_budget_action.serialize_json(
            value["default_budget_action"]
        )
    )
    if "blocked_reason" in value:
        import capo_deadline.types.queue_blocked_reason

        out["blockedReason"] = capo_deadline.types.queue_blocked_reason.serialize_json(
            value["blocked_reason"]
        )
    import capo_deadline.types.created_at

    out["createdAt"] = capo_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import capo_deadline.types.updated_at

        out["updatedAt"] = capo_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "description" in value:
        out["description"] = value["description"]
    if "job_attachment_settings" in value:
        import capo_deadline.types.job_attachment_settings

        out["jobAttachmentSettings"] = (
            capo_deadline.types.job_attachment_settings.serialize_json(
                value["job_attachment_settings"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
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
    if "job_run_as_user" in value:
        import capo_deadline.types.job_run_as_user

        out["jobRunAsUser"] = capo_deadline.types.job_run_as_user.serialize_json(
            value["job_run_as_user"]
        )
    if "scheduling_configuration" in value:
        import capo_deadline.types.scheduling_configuration

        out["schedulingConfiguration"] = (
            capo_deadline.types.scheduling_configuration.serialize_json(
                value["scheduling_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetQueueResponse:
    out: GetQueueResponse = {}  # type: ignore[typeddict-item]
    if data.get("farmId") is not None:
        out["farm_id"] = data["farmId"]
    else:
        out["farm_id"] = ""
    if data.get("queueId") is not None:
        out["queue_id"] = data["queueId"]
    else:
        out["queue_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("status") is not None:
        import capo_deadline.types.queue_status

        out["status"] = capo_deadline.types.queue_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_deadline.types.queue_status.QueueStatus", "")
    if data.get("defaultBudgetAction") is not None:
        import capo_deadline.types.default_queue_budget_action

        out["default_budget_action"] = (
            capo_deadline.types.default_queue_budget_action.deserialize_json(
                data["defaultBudgetAction"]
            )
        )
    else:
        import typing

        out["default_budget_action"] = typing.cast(
            "capo_deadline.types.default_queue_budget_action.DefaultQueueBudgetAction",
            "",
        )
    if data.get("blockedReason") is not None:
        import capo_deadline.types.queue_blocked_reason

        out["blocked_reason"] = (
            capo_deadline.types.queue_blocked_reason.deserialize_json(
                data["blockedReason"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_deadline.types.created_at

        out["created_at"] = capo_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("updatedAt") is not None:
        import capo_deadline.types.updated_at

        out["updated_at"] = capo_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("jobAttachmentSettings") is not None:
        import capo_deadline.types.job_attachment_settings

        out["job_attachment_settings"] = (
            capo_deadline.types.job_attachment_settings.deserialize_json(
                data["jobAttachmentSettings"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
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
    if data.get("jobRunAsUser") is not None:
        import capo_deadline.types.job_run_as_user

        out["job_run_as_user"] = capo_deadline.types.job_run_as_user.deserialize_json(
            data["jobRunAsUser"]
        )
    if data.get("schedulingConfiguration") is not None:
        import capo_deadline.types.scheduling_configuration

        out["scheduling_configuration"] = (
            capo_deadline.types.scheduling_configuration.deserialize_json(
                data["schedulingConfiguration"]
            )
        )
    return out


def redact_sensitive(value: GetQueueResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
