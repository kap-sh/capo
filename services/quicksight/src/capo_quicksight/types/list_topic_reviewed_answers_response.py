"""Generated from Smithy shape ``com.amazonaws.quicksight#ListTopicReviewedAnswersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.topic_id
    import capo_quicksight.types.topic_reviewed_answers


class ListTopicReviewedAnswersResponse(TypedDict, closed=True):
    topic_id: NotRequired["capo_quicksight.types.topic_id.TopicId"]
    """<p>The ID for the topic that contains the reviewed answer that you want to list. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    answers: NotRequired[
        "capo_quicksight.types.topic_reviewed_answers.TopicReviewedAnswers"
    ]
    """<p>The definition of all Answers in the topic.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTopicReviewedAnswersResponse) -> dict:
    out: dict = {}
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "answers" in value:
        import capo_quicksight.types.topic_reviewed_answers

        out["Answers"] = capo_quicksight.types.topic_reviewed_answers.serialize_json(
            value["answers"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListTopicReviewedAnswersResponse:
    out: ListTopicReviewedAnswersResponse = {}  # type: ignore[typeddict-item]
    if data.get("TopicId") is not None:
        out["topic_id"] = data["TopicId"]
    if data.get("TopicArn") is not None:
        out["topic_arn"] = data["TopicArn"]
    if data.get("Answers") is not None:
        import capo_quicksight.types.topic_reviewed_answers

        out["answers"] = capo_quicksight.types.topic_reviewed_answers.deserialize_json(
            data["Answers"]
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: ListTopicReviewedAnswersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "answers" in value:
        import capo_quicksight.types.topic_reviewed_answers

        out["answers"] = capo_quicksight.types.topic_reviewed_answers.redact_sensitive(
            value["answers"]
        )
    return out
