"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InputLambdaProcessorUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.resource_arn


class InputLambdaProcessorUpdate(TypedDict, closed=True):
    resource_arn_update: "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the new Amazon Lambda function that is used to preprocess the records in the stream.</p> <note> <p>To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda">Example ARNs: Amazon Lambda</a> </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputLambdaProcessorUpdate) -> dict:
    out: dict = {}
    out["ResourceARNUpdate"] = value["resource_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputLambdaProcessorUpdate:
    out: InputLambdaProcessorUpdate = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARNUpdate") is not None:
        out["resource_arn_update"] = data["ResourceARNUpdate"]
    else:
        raise DeserializationError(
            "InputLambdaProcessorUpdate.resource_arn_update required"
        )
    return out
