"""Generated from Smithy shape ``com.amazonaws.neptunegraph#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptune_graph.types.arn
    import capo_neptune_graph.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_neptune_graph.types.arn.Arn"
    """<p>ARN of the resource for which tags need to be added.</p>"""
    tags: "capo_neptune_graph.types.tag_map.TagMap"
    r"""<p>The tags to be assigned to the Neptune Analytics resource.</p> <p>The tags are metadata that are specified as a list of key-value pairs:</p> <p> <b>Key</b> (string) – A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length. It can't be prefixed with <code>aws:</code> and can only contain the set of Unicode characters specified by this Java regular expression: <code>"^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$")</code>.</p> <p> <b>Value</b> (string) – A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length. It can't be prefixed with <code>aws:</code> and can only contain the set of Unicode characters specified by this Java regular expression: <code>"^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$")</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_neptune_graph.types.tag_map

    out["tags"] = capo_neptune_graph.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_neptune_graph.types.tag_map

        out["tags"] = capo_neptune_graph.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
