"""Generated from Smithy shape ``com.amazonaws.codeartifact#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.arn
    import capo_codeartifact.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_codeartifact.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from.</p>"""
    tag_keys: "capo_codeartifact.types.tag_key_list.TagKeyList"
    """<p>The tag key for each tag that you want to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    import capo_codeartifact.types.tag_key_list

    out["tagKeys"] = capo_codeartifact.types.tag_key_list.serialize_json(
        value["tag_keys"]
    )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tagKeys") is not None:
        import capo_codeartifact.types.tag_key_list

        out["tag_keys"] = capo_codeartifact.types.tag_key_list.deserialize_json(
            data["tagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
