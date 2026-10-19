"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.amazon_resource_name
    import capo_lex_model_building_service.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_lex_model_building_service.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.</p>"""
    tags: "capo_lex_model_building_service.types.tag_list.TagList"
    """<p>A list of tag keys to add to the resource. If a tag key already exists, the existing value is replaced with the new value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_lex_model_building_service.types.tag_list

    out["tags"] = capo_lex_model_building_service.types.tag_list.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_lex_model_building_service.types.tag_list

        out["tags"] = capo_lex_model_building_service.types.tag_list.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = []
    return out
