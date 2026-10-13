"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#PutKeyRequestListItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cloudfront_keyvaluestore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.key
    import capo_cloudfront_keyvaluestore.types.value


class PutKeyRequestListItem(TypedDict, closed=True):
    key: "capo_cloudfront_keyvaluestore.types.key.Key"
    """<p>The key of the key value pair list item to put.</p>"""
    value: "capo_cloudfront_keyvaluestore.types.value.Value"
    """<p>The value for the key value pair to put.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutKeyRequestListItem) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> PutKeyRequestListItem:
    out: PutKeyRequestListItem = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("PutKeyRequestListItem.key required")
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("PutKeyRequestListItem.value required")
    return out


def redact_sensitive(value: PutKeyRequestListItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
