"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#AssociatePhoneNumbersWithVoiceConnectorGroupResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.phone_number_error_list


class AssociatePhoneNumbersWithVoiceConnectorGroupResponse(TypedDict, closed=True):
    phone_number_errors: NotRequired[
        "capo_chime_sdk_voice.types.phone_number_error_list.PhoneNumberErrorList"
    ]
    """<p>If the action fails for one or more of the phone numbers in the request, a list of the phone numbers is returned, along with error codes and error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePhoneNumbersWithVoiceConnectorGroupResponse) -> dict:
    out: dict = {}
    if "phone_number_errors" in value:
        import capo_chime_sdk_voice.types.phone_number_error_list

        out["PhoneNumberErrors"] = (
            capo_chime_sdk_voice.types.phone_number_error_list.serialize_json(
                value["phone_number_errors"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AssociatePhoneNumbersWithVoiceConnectorGroupResponse:
    out: AssociatePhoneNumbersWithVoiceConnectorGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberErrors") is not None:
        import capo_chime_sdk_voice.types.phone_number_error_list

        out["phone_number_errors"] = (
            capo_chime_sdk_voice.types.phone_number_error_list.deserialize_json(
                data["PhoneNumberErrors"]
            )
        )
    return out


def redact_sensitive(
    value: AssociatePhoneNumbersWithVoiceConnectorGroupResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number_errors" in value:
        import capo_chime_sdk_voice.types.phone_number_error_list

        out["phone_number_errors"] = (
            capo_chime_sdk_voice.types.phone_number_error_list.redact_sensitive(
                value["phone_number_errors"]
            )
        )
    return out
