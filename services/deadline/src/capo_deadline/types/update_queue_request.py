"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueRequest``."""

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
    import capo_deadline.types.queue_id
    import capo_deadline.types.required_file_system_location_names
    import capo_deadline.types.resource_name
    import capo_deadline.types.scheduling_configuration


class UpdateQueueRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID to update in the queue."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID to update."""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """The idempotency token to update in the queue."""
    display_name: NotRequired["capo_deadline.types.resource_name.ResourceName"]
    """<p>The display name of the queue to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The description of the queue to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    default_budget_action: NotRequired[
        "capo_deadline.types.default_queue_budget_action.DefaultQueueBudgetAction"
    ]
    """The default action to take for a queue update if a budget isn't configured."""
    job_attachment_settings: NotRequired[
        "capo_deadline.types.job_attachment_settings.JobAttachmentSettings"
    ]
    """The job attachment settings to update for the queue."""
    role_arn: NotRequired["capo_deadline.types.iam_role_arn.IamRoleArn"]
    """The IAM role ARN that's used to run jobs from this queue."""
    job_run_as_user: NotRequired["capo_deadline.types.job_run_as_user.JobRunAsUser"]
    """Update the jobs in the queue to run as a specified POSIX user."""
    required_file_system_location_names_to_add: NotRequired[
        "capo_deadline.types.required_file_system_location_names.RequiredFileSystemLocationNames"
    ]
    """The required file system location names to add to the queue."""
    required_file_system_location_names_to_remove: NotRequired[
        "capo_deadline.types.required_file_system_location_names.RequiredFileSystemLocationNames"
    ]
    """The required file system location names to remove from the queue."""
    allowed_storage_profile_ids_to_add: NotRequired[
        "capo_deadline.types.allowed_storage_profile_ids.AllowedStorageProfileIds"
    ]
    """The storage profile IDs to add."""
    allowed_storage_profile_ids_to_remove: NotRequired[
        "capo_deadline.types.allowed_storage_profile_ids.AllowedStorageProfileIds"
    ]
    """The storage profile ID to remove."""
    scheduling_configuration: NotRequired[
        "capo_deadline.types.scheduling_configuration.SchedulingConfiguration"
    ]
    """The scheduling configuration for the queue. This configuration determines how workers are assigned to jobs in the queue. When updating the scheduling configuration, the entire configuration is replaced. In-progress tasks run to completion before the new scheduling configuration takes effect."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
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
    if "required_file_system_location_names_to_add" in value:
        import capo_deadline.types.required_file_system_location_names

        out["requiredFileSystemLocationNamesToAdd"] = (
            capo_deadline.types.required_file_system_location_names.serialize_json(
                value["required_file_system_location_names_to_add"]
            )
        )
    if "required_file_system_location_names_to_remove" in value:
        import capo_deadline.types.required_file_system_location_names

        out["requiredFileSystemLocationNamesToRemove"] = (
            capo_deadline.types.required_file_system_location_names.serialize_json(
                value["required_file_system_location_names_to_remove"]
            )
        )
    if "allowed_storage_profile_ids_to_add" in value:
        import capo_deadline.types.allowed_storage_profile_ids

        out["allowedStorageProfileIdsToAdd"] = (
            capo_deadline.types.allowed_storage_profile_ids.serialize_json(
                value["allowed_storage_profile_ids_to_add"]
            )
        )
    if "allowed_storage_profile_ids_to_remove" in value:
        import capo_deadline.types.allowed_storage_profile_ids

        out["allowedStorageProfileIdsToRemove"] = (
            capo_deadline.types.allowed_storage_profile_ids.serialize_json(
                value["allowed_storage_profile_ids_to_remove"]
            )
        )
    if "scheduling_configuration" in value:
        import capo_deadline.types.scheduling_configuration

        out["schedulingConfiguration"] = (
            capo_deadline.types.scheduling_configuration.serialize_json(
                value["scheduling_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateQueueRequest:
    out: UpdateQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
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
    if data.get("requiredFileSystemLocationNamesToAdd") is not None:
        import capo_deadline.types.required_file_system_location_names

        out["required_file_system_location_names_to_add"] = (
            capo_deadline.types.required_file_system_location_names.deserialize_json(
                data["requiredFileSystemLocationNamesToAdd"]
            )
        )
    if data.get("requiredFileSystemLocationNamesToRemove") is not None:
        import capo_deadline.types.required_file_system_location_names

        out["required_file_system_location_names_to_remove"] = (
            capo_deadline.types.required_file_system_location_names.deserialize_json(
                data["requiredFileSystemLocationNamesToRemove"]
            )
        )
    if data.get("allowedStorageProfileIdsToAdd") is not None:
        import capo_deadline.types.allowed_storage_profile_ids

        out["allowed_storage_profile_ids_to_add"] = (
            capo_deadline.types.allowed_storage_profile_ids.deserialize_json(
                data["allowedStorageProfileIdsToAdd"]
            )
        )
    if data.get("allowedStorageProfileIdsToRemove") is not None:
        import capo_deadline.types.allowed_storage_profile_ids

        out["allowed_storage_profile_ids_to_remove"] = (
            capo_deadline.types.allowed_storage_profile_ids.deserialize_json(
                data["allowedStorageProfileIdsToRemove"]
            )
        )
    if data.get("schedulingConfiguration") is not None:
        import capo_deadline.types.scheduling_configuration

        out["scheduling_configuration"] = (
            capo_deadline.types.scheduling_configuration.deserialize_json(
                data["schedulingConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateQueueRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
