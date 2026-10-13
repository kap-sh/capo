"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTopicRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.custom_instructions
    import capo_quicksight.types.topic_details
    import capo_quicksight.types.topic_id


class UpdateTopicRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the topic that you want to update.</p>"""
    topic_id: "capo_quicksight.types.topic_id.TopicId"
    """<p>The ID of the topic that you want to modify. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic: "capo_quicksight.types.topic_details.TopicDetails"
    """<p>The definition of the topic that you want to update.</p>"""
    custom_instructions: NotRequired[
        "capo_quicksight.types.custom_instructions.CustomInstructions"
    ]
    """<p>Custom instructions for the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTopicRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.topic_details

    out["Topic"] = capo_quicksight.types.topic_details.serialize_json(value["topic"])
    if "custom_instructions" in value:
        import capo_quicksight.types.custom_instructions

        out["CustomInstructions"] = (
            capo_quicksight.types.custom_instructions.serialize_json(
                value["custom_instructions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTopicRequest:
    out: UpdateTopicRequest = {}  # type: ignore[typeddict-item]
    if data.get("Topic") is not None:
        import capo_quicksight.types.topic_details

        out["topic"] = capo_quicksight.types.topic_details.deserialize_json(
            data["Topic"]
        )
    else:
        raise DeserializationError("UpdateTopicRequest.topic required")
    if data.get("CustomInstructions") is not None:
        import capo_quicksight.types.custom_instructions

        out["custom_instructions"] = (
            capo_quicksight.types.custom_instructions.deserialize_json(
                data["CustomInstructions"]
            )
        )
    return out


def redact_sensitive(value: UpdateTopicRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "topic" in value:
        import capo_quicksight.types.topic_details

        out["topic"] = capo_quicksight.types.topic_details.redact_sensitive(
            value["topic"]
        )
    if "custom_instructions" in value:
        import capo_quicksight.types.custom_instructions

        out["custom_instructions"] = (
            capo_quicksight.types.custom_instructions.redact_sensitive(
                value["custom_instructions"]
            )
        )
    return out
