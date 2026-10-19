"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#StartSpeakerSearchTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.call_leg_type
    import capo_chime_sdk_voice.types.client_request_id
    import capo_chime_sdk_voice.types.non_empty_string256
    import capo_chime_sdk_voice.types.voice_connector_id


class StartSpeakerSearchTaskRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""
    transaction_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    """<p>The transaction ID of the call being analyzed.</p>"""
    voice_profile_domain_id: (
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The ID of the voice profile domain that will store the voice profile.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_voice.types.client_request_id.ClientRequestId"
    ]
    """<p>The unique identifier for the client request. Use a different token for different speaker search tasks.</p>"""
    call_leg: NotRequired["capo_chime_sdk_voice.types.call_leg_type.CallLegType"]
    """<p>Specifies which call leg to stream for speaker search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSpeakerSearchTaskRequest) -> dict:
    out: dict = {}
    out["TransactionId"] = value["transaction_id"]
    out["VoiceProfileDomainId"] = value["voice_profile_domain_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "call_leg" in value:
        import capo_chime_sdk_voice.types.call_leg_type

        out["CallLeg"] = capo_chime_sdk_voice.types.call_leg_type.serialize_json(
            value["call_leg"]
        )
    return out


def deserialize_json(data: dict) -> StartSpeakerSearchTaskRequest:
    out: StartSpeakerSearchTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransactionId") is not None:
        out["transaction_id"] = data["TransactionId"]
    else:
        out["transaction_id"] = ""
    if data.get("VoiceProfileDomainId") is not None:
        out["voice_profile_domain_id"] = data["VoiceProfileDomainId"]
    else:
        out["voice_profile_domain_id"] = ""
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("CallLeg") is not None:
        import capo_chime_sdk_voice.types.call_leg_type

        out["call_leg"] = capo_chime_sdk_voice.types.call_leg_type.deserialize_json(
            data["CallLeg"]
        )
    return out
