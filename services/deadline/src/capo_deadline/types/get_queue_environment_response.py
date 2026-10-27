"""Generated from Smithy shape ``com.amazonaws.deadline#GetQueueEnvironmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.created_at
    import capo_deadline.types.created_by
    import capo_deadline.types.environment_name
    import capo_deadline.types.environment_template
    import capo_deadline.types.environment_template_type
    import capo_deadline.types.priority
    import capo_deadline.types.queue_environment_id
    import capo_deadline.types.updated_at
    import capo_deadline.types.updated_by


class GetQueueEnvironmentResponse(TypedDict, closed=True):
    queue_environment_id: "capo_deadline.types.queue_environment_id.QueueEnvironmentId"
    """The queue environment ID."""
    name: "capo_deadline.types.environment_name.EnvironmentName"
    """The name of the queue environment."""
    priority: "capo_deadline.types.priority.Priority"
    """The priority of the queue environment."""
    template_type: (
        "capo_deadline.types.environment_template_type.EnvironmentTemplateType"
    )
    """The type of template for the queue environment."""
    template: "capo_deadline.types.environment_template.EnvironmentTemplate"
    """The template for the queue environment."""
    created_at: "capo_deadline.types.created_at.CreatedAt"
    """The date and time the resource was created."""
    created_by: "capo_deadline.types.created_by.CreatedBy"
    """The user or system that created this resource.&gt;"""
    updated_at: NotRequired["capo_deadline.types.updated_at.UpdatedAt"]
    """The date and time the resource was updated."""
    updated_by: NotRequired["capo_deadline.types.updated_by.UpdatedBy"]
    """The user or system that updated this resource."""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueEnvironmentResponse) -> dict:
    out: dict = {}
    out["queueEnvironmentId"] = value["queue_environment_id"]
    out["name"] = value["name"]
    out["priority"] = value["priority"]
    import capo_deadline.types.environment_template_type

    out["templateType"] = capo_deadline.types.environment_template_type.serialize_json(
        value["template_type"]
    )
    out["template"] = value["template"]
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
    return out


def deserialize_json(data: dict) -> GetQueueEnvironmentResponse:
    out: GetQueueEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("queueEnvironmentId") is not None:
        out["queue_environment_id"] = data["queueEnvironmentId"]
    else:
        out["queue_environment_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        out["priority"] = 0
    if data.get("templateType") is not None:
        import capo_deadline.types.environment_template_type

        out["template_type"] = (
            capo_deadline.types.environment_template_type.deserialize_json(
                data["templateType"]
            )
        )
    else:
        import typing

        out["template_type"] = typing.cast(
            "capo_deadline.types.environment_template_type.EnvironmentTemplateType", ""
        )
    if data.get("template") is not None:
        out["template"] = data["template"]
    else:
        out["template"] = ""
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
    return out


def redact_sensitive(value: GetQueueEnvironmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "template" in value:
        out["template"] = "*** Sensitive Data Redacted ***"
    return out
