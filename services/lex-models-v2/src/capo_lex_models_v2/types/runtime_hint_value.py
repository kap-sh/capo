"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#RuntimeHintValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.runtime_hint_phrase


class RuntimeHintValue(TypedDict, closed=True):
    phrase: "capo_lex_models_v2.types.runtime_hint_phrase.RuntimeHintPhrase"
    """<p>The phrase that Amazon Lex should look for in the user's input to the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeHintValue) -> dict:
    out: dict = {}
    out["phrase"] = value["phrase"]
    return out


def deserialize_json(data: dict) -> RuntimeHintValue:
    out: RuntimeHintValue = {}  # type: ignore[typeddict-item]
    if data.get("phrase") is not None:
        out["phrase"] = data["phrase"]
    else:
        out["phrase"] = ""
    return out
