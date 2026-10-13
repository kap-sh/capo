"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateTopicReviewedAnswers``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.create_topic_reviewed_answer

CreateTopicReviewedAnswers: TypeAlias = list[
    "capo_quicksight.types.create_topic_reviewed_answer.CreateTopicReviewedAnswer"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicReviewedAnswers) -> list:
    import capo_quicksight.types.create_topic_reviewed_answer

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.create_topic_reviewed_answer.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CreateTopicReviewedAnswers:
    import capo_quicksight.types.create_topic_reviewed_answer

    out: CreateTopicReviewedAnswers = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.create_topic_reviewed_answer.deserialize_json(item)
        )
    return out


def redact_sensitive(value: CreateTopicReviewedAnswers) -> list[Any]:
    import capo_quicksight.types.create_topic_reviewed_answer

    return [
        capo_quicksight.types.create_topic_reviewed_answer.redact_sensitive(item)
        for item in value
    ]
