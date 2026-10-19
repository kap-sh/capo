"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#StartVoiceToneAnalysisTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.client_request_id
    import capo_chime_sdk_voice.types.language_code
    import capo_chime_sdk_voice.types.non_empty_string256
    import capo_chime_sdk_voice.types.voice_connector_id


class StartVoiceToneAnalysisTaskRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""
    transaction_id: "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    """<p>The transaction ID.</p>"""
    language_code: "capo_chime_sdk_voice.types.language_code.LanguageCode"
    """<p>The language code.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_voice.types.client_request_id.ClientRequestId"
    ]
    """<p>The unique identifier for the client request. Use a different token for different voice tone analysis tasks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartVoiceToneAnalysisTaskRequest) -> dict:
    out: dict = {}
    out["TransactionId"] = value["transaction_id"]
    import capo_chime_sdk_voice.types.language_code

    out["LanguageCode"] = capo_chime_sdk_voice.types.language_code.serialize_json(
        value["language_code"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> StartVoiceToneAnalysisTaskRequest:
    out: StartVoiceToneAnalysisTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransactionId") is not None:
        out["transaction_id"] = data["TransactionId"]
    else:
        out["transaction_id"] = ""
    if data.get("LanguageCode") is not None:
        import capo_chime_sdk_voice.types.language_code

        out["language_code"] = (
            capo_chime_sdk_voice.types.language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    else:
        import typing

        out["language_code"] = typing.cast(
            "capo_chime_sdk_voice.types.language_code.LanguageCode", ""
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
