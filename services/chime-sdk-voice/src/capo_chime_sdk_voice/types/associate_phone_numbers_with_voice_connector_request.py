"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#AssociatePhoneNumbersWithVoiceConnectorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.e164_phone_number_list
    import capo_chime_sdk_voice.types.nullable_boolean
    import capo_chime_sdk_voice.types.voice_connector_id


class AssociatePhoneNumbersWithVoiceConnectorRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""
    e164_phone_numbers: (
        "capo_chime_sdk_voice.types.e164_phone_number_list.E164PhoneNumberList"
    )
    """<p>List of phone numbers, in E.164 format.</p>"""
    force_associate: NotRequired[
        "capo_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
    ]
    """<p>If true, associates the provided phone numbers with the provided Amazon Chime SDK Voice Connector and removes any previously existing associations. If false, does not associate any phone numbers that have previously existing associations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePhoneNumbersWithVoiceConnectorRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.e164_phone_number_list

    out["E164PhoneNumbers"] = (
        capo_chime_sdk_voice.types.e164_phone_number_list.serialize_json(
            value["e164_phone_numbers"]
        )
    )
    if "force_associate" in value:
        out["ForceAssociate"] = value["force_associate"]
    return out


def deserialize_json(data: dict) -> AssociatePhoneNumbersWithVoiceConnectorRequest:
    out: AssociatePhoneNumbersWithVoiceConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("E164PhoneNumbers") is not None:
        import capo_chime_sdk_voice.types.e164_phone_number_list

        out["e164_phone_numbers"] = (
            capo_chime_sdk_voice.types.e164_phone_number_list.deserialize_json(
                data["E164PhoneNumbers"]
            )
        )
    else:
        out["e164_phone_numbers"] = []
    if data.get("ForceAssociate") is not None:
        out["force_associate"] = data["ForceAssociate"]
    return out


def redact_sensitive(
    value: AssociatePhoneNumbersWithVoiceConnectorRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "e164_phone_numbers" in value:
        import capo_chime_sdk_voice.types.e164_phone_number_list

        out["e164_phone_numbers"] = (
            capo_chime_sdk_voice.types.e164_phone_number_list.redact_sensitive(
                value["e164_phone_numbers"]
            )
        )
    return out
