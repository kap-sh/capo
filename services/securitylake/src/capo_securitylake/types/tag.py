"""Generated from Smithy shape ``com.amazonaws.securitylake#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.tag_key
    import capo_securitylake.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_securitylake.types.tag_key.TagKey"
    """<p>The name of the tag. This is a general label that acts as a category for a more specific tag value (<code>value</code>).</p>"""
    value: "capo_securitylake.types.tag_value.TagValue"
    """<p>The value that’s associated with the specified tag key (<code>key</code>). This value acts as a descriptor for the tag key. A tag value cannot be null, but it can be an empty string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
