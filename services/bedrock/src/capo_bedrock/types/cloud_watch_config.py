"""Generated from Smithy shape ``com.amazonaws.bedrock#CloudWatchConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.log_group_name
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.s3_config


class CloudWatchConfig(TypedDict, closed=True):
    log_group_name: "capo_bedrock.types.log_group_name.LogGroupName"
    """<p>The log group name.</p>"""
    role_arn: "capo_bedrock.types.role_arn.RoleArn"
    """<p>The role Amazon Resource Name (ARN).</p>"""
    large_data_delivery_s3_config: NotRequired["capo_bedrock.types.s3_config.S3Config"]
    """<p>S3 configuration for delivering a large amount of data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchConfig) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    out["roleArn"] = value["role_arn"]
    if "large_data_delivery_s3_config" in value:
        import capo_bedrock.types.s3_config

        out["largeDataDeliveryS3Config"] = capo_bedrock.types.s3_config.serialize_json(
            value["large_data_delivery_s3_config"]
        )
    return out


def deserialize_json(data: dict) -> CloudWatchConfig:
    out: CloudWatchConfig = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        out["log_group_name"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("largeDataDeliveryS3Config") is not None:
        import capo_bedrock.types.s3_config

        out["large_data_delivery_s3_config"] = (
            capo_bedrock.types.s3_config.deserialize_json(
                data["largeDataDeliveryS3Config"]
            )
        )
    return out
