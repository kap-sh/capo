"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTopicV2Request``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.custom_instructions
    import capo_quicksight.types.topic_id
    import capo_quicksight.types.topic_v2_details
    import capo_quicksight.types.topic_v2_publish_option


class UpdateTopicV2Request(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the topic that you want to update.</p>"""
    topic_id: "capo_quicksight.types.topic_id.TopicId"
    """<p>The ID of the topic that you want to modify. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic: "capo_quicksight.types.topic_v2_details.TopicV2Details"
    """<p>The definition of the topic that you want to update.</p>"""
    custom_instructions: NotRequired[
        "capo_quicksight.types.custom_instructions.CustomInstructions"
    ]
    publish_option: NotRequired[
        "capo_quicksight.types.topic_v2_publish_option.TopicV2PublishOption"
    ]
    """<p>The publish option for the topic that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTopicV2Request) -> dict:
    out: dict = {}
    import capo_quicksight.types.topic_v2_details

    out["Topic"] = capo_quicksight.types.topic_v2_details.serialize_json(value["topic"])
    if "custom_instructions" in value:
        import capo_quicksight.types.custom_instructions

        out["CustomInstructions"] = (
            capo_quicksight.types.custom_instructions.serialize_json(
                value["custom_instructions"]
            )
        )
    if "publish_option" in value:
        import capo_quicksight.types.topic_v2_publish_option

        out["PublishOption"] = (
            capo_quicksight.types.topic_v2_publish_option.serialize_json(
                value["publish_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTopicV2Request:
    out: UpdateTopicV2Request = {}  # type: ignore[typeddict-item]
    if data.get("Topic") is not None:
        import capo_quicksight.types.topic_v2_details

        out["topic"] = capo_quicksight.types.topic_v2_details.deserialize_json(
            data["Topic"]
        )
    else:
        raise DeserializationError("UpdateTopicV2Request.topic required")
    if data.get("CustomInstructions") is not None:
        import capo_quicksight.types.custom_instructions

        out["custom_instructions"] = (
            capo_quicksight.types.custom_instructions.deserialize_json(
                data["CustomInstructions"]
            )
        )
    if data.get("PublishOption") is not None:
        import capo_quicksight.types.topic_v2_publish_option

        out["publish_option"] = (
            capo_quicksight.types.topic_v2_publish_option.deserialize_json(
                data["PublishOption"]
            )
        )
    return out


def redact_sensitive(value: UpdateTopicV2Request) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_instructions" in value:
        import capo_quicksight.types.custom_instructions

        out["custom_instructions"] = (
            capo_quicksight.types.custom_instructions.redact_sensitive(
                value["custom_instructions"]
            )
        )
    return out
