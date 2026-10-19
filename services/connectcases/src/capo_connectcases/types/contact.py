"""Generated from Smithy shape ``com.amazonaws.connectcases#Contact``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.contact_arn


class Contact(TypedDict, closed=True):
    contact_arn: "capo_connectcases.types.contact_arn.ContactArn"
    """<p>A unique identifier of a contact in Amazon Connect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Contact) -> dict:
    out: dict = {}
    out["contactArn"] = value["contact_arn"]
    return out


def deserialize_json(data: dict) -> Contact:
    out: Contact = {}  # type: ignore[typeddict-item]
    if data.get("contactArn") is not None:
        out["contact_arn"] = data["contactArn"]
    else:
        out["contact_arn"] = ""
    return out
