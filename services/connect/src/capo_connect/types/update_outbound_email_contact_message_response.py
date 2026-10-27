"""Generated from Smithy shape ``com.amazonaws.connect#UpdateOutboundEmailContactMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_id


class UpdateOutboundEmailContactMessageResponse(TypedDict, closed=True):
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOutboundEmailContactMessageResponse) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    return out


def deserialize_json(data: dict) -> UpdateOutboundEmailContactMessageResponse:
    out: UpdateOutboundEmailContactMessageResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        out["contact_id"] = ""
    return out
