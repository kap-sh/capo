"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliveryDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.delivery_destination_configuration
    import capo_cloudwatch_logs.types.delivery_destination_name
    import capo_cloudwatch_logs.types.delivery_destination_type
    import capo_cloudwatch_logs.types.output_format
    import capo_cloudwatch_logs.types.tags


class DeliveryDestination(TypedDict, closed=True):
    name: NotRequired[
        "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName"
    ]
    """<p>The name of this delivery destination.</p>"""
    arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.</p>"""
    delivery_destination_type: NotRequired[
        "capo_cloudwatch_logs.types.delivery_destination_type.DeliveryDestinationType"
    ]
    """<p>Displays whether this delivery destination is CloudWatch Logs, Amazon S3, Firehose, or X-Ray.</p>"""
    output_format: NotRequired["capo_cloudwatch_logs.types.output_format.OutputFormat"]
    """<p>The format of the logs that are sent to this delivery destination. </p>"""
    delivery_destination_configuration: NotRequired[
        "capo_cloudwatch_logs.types.delivery_destination_configuration.DeliveryDestinationConfiguration"
    ]
    """<p>A structure that contains the ARN of the Amazon Web Services resource that will receive the logs.</p>"""
    role_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the IAM role that CloudWatch Logs assumes to deliver to this delivery destination. This field is present only for X-Ray trace delivery destinations that were created with a role.</p>"""
    tags: NotRequired["capo_cloudwatch_logs.types.tags.Tags"]
    """<p>The tags that have been assigned to this delivery destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryDestination) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "delivery_destination_type" in value:
        import capo_cloudwatch_logs.types.delivery_destination_type

        out["deliveryDestinationType"] = (
            capo_cloudwatch_logs.types.delivery_destination_type.serialize_aws_json_1_1(
                value["delivery_destination_type"]
            )
        )
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
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliveryDestination:
    out: DeliveryDestination = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("deliveryDestinationType") is not None:
        import capo_cloudwatch_logs.types.delivery_destination_type

        out["delivery_destination_type"] = (
            capo_cloudwatch_logs.types.delivery_destination_type.deserialize_aws_json_1_1(
                data["deliveryDestinationType"]
            )
        )
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
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("tags") is not None:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
