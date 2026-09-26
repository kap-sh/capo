"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.resource_tags_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired[
        "capo_agent_registry_control.types.resource_tags_map.ResourceTagsMap"
    ]
    """<p>The tags currently associated with the resource, as a map of tag keys to tag values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_agent_registry_control.types.resource_tags_map

        out["tags"] = (
            capo_agent_registry_control.types.resource_tags_map.serialize_json(
                value["tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_agent_registry_control.types.resource_tags_map

        out["tags"] = (
            capo_agent_registry_control.types.resource_tags_map.deserialize_json(
                data["tags"]
            )
        )
    return out
