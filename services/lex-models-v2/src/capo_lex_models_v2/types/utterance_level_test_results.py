"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceLevelTestResults``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.utterance_level_test_result_item_list


class UtteranceLevelTestResults(TypedDict, closed=True):
    items: "capo_lex_models_v2.types.utterance_level_test_result_item_list.UtteranceLevelTestResultItemList"
    """<p>Contains information about an utterance in the results of the test set execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceLevelTestResults) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.utterance_level_test_result_item_list

    out["items"] = (
        capo_lex_models_v2.types.utterance_level_test_result_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> UtteranceLevelTestResults:
    out: UtteranceLevelTestResults = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_lex_models_v2.types.utterance_level_test_result_item_list

        out["items"] = (
            capo_lex_models_v2.types.utterance_level_test_result_item_list.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    return out
