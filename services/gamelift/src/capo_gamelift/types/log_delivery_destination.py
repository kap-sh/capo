"""Generated from Smithy shape ``com.amazonaws.gamelift#LogDeliveryDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.delivery_destination_arn_string_model
    import capo_gamelift.types.log_delivery_destination_type


class LogDeliveryDestination(TypedDict, closed=True):
    log_destination: NotRequired[
        "capo_gamelift.types.log_delivery_destination_type.LogDeliveryDestinationType"
    ]
    """<p>The type of Amazon Web Services resource that receives the game session placement insight logs. This value is required. Valid values are:</p> <ul> <li> <p> <code>CLOUDWATCH</code> -- an Amazon CloudWatch Logs log group.</p> </li> <li> <p> <code>S3</code> -- an Amazon S3 bucket.</p> </li> <li> <p> <code>FIREHOSE</code> -- an Amazon Data Firehose delivery stream.</p> </li> </ul>"""
    destination_arn: NotRequired[
        "capo_gamelift.types.delivery_destination_arn_string_model.DeliveryDestinationArnStringModel"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource that receives the game session placement insight logs. This resource must match the type that you specify in <code>LogDestination</code>. This value is required for <code>FIREHOSE</code> destinations. For <code>CLOUDWATCH</code> and <code>S3</code>, you can omit this value; Amazon GameLift Servers then creates a destination resource of the specified type on your behalf.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogDeliveryDestination) -> dict:
    out: dict = {}
    if "log_destination" in value:
        import capo_gamelift.types.log_delivery_destination_type

        out["LogDestination"] = (
            capo_gamelift.types.log_delivery_destination_type.serialize_aws_json_1_1(
                value["log_destination"]
            )
        )
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LogDeliveryDestination:
    out: LogDeliveryDestination = {}  # type: ignore[typeddict-item]
    if data.get("LogDestination") is not None:
        import capo_gamelift.types.log_delivery_destination_type

        out["log_destination"] = (
            capo_gamelift.types.log_delivery_destination_type.deserialize_aws_json_1_1(
                data["LogDestination"]
            )
        )
    if data.get("DestinationArn") is not None:
        out["destination_arn"] = data["DestinationArn"]
    return out
