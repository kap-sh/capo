"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteBandwidthRateLimitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.bandwidth_type
    import capo_storage_gateway.types.gateway_arn


class DeleteBandwidthRateLimitInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    bandwidth_type: "capo_storage_gateway.types.bandwidth_type.BandwidthType"
    """<p>One of the BandwidthType values that indicates the gateway bandwidth rate limit to delete.</p> <p>Valid Values: <code>UPLOAD</code> | <code>DOWNLOAD</code> | <code>ALL</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBandwidthRateLimitInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["BandwidthType"] = value["bandwidth_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBandwidthRateLimitInput:
    out: DeleteBandwidthRateLimitInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("BandwidthType") is not None:
        out["bandwidth_type"] = data["BandwidthType"]
    else:
        out["bandwidth_type"] = ""
    return out
