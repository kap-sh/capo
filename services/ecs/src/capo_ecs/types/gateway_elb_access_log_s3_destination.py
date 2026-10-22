"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayElbAccessLogS3Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class GatewayElbAccessLogS3Destination(TypedDict, closed=True):
    bucket: "capo_ecs.types.string.String"
    """<p>The name of the Amazon S3 bucket where access logs are delivered.</p>"""
    prefix: NotRequired["capo_ecs.types.string.String"]
    """<p>The object key prefix for the access logs in the Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayElbAccessLogS3Destination) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayElbAccessLogS3Destination:
    out: GatewayElbAccessLogS3Destination = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    return out
