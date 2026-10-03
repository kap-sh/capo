"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateGatewayInformationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.cloud_watch_log_group_arn
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.gateway_capacity
    import capo_storage_gateway.types.gateway_name
    import capo_storage_gateway.types.gateway_timezone


class UpdateGatewayInformationInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    gateway_name: NotRequired["capo_storage_gateway.types.gateway_name.GatewayName"]
    gateway_timezone: NotRequired[
        "capo_storage_gateway.types.gateway_timezone.GatewayTimezone"
    ]
    """<p>A value that indicates the time zone of the gateway.</p>"""
    cloud_watch_log_group_arn: NotRequired[
        "capo_storage_gateway.types.cloud_watch_log_group_arn.CloudWatchLogGroupARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that you want to use to monitor and log events in the gateway.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html">What is Amazon CloudWatch Logs?</a> </p>"""
    gateway_capacity: NotRequired[
        "capo_storage_gateway.types.gateway_capacity.GatewayCapacity"
    ]
    """<p>Specifies the size of the gateway's metadata cache. This setting impacts gateway performance and hardware recommendations. For more information, see <a href="https://docs.aws.amazon.com/filegateway/latest/files3/performance-multiple-file-shares.html">Performance guidance for gateways with multiple file shares</a> in the <i>Amazon S3 File Gateway User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGatewayInformationInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    if "gateway_name" in value:
        out["GatewayName"] = value["gateway_name"]
    if "gateway_timezone" in value:
        out["GatewayTimezone"] = value["gateway_timezone"]
    if "cloud_watch_log_group_arn" in value:
        out["CloudWatchLogGroupARN"] = value["cloud_watch_log_group_arn"]
    if "gateway_capacity" in value:
        import capo_storage_gateway.types.gateway_capacity

        out["GatewayCapacity"] = (
            capo_storage_gateway.types.gateway_capacity.serialize_aws_json_1_1(
                value["gateway_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGatewayInformationInput:
    out: UpdateGatewayInformationInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("UpdateGatewayInformationInput.gateway_arn required")
    if data.get("GatewayName") is not None:
        out["gateway_name"] = data["GatewayName"]
    if data.get("GatewayTimezone") is not None:
        out["gateway_timezone"] = data["GatewayTimezone"]
    if data.get("CloudWatchLogGroupARN") is not None:
        out["cloud_watch_log_group_arn"] = data["CloudWatchLogGroupARN"]
    if data.get("GatewayCapacity") is not None:
        import capo_storage_gateway.types.gateway_capacity

        out["gateway_capacity"] = (
            capo_storage_gateway.types.gateway_capacity.deserialize_aws_json_1_1(
                data["GatewayCapacity"]
            )
        )
    return out
