"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ZendeskSourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.object


class ZendeskSourceProperties(TypedDict, closed=True):
    object: "capo_customer_profiles.types.object.Object"
    """<p>The object specified in the Zendesk flow source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ZendeskSourceProperties) -> dict:
    out: dict = {}
    out["Object"] = value["object"]
    return out


def deserialize_json(data: dict) -> ZendeskSourceProperties:
    out: ZendeskSourceProperties = {}  # type: ignore[typeddict-item]
    if data.get("Object") is not None:
        out["object"] = data["Object"]
    else:
        out["object"] = ""
    return out
