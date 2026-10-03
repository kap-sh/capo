"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionResultFilterBy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.conversation_level_test_results_filter_by
    import capo_lex_models_v2.types.test_result_type_filter


class TestExecutionResultFilterBy(TypedDict, closed=True):
    result_type_filter: (
        "capo_lex_models_v2.types.test_result_type_filter.TestResultTypeFilter"
    )
    """<p>Specifies which results to filter. See <a href="https://docs.aws.amazon.com/lexv2/latest/dg/test-results-details-test-set.html">Test result details">Test results details</a> for details about different types of results.</p>"""
    conversation_level_test_results_filter_by: NotRequired[
        "capo_lex_models_v2.types.conversation_level_test_results_filter_by.ConversationLevelTestResultsFilterBy"
    ]
    """<p>Contains information about the method for filtering Conversation level test results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionResultFilterBy) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.test_result_type_filter

    out["resultTypeFilter"] = (
        capo_lex_models_v2.types.test_result_type_filter.serialize_json(
            value["result_type_filter"]
        )
    )
    if "conversation_level_test_results_filter_by" in value:
        import capo_lex_models_v2.types.conversation_level_test_results_filter_by

        out["conversationLevelTestResultsFilterBy"] = (
            capo_lex_models_v2.types.conversation_level_test_results_filter_by.serialize_json(
                value["conversation_level_test_results_filter_by"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestExecutionResultFilterBy:
    out: TestExecutionResultFilterBy = {}  # type: ignore[typeddict-item]
    if data.get("resultTypeFilter") is not None:
        import capo_lex_models_v2.types.test_result_type_filter

        out["result_type_filter"] = (
            capo_lex_models_v2.types.test_result_type_filter.deserialize_json(
                data["resultTypeFilter"]
            )
        )
    else:
        raise DeserializationError(
            "TestExecutionResultFilterBy.result_type_filter required"
        )
    if data.get("conversationLevelTestResultsFilterBy") is not None:
        import capo_lex_models_v2.types.conversation_level_test_results_filter_by

        out["conversation_level_test_results_filter_by"] = (
            capo_lex_models_v2.types.conversation_level_test_results_filter_by.deserialize_json(
                data["conversationLevelTestResultsFilterBy"]
            )
        )
    return out
