"""Generated from Smithy shape ``com.amazonaws.deadline#CreateQueueEnvironmentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.environment_template
    import capo_deadline.types.environment_template_type
    import capo_deadline.types.farm_id
    import capo_deadline.types.priority
    import capo_deadline.types.queue_id


class CreateQueueEnvironmentRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm to connect to the environment."""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """The queue ID to connect the queue and environment."""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """The unique token which the server uses to recognize retries of the same request."""
    priority: "capo_deadline.types.priority.Priority"
    """Sets the priority of the environments in the queue from 0 to 10,000, where 0 is the highest priority (activated first and deactivated last). If two environments share the same priority value, the environment created first takes higher priority."""
    template_type: (
        "capo_deadline.types.environment_template_type.EnvironmentTemplateType"
    )
    """The template's file type, <code>JSON</code> or <code>YAML</code>."""
    template: "capo_deadline.types.environment_template.EnvironmentTemplate"
    """The environment template to use in the queue."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueEnvironmentRequest) -> dict:
    out: dict = {}
    out["priority"] = value["priority"]
    import capo_deadline.types.environment_template_type

    out["templateType"] = capo_deadline.types.environment_template_type.serialize_json(
        value["template_type"]
    )
    out["template"] = value["template"]
    return out


def deserialize_json(data: dict) -> CreateQueueEnvironmentRequest:
    out: CreateQueueEnvironmentRequest = {}  # type: ignore[typeddict-item]
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
    return out


def redact_sensitive(value: CreateQueueEnvironmentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "template" in value:
        out["template"] = "*** Sensitive Data Redacted ***"
    return out
