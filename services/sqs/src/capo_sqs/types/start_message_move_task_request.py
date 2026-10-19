"""Generated from Smithy shape ``com.amazonaws.sqs#StartMessageMoveTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.nullable_integer
    import capo_sqs.types.string


class StartMessageMoveTaskRequest(TypedDict, closed=True):
    source_arn: "capo_sqs.types.string.String"
    """<p>The ARN of the queue that contains the messages to be moved to another queue. Currently, only ARNs of dead-letter queues (DLQs) whose sources are other Amazon SQS queues are accepted. DLQs whose sources are non-SQS queues, such as Lambda or Amazon SNS topics, are not currently supported.</p>"""
    destination_arn: NotRequired["capo_sqs.types.string.String"]
    """<p>The ARN of the queue that receives the moved messages. You can use this field to specify the destination queue where you would like to redrive messages. If this field is left blank, the messages will be redriven back to their respective original source queues.</p>"""
    max_number_of_messages_per_second: NotRequired[
        "capo_sqs.types.nullable_integer.NullableInteger"
    ]
    """<p>The number of messages to be moved per second (the message movement rate). You can use this field to define a fixed message movement rate. The maximum value for messages per second is 500. If this field is left blank, the system will optimize the rate based on the queue message backlog size, which may vary throughout the duration of the message movement task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartMessageMoveTaskRequest) -> dict:
    out: dict = {}
    out["SourceArn"] = value["source_arn"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    if "max_number_of_messages_per_second" in value:
        out["MaxNumberOfMessagesPerSecond"] = value["max_number_of_messages_per_second"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartMessageMoveTaskRequest:
    out: StartMessageMoveTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    else:
        out["source_arn"] = ""
    if data.get("DestinationArn") is not None:
        out["destination_arn"] = data["DestinationArn"]
    if data.get("MaxNumberOfMessagesPerSecond") is not None:
        out["max_number_of_messages_per_second"] = data["MaxNumberOfMessagesPerSecond"]
    return out
