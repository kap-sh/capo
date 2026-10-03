"""Generated from Smithy shape ``com.amazonaws.lambda#OnFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.destination_arn


class OnFailure(TypedDict, closed=True):
    destination: NotRequired["capo_lambda.types.destination_arn.DestinationArn"]
    """<p>The Amazon Resource Name (ARN) of the destination resource.</p> <p>To retain records of failed invocations from <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html">Kinesis</a>, <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html">DynamoDB</a>, <a href="https://docs.aws.amazon.com/lambda/latest/dg/kafka-on-failure.html">self-managed Apache Kafka</a>, or <a href="https://docs.aws.amazon.com/lambda/latest/dg/kafka-on-failure.html">Amazon MSK</a>, you can configure an Amazon SNS topic, Amazon SQS queue, Amazon S3 bucket, or Kafka topic as the destination.</p> <note> <p>Amazon SNS destinations have a message size limit of 256 KB. If the combined size of the function request and response payload exceeds the limit, Lambda will drop the payload when sending <code>OnFailure</code> event to the destination. For details on this behavior, refer to <a href="https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html">Retaining records of asynchronous invocations</a>.</p> </note> <p>To retain records of failed invocations from <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html">Kinesis</a>, <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html">DynamoDB</a>, <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-smaa-onfailure-destination">self-managed Kafka</a> or <a href="https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-onfailure-destination">Amazon MSK</a>, you can configure an Amazon SNS topic, Amazon SQS queue, or Amazon S3 bucket as the destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnFailure) -> dict:
    out: dict = {}
    if "destination" in value:
        out["Destination"] = value["destination"]
    return out


def deserialize_json(data: dict) -> OnFailure:
    out: OnFailure = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    return out
