"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentClassificationTestResults``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.intent_classification_test_result_item_list


class IntentClassificationTestResults(TypedDict, closed=True):
    items: "capo_lex_models_v2.types.intent_classification_test_result_item_list.IntentClassificationTestResultItemList"
    """<p>A list of the results for the intent classification test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentClassificationTestResults) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.intent_classification_test_result_item_list

    out["items"] = (
        capo_lex_models_v2.types.intent_classification_test_result_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> IntentClassificationTestResults:
    out: IntentClassificationTestResults = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_lex_models_v2.types.intent_classification_test_result_item_list

        out["items"] = (
            capo_lex_models_v2.types.intent_classification_test_result_item_list.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    return out
