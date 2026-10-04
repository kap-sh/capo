"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutDeliveryDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.delivery_destination_configuration
    import capo_cloudwatch_logs.types.delivery_destination_name
    import capo_cloudwatch_logs.types.delivery_destination_type
    import capo_cloudwatch_logs.types.output_format
    import capo_cloudwatch_logs.types.tags


class PutDeliveryDestinationRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName"
    """<p>A name for this delivery destination. This name must be unique for all delivery destinations in your account.</p>"""
    output_format: NotRequired["capo_cloudwatch_logs.types.output_format.OutputFormat"]
    """<p>The format for the logs that this delivery destination will receive.</p>"""
    delivery_destination_configuration: NotRequired[
        "capo_cloudwatch_logs.types.delivery_destination_configuration.DeliveryDestinationConfiguration"
    ]
    """<p>A structure that contains the ARN of the Amazon Web Services resource that will receive the logs.</p> <note> <p> <code>deliveryDestinationConfiguration</code> is required for CloudWatch Logs, Amazon S3, Firehose log delivery destinations and not required for X-Ray trace delivery destinations. <code>deliveryDestinationType</code> is needed for X-Ray trace delivery destinations but not required for other logs delivery destinations.</p> </note>"""
    delivery_destination_type: NotRequired[
        "capo_cloudwatch_logs.types.delivery_destination_type.DeliveryDestinationType"
    ]
    """<p>The type of delivery destination. This parameter specifies the target service where log data will be delivered. Valid values include:</p> <ul> <li> <p> <code>S3</code> - Amazon S3 for long-term storage and analytics</p> </li> <li> <p> <code>CWL</code> - CloudWatch Logs for centralized log management</p> </li> <li> <p> <code>FH</code> - Amazon Kinesis Data Firehose for real-time data streaming</p> </li> <li> <p> <code>XRAY</code> - Amazon Web Services X-Ray for distributed tracing and application monitoring</p> </li> </ul> <p>The delivery destination type determines the format and configuration options available for log delivery.</p>"""
    role_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of an IAM role in your account that CloudWatch Logs assumes to deliver to this delivery destination. The trust policy of the role must allow CloudWatch Logs to assume it. This parameter is supported only for X-Ray trace delivery destinations.</p>"""
    tags: NotRequired["capo_cloudwatch_logs.types.tags.Tags"]
    """<p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDeliveryDestinationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "output_format" in value:
        import capo_cloudwatch_logs.types.output_format

        out["outputFormat"] = (
            capo_cloudwatch_logs.types.output_format.serialize_aws_json_1_1(
                value["output_format"]
            )
        )
    if "delivery_destination_configuration" in value:
        import capo_cloudwatch_logs.types.delivery_destination_configuration

        out["deliveryDestinationConfiguration"] = (
            capo_cloudwatch_logs.types.delivery_destination_configuration.serialize_aws_json_1_1(
                value["delivery_destination_configuration"]
            )
        )
    if "delivery_destination_type" in value:
        import capo_cloudwatch_logs.types.delivery_destination_type

        out["deliveryDestinationType"] = (
            capo_cloudwatch_logs.types.delivery_destination_type.serialize_aws_json_1_1(
                value["delivery_destination_type"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDeliveryDestinationRequest:
    out: PutDeliveryDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PutDeliveryDestinationRequest.name required")
    if data.get("outputFormat") is not None:
        import capo_cloudwatch_logs.types.output_format

        out["output_format"] = (
            capo_cloudwatch_logs.types.output_format.deserialize_aws_json_1_1(
                data["outputFormat"]
            )
        )
    if data.get("deliveryDestinationConfiguration") is not None:
        import capo_cloudwatch_logs.types.delivery_destination_configuration

        out["delivery_destination_configuration"] = (
            capo_cloudwatch_logs.types.delivery_destination_configuration.deserialize_aws_json_1_1(
                data["deliveryDestinationConfiguration"]
            )
        )
    if data.get("deliveryDestinationType") is not None:
        import capo_cloudwatch_logs.types.delivery_destination_type

        out["delivery_destination_type"] = (
            capo_cloudwatch_logs.types.delivery_destination_type.deserialize_aws_json_1_1(
                data["deliveryDestinationType"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("tags") is not None:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
