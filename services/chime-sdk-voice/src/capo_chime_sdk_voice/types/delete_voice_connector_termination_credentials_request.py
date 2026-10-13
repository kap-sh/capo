"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteVoiceConnectorTerminationCredentialsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sensitive_string_list
    import capo_chime_sdk_voice.types.voice_connector_id


class DeleteVoiceConnectorTerminationCredentialsRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""
    usernames: "capo_chime_sdk_voice.types.sensitive_string_list.SensitiveStringList"
    """<p>The RFC2617 compliant username associated with the SIP credentials, in US-ASCII format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVoiceConnectorTerminationCredentialsRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.sensitive_string_list

    out["Usernames"] = capo_chime_sdk_voice.types.sensitive_string_list.serialize_json(
        value["usernames"]
    )
    return out


def deserialize_json(data: dict) -> DeleteVoiceConnectorTerminationCredentialsRequest:
    out: DeleteVoiceConnectorTerminationCredentialsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Usernames") is not None:
        import capo_chime_sdk_voice.types.sensitive_string_list

        out["usernames"] = (
            capo_chime_sdk_voice.types.sensitive_string_list.deserialize_json(
                data["Usernames"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteVoiceConnectorTerminationCredentialsRequest.usernames required"
        )
    return out


def redact_sensitive(
    value: DeleteVoiceConnectorTerminationCredentialsRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "usernames" in value:
        import capo_chime_sdk_voice.types.sensitive_string_list

        out["usernames"] = (
            capo_chime_sdk_voice.types.sensitive_string_list.redact_sensitive(
                value["usernames"]
            )
        )
    return out
