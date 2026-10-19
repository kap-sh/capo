"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SampleUtterance``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.utterance


class SampleUtterance(TypedDict, closed=True):
    utterance: "capo_lex_models_v2.types.utterance.Utterance"
    """<p>The sample utterance that Amazon Lex uses to build its machine-learning model to recognize intents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SampleUtterance) -> dict:
    out: dict = {}
    out["utterance"] = value["utterance"]
    return out


def deserialize_json(data: dict) -> SampleUtterance:
    out: SampleUtterance = {}  # type: ignore[typeddict-item]
    if data.get("utterance") is not None:
        out["utterance"] = data["utterance"]
    else:
        out["utterance"] = ""
    return out
