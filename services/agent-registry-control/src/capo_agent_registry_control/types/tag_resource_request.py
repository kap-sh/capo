"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.resource_arn
    import capo_agent_registry_control.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_agent_registry_control.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to tag. Supported resources include registries and registry records.</p>"""
    tags: "capo_agent_registry_control.types.tags_map.TagsMap"
    """<p>The tags to apply to the resource, as a map of tag keys to tag values. Tag keys must be unique within the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.tags_map

    out["tags"] = capo_agent_registry_control.types.tags_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_agent_registry_control.types.tags_map

        out["tags"] = capo_agent_registry_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
