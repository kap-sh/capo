"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.email_address_id


class EmailAddressConfig(TypedDict, closed=True):
    email_address_id: "capo_connect.types.email_address_id.EmailAddressId"
    """<p>The identifier of the email address that should be associated with the queue. This email address must already exist in the Connect Customer instance and will be used to route incoming email contacts to the specified queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressConfig) -> dict:
    out: dict = {}
    out["EmailAddressId"] = value["email_address_id"]
    return out


def deserialize_json(data: dict) -> EmailAddressConfig:
    out: EmailAddressConfig = {}  # type: ignore[typeddict-item]
    if data.get("EmailAddressId") is not None:
        out["email_address_id"] = data["EmailAddressId"]
    else:
        out["email_address_id"] = ""
    return out
