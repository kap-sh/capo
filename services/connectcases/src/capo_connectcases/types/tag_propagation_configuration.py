"""Generated from Smithy shape ``com.amazonaws.connectcases#TagPropagationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.mutable_tags
    import capo_connectcases.types.tag_propagation_resource_type


class TagPropagationConfiguration(TypedDict, closed=True):
    resource_type: "capo_connectcases.types.tag_propagation_resource_type.TagPropagationResourceType"
    """<p>Supported resource types for tag propagation. Determines which resources will receive automatically propagated tags.</p>"""
    tag_map: "capo_connectcases.types.mutable_tags.MutableTags"
    """<p>The tags that will be applied to the created resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagPropagationConfiguration) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    import capo_connectcases.types.mutable_tags

    out["tagMap"] = capo_connectcases.types.mutable_tags.serialize_json(
        value["tag_map"]
    )
    return out


def deserialize_json(data: dict) -> TagPropagationConfiguration:
    out: TagPropagationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("tagMap") is not None:
        import capo_connectcases.types.mutable_tags

        out["tag_map"] = capo_connectcases.types.mutable_tags.deserialize_json(
            data["tagMap"]
        )
    else:
        out["tag_map"] = {}
    return out
