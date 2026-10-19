"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteDomainLayoutResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.message


class DeleteDomainLayoutResponse(TypedDict, closed=True):
    message: "capo_customer_profiles.types.message.message"
    """<p>A message that indicates the delete request is done.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainLayoutResponse) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteDomainLayoutResponse:
    out: DeleteDomainLayoutResponse = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
