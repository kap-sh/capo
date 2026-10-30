"""Generated from Smithy shape ``com.amazonaws.inspector2#AmiTagFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ami_tag_key
    import capo_inspector2.types.ami_tag_value


class AmiTagFilter(TypedDict, closed=True):
    key: "capo_inspector2.types.ami_tag_key.AmiTagKey"
    """<p>The tag key to match against an AMI's tags.</p>"""
    value: NotRequired["capo_inspector2.types.ami_tag_value.AmiTagValue"]
    """<p>The tag value to match against an AMI's tags. If omitted, the filter matches on the tag key alone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiTagFilter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AmiTagFilter:
    out: AmiTagFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
