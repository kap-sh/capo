"""Generated from Smithy shape ``com.amazonaws.kinesis#DeleteStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.boolean_object
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name


class DeleteStreamInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream to delete.</p>"""
    enforce_consumer_deletion: NotRequired[
        "capo_kinesis.types.boolean_object.BooleanObject"
    ]
    """<p>If this parameter is unset (<code>null</code>) or if you set it to <code>false</code>, and the stream has registered enhanced fan-out consumers, the call to <code>DeleteStream</code> fails with a <code>ResourceInUseException</code>.</p> <p>If you set it to <code>true</code>, <code>DeleteStream</code> deletes the stream and every consumer registered with it.</p> <p>This parameter does not apply to queues. A stream that has queues cannot be deleted until every queue on it is deleted with <a>DeleteQueue</a>, whatever this parameter is set to.</p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteStreamInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "enforce_consumer_deletion" in value:
        out["EnforceConsumerDeletion"] = value["enforce_consumer_deletion"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteStreamInput:
    out: DeleteStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("EnforceConsumerDeletion") is not None:
        out["enforce_consumer_deletion"] = data["EnforceConsumerDeletion"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    return out
