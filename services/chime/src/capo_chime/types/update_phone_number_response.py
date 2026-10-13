"""Generated from Smithy shape ``com.amazonaws.chime#UpdatePhoneNumberResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.phone_number


class UpdatePhoneNumberResponse(TypedDict, closed=True):
    phone_number: NotRequired["capo_chime.types.phone_number.PhoneNumber"]
    """<p>The updated phone number details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePhoneNumberResponse) -> dict:
    out: dict = {}
    if "phone_number" in value:
        import capo_chime.types.phone_number

        out["PhoneNumber"] = capo_chime.types.phone_number.serialize_json(
            value["phone_number"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePhoneNumberResponse:
    out: UpdatePhoneNumberResponse = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumber") is not None:
        import capo_chime.types.phone_number

        out["phone_number"] = capo_chime.types.phone_number.deserialize_json(
            data["PhoneNumber"]
        )
    return out


def redact_sensitive(value: UpdatePhoneNumberResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number" in value:
        import capo_chime.types.phone_number

        out["phone_number"] = capo_chime.types.phone_number.redact_sensitive(
            value["phone_number"]
        )
    return out
