"""Generated from Smithy shape ``com.amazonaws.quicksight#PredictQAResultsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.include_generated_answer
    import capo_quicksight.types.include_quick_sight_q_index
    import capo_quicksight.types.max_topics_to_consider
    import capo_quicksight.types.qa_query_text


class PredictQAResultsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that the user wants to execute Predict QA results in.</p>"""
    query_text: "capo_quicksight.types.qa_query_text.QAQueryText"
    """<p>The query text to be used to predict QA results.</p>"""
    include_quick_sight_q_index: NotRequired[
        "capo_quicksight.types.include_quick_sight_q_index.IncludeQuickSightQIndex"
    ]
    """<p>Indicates whether Q indicies are included or excluded.</p>"""
    include_generated_answer: NotRequired[
        "capo_quicksight.types.include_generated_answer.IncludeGeneratedAnswer"
    ]
    """<p>Indicates whether generated answers are included or excluded.</p>"""
    max_topics_to_consider: NotRequired[
        "capo_quicksight.types.max_topics_to_consider.MaxTopicsToConsider"
    ]
    """<p>The number of maximum topics to be considered to predict QA results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictQAResultsRequest) -> dict:
    out: dict = {}
    out["QueryText"] = value["query_text"]
    if "include_quick_sight_q_index" in value:
        import capo_quicksight.types.include_quick_sight_q_index

        out["IncludeQuickSightQIndex"] = (
            capo_quicksight.types.include_quick_sight_q_index.serialize_json(
                value["include_quick_sight_q_index"]
            )
        )
    if "include_generated_answer" in value:
        import capo_quicksight.types.include_generated_answer

        out["IncludeGeneratedAnswer"] = (
            capo_quicksight.types.include_generated_answer.serialize_json(
                value["include_generated_answer"]
            )
        )
    if "max_topics_to_consider" in value:
        out["MaxTopicsToConsider"] = value["max_topics_to_consider"]
    return out


def deserialize_json(data: dict) -> PredictQAResultsRequest:
    out: PredictQAResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueryText") is not None:
        out["query_text"] = data["QueryText"]
    else:
        raise DeserializationError("PredictQAResultsRequest.query_text required")
    if data.get("IncludeQuickSightQIndex") is not None:
        import capo_quicksight.types.include_quick_sight_q_index

        out["include_quick_sight_q_index"] = (
            capo_quicksight.types.include_quick_sight_q_index.deserialize_json(
                data["IncludeQuickSightQIndex"]
            )
        )
    if data.get("IncludeGeneratedAnswer") is not None:
        import capo_quicksight.types.include_generated_answer

        out["include_generated_answer"] = (
            capo_quicksight.types.include_generated_answer.deserialize_json(
                data["IncludeGeneratedAnswer"]
            )
        )
    if data.get("MaxTopicsToConsider") is not None:
        out["max_topics_to_consider"] = data["MaxTopicsToConsider"]
    return out


def redact_sensitive(value: PredictQAResultsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_text" in value:
        out["query_text"] = "*** Sensitive Data Redacted ***"
    return out
