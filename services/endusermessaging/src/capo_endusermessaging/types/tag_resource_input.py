"""Generated from Smithy shape ``com.amazonaws.endusermessaging#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.amazon_resource_name
    import capo_endusermessaging.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_endusermessaging.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "capo_endusermessaging.types.tag_list.TagList"
    """<p>An array of key and value pair tags that are associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.tag_list

    out["tags"] = capo_endusermessaging.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_endusermessaging.types.tag_list

        out["tags"] = capo_endusermessaging.types.tag_list.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
