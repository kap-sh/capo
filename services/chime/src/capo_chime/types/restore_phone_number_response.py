"""Generated from Smithy shape ``com.amazonaws.chime#RestorePhoneNumberResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.phone_number


class RestorePhoneNumberResponse(TypedDict, closed=True):
    phone_number: NotRequired["capo_chime.types.phone_number.PhoneNumber"]
    """<p>The phone number details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestorePhoneNumberResponse) -> dict:
    out: dict = {}
    if "phone_number" in value:
        import capo_chime.types.phone_number

        out["PhoneNumber"] = capo_chime.types.phone_number.serialize_json(
            value["phone_number"]
        )
    return out


def deserialize_json(data: dict) -> RestorePhoneNumberResponse:
    out: RestorePhoneNumberResponse = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumber") is not None:
        import capo_chime.types.phone_number

        out["phone_number"] = capo_chime.types.phone_number.deserialize_json(
            data["PhoneNumber"]
        )
    return out


def redact_sensitive(value: RestorePhoneNumberResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number" in value:
        import capo_chime.types.phone_number

        out["phone_number"] = capo_chime.types.phone_number.redact_sensitive(
            value["phone_number"]
        )
    return out
