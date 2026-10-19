"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DTMFSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.dtmf_character
    import capo_lex_models_v2.types.max_utterance_digits
    import capo_lex_models_v2.types.time_in_milli_seconds


class DTMFSpecification(TypedDict, closed=True):
    max_length: "capo_lex_models_v2.types.max_utterance_digits.MaxUtteranceDigits"
    """<p>The maximum number of DTMF digits allowed in an utterance.</p>"""
    end_timeout_ms: "capo_lex_models_v2.types.time_in_milli_seconds.TimeInMilliSeconds"
    """<p>How long the bot should wait after the last DTMF character input before assuming that the input has concluded.</p>"""
    deletion_character: "capo_lex_models_v2.types.dtmf_character.DTMFCharacter"
    """<p>The DTMF character that clears the accumulated DTMF digits and immediately ends the input.</p>"""
    end_character: "capo_lex_models_v2.types.dtmf_character.DTMFCharacter"
    """<p>The DTMF character that immediately ends input. If the user does not press this character, the input ends after the end timeout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DTMFSpecification) -> dict:
    out: dict = {}
    out["maxLength"] = value["max_length"]
    out["endTimeoutMs"] = value["end_timeout_ms"]
    out["deletionCharacter"] = value["deletion_character"]
    out["endCharacter"] = value["end_character"]
    return out


def deserialize_json(data: dict) -> DTMFSpecification:
    out: DTMFSpecification = {}  # type: ignore[typeddict-item]
    if data.get("maxLength") is not None:
        out["max_length"] = data["maxLength"]
    else:
        out["max_length"] = 0
    if data.get("endTimeoutMs") is not None:
        out["end_timeout_ms"] = data["endTimeoutMs"]
    else:
        out["end_timeout_ms"] = 0
    if data.get("deletionCharacter") is not None:
        out["deletion_character"] = data["deletionCharacter"]
    else:
        out["deletion_character"] = ""
    if data.get("endCharacter") is not None:
        out["end_character"] = data["endCharacter"]
    else:
        out["end_character"] = ""
    return out
