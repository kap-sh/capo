"""Generated from Smithy shape ``com.amazonaws.kinesis#ListStreamConsumersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.list_stream_consumers_input_limit
    import capo_kinesis.types.next_token
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.timestamp


class ListStreamConsumersInput(TypedDict, closed=True):
    stream_arn: "capo_kinesis.types.stream_arn.StreamARN"
    """<p>The ARN of the Kinesis data stream for which you want to list the registered consumers. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    next_token: NotRequired["capo_kinesis.types.next_token.NextToken"]
    """<p>When the number of consumers that are registered with the data stream is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of consumers that are registered with the data stream, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListStreamConsumers</code> to list the next set of registered consumers.</p> <p>Don't specify <code>StreamName</code> or <code>StreamCreationTimestamp</code> if you specify <code>NextToken</code> because the latter unambiguously identifies the stream.</p> <p>You can optionally specify a value for the <code>MaxResults</code> parameter when you specify <code>NextToken</code>. If you specify a <code>MaxResults</code> value that is less than the number of consumers that the operation returns if you don't specify <code>MaxResults</code>, the response will contain a new <code>NextToken</code> value. You can use the new <code>NextToken</code> value in a subsequent call to the <code>ListStreamConsumers</code> operation to list the next set of consumers.</p> <important> <p>Tokens expire after 300 seconds. When you obtain a value for <code>NextToken</code> in the response to a call to <code>ListStreamConsumers</code>, you have 300 seconds to use that value. If you specify an expired token in a call to <code>ListStreamConsumers</code>, you get <code>ExpiredNextTokenException</code>.</p> </important>"""
    max_results: NotRequired[
        "capo_kinesis.types.list_stream_consumers_input_limit.ListStreamConsumersInputLimit"
    ]
    """<p>The maximum number of consumers that you want a single call of <code>ListStreamConsumers</code> to return. The default value is 100. If you specify a value greater than 100, at most 100 results are returned. </p>"""
    stream_creation_timestamp: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>Specify this input parameter to distinguish data streams that have the same name. For example, if you create a data stream and then delete it, and you later create another data stream with the same name, you can use this input parameter to specify which of the two streams you want to list the consumers for. </p> <p>You can't specify this parameter if you specify the NextToken parameter. </p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStreamConsumersInput) -> dict:
    out: dict = {}
    out["StreamARN"] = value["stream_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "stream_creation_timestamp" in value:
        import capo_kinesis.types.timestamp

        out["StreamCreationTimestamp"] = (
            capo_kinesis.types.timestamp.serialize_aws_json_1_1(
                value["stream_creation_timestamp"]
            )
        )
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStreamConsumersInput:
    out: ListStreamConsumersInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    else:
        raise DeserializationError("ListStreamConsumersInput.stream_arn required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("StreamCreationTimestamp") is not None:
        import capo_kinesis.types.timestamp

        out["stream_creation_timestamp"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["StreamCreationTimestamp"]
            )
        )
    if data.get("StreamId") is not None:
        out["stream_id"] = data["StreamId"]
    return out
