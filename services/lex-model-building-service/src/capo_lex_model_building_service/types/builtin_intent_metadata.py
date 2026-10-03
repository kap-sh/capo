"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#BuiltinIntentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.builtin_intent_signature
    import capo_lex_model_building_service.types.locale_list


class BuiltinIntentMetadata(TypedDict, closed=True):
    signature: NotRequired[
        "capo_lex_model_building_service.types.builtin_intent_signature.BuiltinIntentSignature"
    ]
    """<p>A unique identifier for the built-in intent. To find the signature for an intent, see <a href="https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents">Standard Built-in Intents</a> in the <i>Alexa Skills Kit</i>.</p>"""
    supported_locales: NotRequired[
        "capo_lex_model_building_service.types.locale_list.LocaleList"
    ]
    """<p>A list of identifiers for the locales that the intent supports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuiltinIntentMetadata) -> dict:
    out: dict = {}
    if "signature" in value:
        out["signature"] = value["signature"]
    if "supported_locales" in value:
        import capo_lex_model_building_service.types.locale_list

        out["supportedLocales"] = (
            capo_lex_model_building_service.types.locale_list.serialize_json(
                value["supported_locales"]
            )
        )
    return out


def deserialize_json(data: dict) -> BuiltinIntentMetadata:
    out: BuiltinIntentMetadata = {}  # type: ignore[typeddict-item]
    if data.get("signature") is not None:
        out["signature"] = data["signature"]
    if data.get("supportedLocales") is not None:
        import capo_lex_model_building_service.types.locale_list

        out["supported_locales"] = (
            capo_lex_model_building_service.types.locale_list.deserialize_json(
                data["supportedLocales"]
            )
        )
    return out
