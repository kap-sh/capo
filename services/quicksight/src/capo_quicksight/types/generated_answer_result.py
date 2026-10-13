"""Generated from Smithy shape ``com.amazonaws.quicksight#GeneratedAnswerResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.answer_id
    import capo_quicksight.types.generated_answer_status
    import capo_quicksight.types.qa_query_text
    import capo_quicksight.types.qa_url
    import capo_quicksight.types.question_id
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.topic_id


class GeneratedAnswerResult(TypedDict, closed=True):
    question_text: NotRequired["capo_quicksight.types.qa_query_text.QAQueryText"]
    """<p>The question text.</p>"""
    answer_status: NotRequired[
        "capo_quicksight.types.generated_answer_status.GeneratedAnswerStatus"
    ]
    """<p>The answer status of the generated answer.</p>"""
    topic_id: NotRequired["capo_quicksight.types.topic_id.TopicId"]
    """<p>The ID of the topic.</p>"""
    topic_name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>The name of the topic.</p>"""
    restatement: NotRequired["capo_quicksight.types.qa_query_text.QAQueryText"]
    """<p>The restatement for the answer.</p>"""
    question_id: NotRequired["capo_quicksight.types.question_id.QuestionId"]
    """<p>The ID of the question.</p>"""
    answer_id: NotRequired["capo_quicksight.types.answer_id.AnswerId"]
    """<p>The ID of the answer.</p>"""
    question_url: NotRequired["capo_quicksight.types.qa_url.QAUrl"]
    """<p>The URL of the question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedAnswerResult) -> dict:
    out: dict = {}
    if "question_text" in value:
        out["QuestionText"] = value["question_text"]
    if "answer_status" in value:
        import capo_quicksight.types.generated_answer_status

        out["AnswerStatus"] = (
            capo_quicksight.types.generated_answer_status.serialize_json(
                value["answer_status"]
            )
        )
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    if "restatement" in value:
        out["Restatement"] = value["restatement"]
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "answer_id" in value:
        out["AnswerId"] = value["answer_id"]
    if "question_url" in value:
        out["QuestionUrl"] = value["question_url"]
    return out


def deserialize_json(data: dict) -> GeneratedAnswerResult:
    out: GeneratedAnswerResult = {}  # type: ignore[typeddict-item]
    if data.get("QuestionText") is not None:
        out["question_text"] = data["QuestionText"]
    if data.get("AnswerStatus") is not None:
        import capo_quicksight.types.generated_answer_status

        out["answer_status"] = (
            capo_quicksight.types.generated_answer_status.deserialize_json(
                data["AnswerStatus"]
            )
        )
    if data.get("TopicId") is not None:
        out["topic_id"] = data["TopicId"]
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    if data.get("Restatement") is not None:
        out["restatement"] = data["Restatement"]
    if data.get("QuestionId") is not None:
        out["question_id"] = data["QuestionId"]
    if data.get("AnswerId") is not None:
        out["answer_id"] = data["AnswerId"]
    if data.get("QuestionUrl") is not None:
        out["question_url"] = data["QuestionUrl"]
    return out


def redact_sensitive(value: GeneratedAnswerResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "question_text" in value:
        out["question_text"] = "*** Sensitive Data Redacted ***"
    if "restatement" in value:
        out["restatement"] = "*** Sensitive Data Redacted ***"
    return out
