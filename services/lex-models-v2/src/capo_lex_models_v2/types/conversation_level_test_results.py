"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ConversationLevelTestResults``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.conversation_level_test_result_item_list


class ConversationLevelTestResults(TypedDict, closed=True):
    items: "capo_lex_models_v2.types.conversation_level_test_result_item_list.ConversationLevelTestResultItemList"
    """<p>The item list in the test set results data at the conversation level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLevelTestResults) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.conversation_level_test_result_item_list

    out["items"] = (
        capo_lex_models_v2.types.conversation_level_test_result_item_list.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConversationLevelTestResults:
    out: ConversationLevelTestResults = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_lex_models_v2.types.conversation_level_test_result_item_list

        out["items"] = (
            capo_lex_models_v2.types.conversation_level_test_result_item_list.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    return out
