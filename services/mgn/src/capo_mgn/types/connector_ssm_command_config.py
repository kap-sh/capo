"""Generated from Smithy shape ``com.amazonaws.mgn#ConnectorSsmCommandConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.cloud_watch_log_group_name
    import capo_mgn.types.s3_bucket_name


class ConnectorSsmCommandConfig(TypedDict, closed=True):
    s3_output_enabled: "bool"
    """<p>Connector SSM command config S3 output enabled.</p>"""
    output_s3_bucket_name: NotRequired["capo_mgn.types.s3_bucket_name.S3BucketName"]
    """<p>Connector SSM command config output S3 bucket name.</p>"""
    cloud_watch_output_enabled: "bool"
    """<p>Connector SSM command config CloudWatch output enabled.</p>"""
    cloud_watch_log_group_name: NotRequired[
        "capo_mgn.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
    ]
    """<p>Connector SSM command config CloudWatch log group name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorSsmCommandConfig) -> dict:
    out: dict = {}
    out["s3OutputEnabled"] = value["s3_output_enabled"]
    if "output_s3_bucket_name" in value:
        out["outputS3BucketName"] = value["output_s3_bucket_name"]
    out["cloudWatchOutputEnabled"] = value["cloud_watch_output_enabled"]
    if "cloud_watch_log_group_name" in value:
        out["cloudWatchLogGroupName"] = value["cloud_watch_log_group_name"]
    return out


def deserialize_json(data: dict) -> ConnectorSsmCommandConfig:
    out: ConnectorSsmCommandConfig = {}  # type: ignore[typeddict-item]
    if data.get("s3OutputEnabled") is not None:
        out["s3_output_enabled"] = data["s3OutputEnabled"]
    else:
        out["s3_output_enabled"] = False
    if data.get("outputS3BucketName") is not None:
        out["output_s3_bucket_name"] = data["outputS3BucketName"]
    if data.get("cloudWatchOutputEnabled") is not None:
        out["cloud_watch_output_enabled"] = data["cloudWatchOutputEnabled"]
    else:
        out["cloud_watch_output_enabled"] = False
    if data.get("cloudWatchLogGroupName") is not None:
        out["cloud_watch_log_group_name"] = data["cloudWatchLogGroupName"]
    return out
