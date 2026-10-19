"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.resource_arn
    import capo_migrationhuborchestrator.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_migrationhuborchestrator.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to which you want to add tags.</p>"""
    tags: "capo_migrationhuborchestrator.types.tag_map.TagMap"
    """<p>A collection of labels, in the form of key:value pairs, that apply to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_migrationhuborchestrator.types.tag_map

    out["tags"] = capo_migrationhuborchestrator.types.tag_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_migrationhuborchestrator.types.tag_map

        out["tags"] = capo_migrationhuborchestrator.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
