"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AllowedInputTypes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boxed_boolean


class AllowedInputTypes(TypedDict, closed=True):
    allow_audio_input: "capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Indicates whether audio input is allowed.</p>"""
    allow_dtmf_input: "capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Indicates whether DTMF input is allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedInputTypes) -> dict:
    out: dict = {}
    out["allowAudioInput"] = value["allow_audio_input"]
    out["allowDTMFInput"] = value["allow_dtmf_input"]
    return out


def deserialize_json(data: dict) -> AllowedInputTypes:
    out: AllowedInputTypes = {}  # type: ignore[typeddict-item]
    if data.get("allowAudioInput") is not None:
        out["allow_audio_input"] = data["allowAudioInput"]
    else:
        out["allow_audio_input"] = False
    if data.get("allowDTMFInput") is not None:
        out["allow_dtmf_input"] = data["allowDTMFInput"]
    else:
        out["allow_dtmf_input"] = False
    return out
