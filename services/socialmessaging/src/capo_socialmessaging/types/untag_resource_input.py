"""Generated from Smithy shape ``com.amazonaws.socialmessaging#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.arn
    import capo_socialmessaging.types.string_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_socialmessaging.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>"""
    tag_keys: "capo_socialmessaging.types.string_list.StringList"
    """<p>The keys of the tags to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_socialmessaging.types.string_list

    out["tagKeys"] = capo_socialmessaging.types.string_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_socialmessaging.types.string_list

        out["tag_keys"] = capo_socialmessaging.types.string_list.deserialize_json(
            data["tagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
