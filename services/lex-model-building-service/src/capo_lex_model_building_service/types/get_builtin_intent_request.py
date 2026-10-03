"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBuiltinIntentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.builtin_intent_signature


class GetBuiltinIntentRequest(TypedDict, closed=True):
    signature: "capo_lex_model_building_service.types.builtin_intent_signature.BuiltinIntentSignature"
    """<p>The unique identifier for a built-in intent. To find the signature for an intent, see <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBuiltinIntentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBuiltinIntentRequest:
    out: GetBuiltinIntentRequest = {}  # type: ignore[typeddict-item]
    return out
