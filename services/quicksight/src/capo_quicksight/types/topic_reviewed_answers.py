"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicReviewedAnswers``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.topic_reviewed_answer

TopicReviewedAnswers: TypeAlias = list[
    "capo_quicksight.types.topic_reviewed_answer.TopicReviewedAnswer"
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicReviewedAnswers) -> list:
    import capo_quicksight.types.topic_reviewed_answer

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.topic_reviewed_answer.serialize_json(item))
    return out


def deserialize_json(data: list) -> TopicReviewedAnswers:
    import capo_quicksight.types.topic_reviewed_answer

    out: TopicReviewedAnswers = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.topic_reviewed_answer.deserialize_json(item))
    return out


def redact_sensitive(value: TopicReviewedAnswers) -> list[Any]:
    import capo_quicksight.types.topic_reviewed_answer

    return [
        capo_quicksight.types.topic_reviewed_answer.redact_sensitive(item)
        for item in value
    ]
