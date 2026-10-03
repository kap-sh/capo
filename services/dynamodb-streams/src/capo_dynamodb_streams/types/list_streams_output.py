"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#ListStreamsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.stream_arn
    import capo_dynamodb_streams.types.stream_list


class ListStreamsOutput(TypedDict, closed=True):
    streams: NotRequired["capo_dynamodb_streams.types.stream_list.StreamList"]
    """<p>A list of stream descriptors associated with the current account and endpoint.</p>"""
    last_evaluated_stream_arn: NotRequired[
        "capo_dynamodb_streams.types.stream_arn.StreamArn"
    ]
    """<p>The stream ARN of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request.</p> <p>If <code>LastEvaluatedStreamArn</code> is empty, then the "last page" of results has been processed and there is no more data to be retrieved.</p> <p>If <code>LastEvaluatedStreamArn</code> is not empty, it does not necessarily mean that there is more data in the result set. The only way to know when you have reached the end of the result set is when <code>LastEvaluatedStreamArn</code> is empty.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListStreamsOutput) -> dict:
    out: dict = {}
    if "streams" in value:
        import capo_dynamodb_streams.types.stream_list

        out["Streams"] = capo_dynamodb_streams.types.stream_list.serialize_aws_json_1_0(
            value["streams"]
        )
    if "last_evaluated_stream_arn" in value:
        out["LastEvaluatedStreamArn"] = value["last_evaluated_stream_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListStreamsOutput:
    out: ListStreamsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Streams") is not None:
        import capo_dynamodb_streams.types.stream_list

        out["streams"] = (
            capo_dynamodb_streams.types.stream_list.deserialize_aws_json_1_0(
                data["Streams"]
            )
        )
    if data.get("LastEvaluatedStreamArn") is not None:
        out["last_evaluated_stream_arn"] = data["LastEvaluatedStreamArn"]
    return out
