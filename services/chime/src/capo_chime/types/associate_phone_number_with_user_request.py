"""Generated from Smithy shape ``com.amazonaws.chime#AssociatePhoneNumberWithUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime.types.e164_phone_number
    import capo_chime.types.string


class AssociatePhoneNumberWithUserRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.string.String"
    """<p>The Amazon Chime account ID.</p>"""
    user_id: "capo_chime.types.string.String"
    """<p>The user ID.</p>"""
    e164_phone_number: "capo_chime.types.e164_phone_number.E164PhoneNumber"
    """<p>The phone number, in E.164 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePhoneNumberWithUserRequest) -> dict:
    out: dict = {}
    out["E164PhoneNumber"] = value["e164_phone_number"]
    return out


def deserialize_json(data: dict) -> AssociatePhoneNumberWithUserRequest:
    out: AssociatePhoneNumberWithUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("E164PhoneNumber") is not None:
        out["e164_phone_number"] = data["E164PhoneNumber"]
    else:
        raise DeserializationError(
            "AssociatePhoneNumberWithUserRequest.e164_phone_number required"
        )
    return out


def redact_sensitive(value: AssociatePhoneNumberWithUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "e164_phone_number" in value:
        out["e164_phone_number"] = "*** Sensitive Data Redacted ***"
    return out
