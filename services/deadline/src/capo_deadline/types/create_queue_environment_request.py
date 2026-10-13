"""Generated from Smithy shape ``com.amazonaws.deadline#CreateQueueEnvironmentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.environment_template
    import capo_deadline.types.environment_template_type
    import capo_deadline.types.farm_id
    import capo_deadline.types.priority
    import capo_deadline.types.queue_id


class CreateQueueEnvironmentRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to connect to the environment.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID to connect the queue and environment.</p>"""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    priority: "capo_deadline.types.priority.Priority"
    """<p>Sets the priority of the environments in the queue from 0 to 10,000, where 0 is the highest priority (activated first and deactivated last). If two environments share the same priority value, the environment created first takes higher priority.</p>"""
    template_type: (
        "capo_deadline.types.environment_template_type.EnvironmentTemplateType"
    )
    """<p>The template's file type, <code>JSON</code> or <code>YAML</code>.</p>"""
    template: "capo_deadline.types.environment_template.EnvironmentTemplate"
    """<p>The environment template to use in the queue.</p>"""


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
        raise DeserializationError("CreateQueueEnvironmentRequest.priority required")
    if data.get("templateType") is not None:
        import capo_deadline.types.environment_template_type

        out["template_type"] = (
            capo_deadline.types.environment_template_type.deserialize_json(
                data["templateType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateQueueEnvironmentRequest.template_type required"
        )
    if data.get("template") is not None:
        out["template"] = data["template"]
    else:
        raise DeserializationError("CreateQueueEnvironmentRequest.template required")
    return out


def redact_sensitive(value: CreateQueueEnvironmentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "template" in value:
        out["template"] = "*** Sensitive Data Redacted ***"
    return out
