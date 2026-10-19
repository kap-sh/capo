"""Generated from Smithy shape ``com.amazonaws.iot#UserProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.user_property_key
    import capo_iot.types.user_property_value


class UserProperty(TypedDict, closed=True):
    key: "capo_iot.types.user_property_key.UserPropertyKey"
    """<p>A key to be specified in <code>UserProperty</code>.</p>"""
    value: "capo_iot.types.user_property_value.UserPropertyValue"
    """<p>A value to be specified in <code>UserProperty</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserProperty) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> UserProperty:
    out: UserProperty = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
