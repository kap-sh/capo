"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AudioAndDTMFInputSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.audio_specification
    import capo_lex_models_v2.types.dtmf_specification
    import capo_lex_models_v2.types.time_in_milli_seconds


class AudioAndDTMFInputSpecification(TypedDict, closed=True):
    start_timeout_ms: (
        "capo_lex_models_v2.types.time_in_milli_seconds.TimeInMilliSeconds"
    )
    """<p>Time for which a bot waits before assuming that the customer isn't going to speak or press a key. This timeout is shared between Audio and DTMF inputs.</p>"""
    audio_specification: NotRequired[
        "capo_lex_models_v2.types.audio_specification.AudioSpecification"
    ]
    """<p>Specifies the settings on audio input.</p>"""
    dtmf_specification: NotRequired[
        "capo_lex_models_v2.types.dtmf_specification.DTMFSpecification"
    ]
    """<p>Specifies the settings on DTMF input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioAndDTMFInputSpecification) -> dict:
    out: dict = {}
    out["startTimeoutMs"] = value["start_timeout_ms"]
    if "audio_specification" in value:
        import capo_lex_models_v2.types.audio_specification

        out["audioSpecification"] = (
            capo_lex_models_v2.types.audio_specification.serialize_json(
                value["audio_specification"]
            )
        )
    if "dtmf_specification" in value:
        import capo_lex_models_v2.types.dtmf_specification

        out["dtmfSpecification"] = (
            capo_lex_models_v2.types.dtmf_specification.serialize_json(
                value["dtmf_specification"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioAndDTMFInputSpecification:
    out: AudioAndDTMFInputSpecification = {}  # type: ignore[typeddict-item]
    if data.get("startTimeoutMs") is not None:
        out["start_timeout_ms"] = data["startTimeoutMs"]
    else:
        out["start_timeout_ms"] = 0
    if data.get("audioSpecification") is not None:
        import capo_lex_models_v2.types.audio_specification

        out["audio_specification"] = (
            capo_lex_models_v2.types.audio_specification.deserialize_json(
                data["audioSpecification"]
            )
        )
    if data.get("dtmfSpecification") is not None:
        import capo_lex_models_v2.types.dtmf_specification

        out["dtmf_specification"] = (
            capo_lex_models_v2.types.dtmf_specification.deserialize_json(
                data["dtmfSpecification"]
            )
        )
    return out
