"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#PredictedIntent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.intent_confidence
    import capo_lex_runtime_service.types.intent_name
    import capo_lex_runtime_service.types.string_map


class PredictedIntent(TypedDict, closed=True):
    intent_name: NotRequired["capo_lex_runtime_service.types.intent_name.IntentName"]
    """<p>The name of the intent that Amazon Lex suggests satisfies the user's intent.</p>"""
    nlu_intent_confidence: NotRequired[
        "capo_lex_runtime_service.types.intent_confidence.IntentConfidence"
    ]
    """<p>Indicates how confident Amazon Lex is that an intent satisfies the user's intent.</p>"""
    slots: NotRequired["capo_lex_runtime_service.types.string_map.StringMap"]
    """<p>The slot and slot values associated with the predicted intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictedIntent) -> dict:
    out: dict = {}
    if "intent_name" in value:
        out["intentName"] = value["intent_name"]
    if "nlu_intent_confidence" in value:
        import capo_lex_runtime_service.types.intent_confidence

        out["nluIntentConfidence"] = (
            capo_lex_runtime_service.types.intent_confidence.serialize_json(
                value["nlu_intent_confidence"]
            )
        )
    if "slots" in value:
        import capo_lex_runtime_service.types.string_map

        out["slots"] = capo_lex_runtime_service.types.string_map.serialize_json(
            value["slots"]
        )
    return out


def deserialize_json(data: dict) -> PredictedIntent:
    out: PredictedIntent = {}  # type: ignore[typeddict-item]
    if data.get("intentName") is not None:
        out["intent_name"] = data["intentName"]
    if data.get("nluIntentConfidence") is not None:
        import capo_lex_runtime_service.types.intent_confidence

        out["nlu_intent_confidence"] = (
            capo_lex_runtime_service.types.intent_confidence.deserialize_json(
                data["nluIntentConfidence"]
            )
        )
    if data.get("slots") is not None:
        import capo_lex_runtime_service.types.string_map

        out["slots"] = capo_lex_runtime_service.types.string_map.deserialize_json(
            data["slots"]
        )
    return out


def redact_sensitive(value: PredictedIntent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "slots" in value:
        out["slots"] = "*** Sensitive Data Redacted ***"
    return out
