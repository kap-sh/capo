"""Generated from Smithy shape ``com.amazonaws.swf#TagFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_swf.types.tag


class TagFilter(TypedDict, closed=True):
    tag: "capo_swf.types.tag.Tag"
    """<p> Specifies the tag that must be associated with the execution for it to meet the filter criteria.</p> <p>Tags may only contain unicode letters, digits, whitespace, or these symbols: <code>_ . : / = + - @</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagFilter) -> dict:
    out: dict = {}
    out["tag"] = value["tag"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if data.get("tag") is not None:
        out["tag"] = data["tag"]
    else:
        out["tag"] = ""
    return out
