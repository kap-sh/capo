"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_name


class AttributeItem(TypedDict, closed=True):
    name: "capo_customer_profiles.types.attribute_name.attributeName"
    """<p>The name of an attribute defined in a profile object type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeItem) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AttributeItem:
    out: AttributeItem = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
