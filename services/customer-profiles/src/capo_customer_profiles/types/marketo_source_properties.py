"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MarketoSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.object


class MarketoSourceProperties(TypedDict, closed=True):
    object: "capo_customer_profiles.types.object.Object"
    """<p>The object specified in the Marketo flow source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MarketoSourceProperties) -> dict:
    out: dict = {}
    out["Object"] = value["object"]
    return out


def deserialize_json(data: dict) -> MarketoSourceProperties:
    out: MarketoSourceProperties = {}  # type: ignore[typeddict-item]
    if data.get("Object") is not None:
        out["object"] = data["Object"]
    else:
        out["object"] = ""
    return out
