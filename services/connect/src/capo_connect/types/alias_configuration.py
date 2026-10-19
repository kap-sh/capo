"""Generated from Smithy shape ``com.amazonaws.connect#AliasConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.email_address_id


class AliasConfiguration(TypedDict, closed=True):
    email_address_id: "capo_connect.types.email_address_id.EmailAddressId"
    """<p>The email address ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AliasConfiguration) -> dict:
    out: dict = {}
    out["EmailAddressId"] = value["email_address_id"]
    return out


def deserialize_json(data: dict) -> AliasConfiguration:
    out: AliasConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EmailAddressId") is not None:
        out["email_address_id"] = data["EmailAddressId"]
    else:
        out["email_address_id"] = ""
    return out
