"""Generated from Smithy shape ``com.amazonaws.lambda#ListEventSourceMappingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.arn
    import capo_lambda.types.max_list_items
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.string


class ListEventSourceMappingsRequest(TypedDict, closed=True):
    event_source_arn: NotRequired["capo_lambda.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the event source.</p> <ul> <li> <p> <b>Amazon Kinesis</b> – The ARN of the data stream or a stream consumer.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – The ARN of the stream.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – The ARN of the queue.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – The ARN of the cluster or the ARN of the VPC connection (for <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#msk-multi-vpc">cross-account event source mappings</a>).</p> </li> <li> <p> <b>Amazon MQ</b> – The ARN of the broker.</p> </li> <li> <p> <b>Amazon DocumentDB</b> – The ARN of the DocumentDB change stream.</p> </li> </ul>"""
    function_name: NotRequired[
        "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    ]
    """<p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>"""
    marker: NotRequired["capo_lambda.types.string.String"]
    """<p>A pagination token returned by a previous call.</p>"""
    max_items: NotRequired["capo_lambda.types.max_list_items.MaxListItems"]
    """<p>The maximum number of event source mappings to return. Note that ListEventSourceMappings returns a maximum of 100 items in each response, even if you set the number higher.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventSourceMappingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEventSourceMappingsRequest:
    out: ListEventSourceMappingsRequest = {}  # type: ignore[typeddict-item]
    return out
