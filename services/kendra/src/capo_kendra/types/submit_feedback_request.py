"""Generated from Smithy shape ``com.amazonaws.kendra#SubmitFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.click_feedback_list
    import capo_kendra.types.index_id
    import capo_kendra.types.query_id
    import capo_kendra.types.relevance_feedback_list


class SubmitFeedbackRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index that was queried.</p>"""
    query_id: "capo_kendra.types.query_id.QueryId"
    """<p>The identifier of the specific query for which you are submitting feedback. The query ID is returned in the response to the <code>Query</code> API.</p>"""
    click_feedback_items: NotRequired[
        "capo_kendra.types.click_feedback_list.ClickFeedbackList"
    ]
    """<p>Tells Amazon Kendra that a particular search result link was chosen by the user. </p>"""
    relevance_feedback_items: NotRequired[
        "capo_kendra.types.relevance_feedback_list.RelevanceFeedbackList"
    ]
    """<p>Provides Amazon Kendra with relevant or not relevant feedback for whether a particular item was relevant to the search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubmitFeedbackRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["QueryId"] = value["query_id"]
    if "click_feedback_items" in value:
        import capo_kendra.types.click_feedback_list

        out["ClickFeedbackItems"] = (
            capo_kendra.types.click_feedback_list.serialize_aws_json_1_1(
                value["click_feedback_items"]
            )
        )
    if "relevance_feedback_items" in value:
        import capo_kendra.types.relevance_feedback_list

        out["RelevanceFeedbackItems"] = (
            capo_kendra.types.relevance_feedback_list.serialize_aws_json_1_1(
                value["relevance_feedback_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubmitFeedbackRequest:
    out: SubmitFeedbackRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    else:
        out["query_id"] = ""
    if data.get("ClickFeedbackItems") is not None:
        import capo_kendra.types.click_feedback_list

        out["click_feedback_items"] = (
            capo_kendra.types.click_feedback_list.deserialize_aws_json_1_1(
                data["ClickFeedbackItems"]
            )
        )
    if data.get("RelevanceFeedbackItems") is not None:
        import capo_kendra.types.relevance_feedback_list

        out["relevance_feedback_items"] = (
            capo_kendra.types.relevance_feedback_list.deserialize_aws_json_1_1(
                data["RelevanceFeedbackItems"]
            )
        )
    return out
