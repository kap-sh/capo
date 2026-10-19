"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelIntentClassificationResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.test_result_match_status


class ConversationLevelIntentClassificationResultItem(TypedDict, closed=True):
    intent_name: "capo_lex_models_v2.types.name.Name"
    """<p>The intent name used in the evaluation of intent level success or failure.</p>"""
    match_result: (
        "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus"
    )
    """<p>The number of times the specific intent is used in the evaluation of intent level success or failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelIntentClassificationResultItem) -> dict:
    out: dict = {}
    out["intentName"] = value["intent_name"]
    import capo_lex_models_v2.types.test_result_match_status

    out["matchResult"] = (
        capo_lex_models_v2.types.test_result_match_status.serialize_json(
            value["match_result"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConversationLevelIntentClassificationResultItem:
    out: ConversationLevelIntentClassificationResultItem = {}  # type: ignore[typeddict-item]
    if data.get("intentName") is not None:
        out["intent_name"] = data["intentName"]
    else:
        out["intent_name"] = ""
    if data.get("matchResult") is not None:
        import capo_lex_models_v2.types.test_result_match_status

        out["match_result"] = (
            capo_lex_models_v2.types.test_result_match_status.deserialize_json(
                data["matchResult"]
            )
        )
    else:
        import typing

        out["match_result"] = typing.cast(
            "capo_lex_models_v2.types.test_result_match_status.TestResultMatchStatus",
            "",
        )
    return out
