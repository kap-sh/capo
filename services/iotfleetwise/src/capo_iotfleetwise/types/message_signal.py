"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#MessageSignal``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.structured_message
    import capo_iotfleetwise.types.topic_name


class MessageSignal(TypedDict, closed=True):
    topic_name: "capo_iotfleetwise.types.topic_name.TopicName"
    """<p>The topic name for the message signal. It corresponds to topics in ROS 2. </p>"""
    structured_message: "capo_iotfleetwise.types.structured_message.StructuredMessage"
    """<p>The structured message for the message signal. It can be defined with either a <code>primitiveMessageDefinition</code>, <code>structuredMessageListDefinition</code>, or <code>structuredMessageDefinition</code> recursively.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageSignal) -> dict:
    out: dict = {}
    out["topicName"] = value["topic_name"]
    import capo_iotfleetwise.types.structured_message

    out["structuredMessage"] = (
        capo_iotfleetwise.types.structured_message.serialize_aws_json_1_0(
            value["structured_message"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MessageSignal:
    out: MessageSignal = {}  # type: ignore[typeddict-item]
    if data.get("topicName") is not None:
        out["topic_name"] = data["topicName"]
    else:
        out["topic_name"] = ""
    if data.get("structuredMessage") is not None:
        import capo_iotfleetwise.types.structured_message

        out["structured_message"] = (
            capo_iotfleetwise.types.structured_message.deserialize_aws_json_1_0(
                data["structuredMessage"]
            )
        )
    else:
        import capo_iotfleetwise.types._unknown

        out["structured_message"] = capo_iotfleetwise.types._unknown.UnknownUnionMember(
            ""
        )
    return out
