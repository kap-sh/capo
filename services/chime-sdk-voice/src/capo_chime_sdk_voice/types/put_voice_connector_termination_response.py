"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorTerminationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.termination


class PutVoiceConnectorTerminationResponse(TypedDict, closed=True):
    termination: NotRequired["capo_chime_sdk_voice.types.termination.Termination"]
    """<p>The updated termination settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorTerminationResponse) -> dict:
    out: dict = {}
    if "termination" in value:
        import capo_chime_sdk_voice.types.termination

        out["Termination"] = capo_chime_sdk_voice.types.termination.serialize_json(
            value["termination"]
        )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorTerminationResponse:
    out: PutVoiceConnectorTerminationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Termination") is not None:
        import capo_chime_sdk_voice.types.termination

        out["termination"] = capo_chime_sdk_voice.types.termination.deserialize_json(
            data["Termination"]
        )
    return out


def redact_sensitive(value: PutVoiceConnectorTerminationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "termination" in value:
        import capo_chime_sdk_voice.types.termination

        out["termination"] = capo_chime_sdk_voice.types.termination.redact_sensitive(
            value["termination"]
        )
    return out
