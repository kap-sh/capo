"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetServiceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.registered_service
    import capo_devops_agent.types.tags


class GetServiceOutput(TypedDict, closed=True):
    service: "capo_devops_agent.types.registered_service.RegisteredService"
    tags: NotRequired["capo_devops_agent.types.tags.Tags"]
    """<p>Tags associated with the Service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceOutput) -> dict:
    out: dict = {}
    import capo_devops_agent.types.registered_service

    out["service"] = capo_devops_agent.types.registered_service.serialize_json(
        value["service"]
    )
    if "tags" in value:
        import capo_devops_agent.types.tags

        out["tags"] = capo_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetServiceOutput:
    out: GetServiceOutput = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        import capo_devops_agent.types.registered_service

        out["service"] = capo_devops_agent.types.registered_service.deserialize_json(
            data["service"]
        )
    else:
        raise DeserializationError("GetServiceOutput.service required")
    if data.get("tags") is not None:
        import capo_devops_agent.types.tags

        out["tags"] = capo_devops_agent.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: GetServiceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service" in value:
        import capo_devops_agent.types.registered_service

        out["service"] = capo_devops_agent.types.registered_service.redact_sensitive(
            value["service"]
        )
    return out
