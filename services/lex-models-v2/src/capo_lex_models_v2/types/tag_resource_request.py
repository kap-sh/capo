"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.amazon_resource_name
    import capo_lex_models_v2.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.</p>"""
    tags: "capo_lex_models_v2.types.tag_map.TagMap"
    """<p>A list of tag keys to add to the resource. If a tag key already exists, the existing value is replaced with the new value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.tag_map

    out["tags"] = capo_lex_models_v2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_lex_models_v2.types.tag_map

        out["tags"] = capo_lex_models_v2.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    return out
