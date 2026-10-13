"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTopicV2Response``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.custom_instructions
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.topic_id
    import capo_quicksight.types.topic_v2_details


class DescribeTopicV2Response(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    topic_id: NotRequired["capo_quicksight.types.topic_id.TopicId"]
    """<p>The ID of the topic that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    topic: NotRequired["capo_quicksight.types.topic_v2_details.TopicV2Details"]
    """<p>The definition of a topic.</p>"""
    custom_instructions: NotRequired[
        "capo_quicksight.types.custom_instructions.CustomInstructions"
    ]
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicV2Response) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "topic_id" in value:
        out["TopicId"] = value["topic_id"]
    if "topic" in value:
        import capo_quicksight.types.topic_v2_details

        out["Topic"] = capo_quicksight.types.topic_v2_details.serialize_json(
            value["topic"]
        )
    if "custom_instructions" in value:
        import capo_quicksight.types.custom_instructions

        out["CustomInstructions"] = (
            capo_quicksight.types.custom_instructions.serialize_json(
                value["custom_instructions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeTopicV2Response:
    out: DescribeTopicV2Response = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("TopicId") is not None:
        out["topic_id"] = data["TopicId"]
    if data.get("Topic") is not None:
        import capo_quicksight.types.topic_v2_details

        out["topic"] = capo_quicksight.types.topic_v2_details.deserialize_json(
            data["Topic"]
        )
    if data.get("CustomInstructions") is not None:
        import capo_quicksight.types.custom_instructions

        out["custom_instructions"] = (
            capo_quicksight.types.custom_instructions.deserialize_json(
                data["CustomInstructions"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: DescribeTopicV2Response) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_instructions" in value:
        import capo_quicksight.types.custom_instructions

        out["custom_instructions"] = (
            capo_quicksight.types.custom_instructions.redact_sensitive(
                value["custom_instructions"]
            )
        )
    return out
