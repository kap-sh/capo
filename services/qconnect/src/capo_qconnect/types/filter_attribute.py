"""Generated from Smithy shape ``com.amazonaws.qconnect#FilterAttribute``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.filter_attribute_key
    import capo_qconnect.types.json_document


class FilterAttribute(TypedDict, closed=True):
    key: "capo_qconnect.types.filter_attribute_key.FilterAttributeKey"
    """<p>The key of the filter attribute.</p>"""
    value: "capo_qconnect.types.json_document.JSONDocument"
    """<p>The value of the filter attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterAttribute) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> FilterAttribute:
    out: FilterAttribute = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("FilterAttribute.key required")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError("FilterAttribute.value required")
    return out


def redact_sensitive(value: FilterAttribute) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
