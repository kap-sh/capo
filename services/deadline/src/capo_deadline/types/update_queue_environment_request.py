"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateQueueEnvironmentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.environment_template
    import capo_deadline.types.environment_template_type
    import capo_deadline.types.farm_id
    import capo_deadline.types.priority
    import capo_deadline.types.queue_environment_id
    import capo_deadline.types.queue_id


class UpdateQueueEnvironmentRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the queue environment to update.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the queue environment to update.</p>"""
    queue_environment_id: "capo_deadline.types.queue_environment_id.QueueEnvironmentId"
    """<p>The queue environment ID to update.</p>"""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    priority: NotRequired["capo_deadline.types.priority.Priority"]
    """<p>The priority to update.</p>"""
    template_type: NotRequired[
        "capo_deadline.types.environment_template_type.EnvironmentTemplateType"
    ]
    """<p>The template type to update.</p>"""
    template: NotRequired[
        "capo_deadline.types.environment_template.EnvironmentTemplate"
    ]
    """<p>The template to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueEnvironmentRequest) -> dict:
    out: dict = {}
    if "priority" in value:
        out["priority"] = value["priority"]
    if "template_type" in value:
        import capo_deadline.types.environment_template_type

        out["templateType"] = (
            capo_deadline.types.environment_template_type.serialize_json(
                value["template_type"]
            )
        )
    if "template" in value:
        out["template"] = value["template"]
    return out


def deserialize_json(data: dict) -> UpdateQueueEnvironmentRequest:
    out: UpdateQueueEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("templateType") is not None:
        import capo_deadline.types.environment_template_type

        out["template_type"] = (
            capo_deadline.types.environment_template_type.deserialize_json(
                data["templateType"]
            )
        )
    if data.get("template") is not None:
        out["template"] = data["template"]
    return out


def redact_sensitive(value: UpdateQueueEnvironmentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "template" in value:
        out["template"] = "*** Sensitive Data Redacted ***"
    return out
