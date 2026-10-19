"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateBandwidthRateLimitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.bandwidth_download_rate_limit
    import capo_storage_gateway.types.bandwidth_upload_rate_limit
    import capo_storage_gateway.types.gateway_arn


class UpdateBandwidthRateLimitInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    average_upload_rate_limit_in_bits_per_sec: NotRequired[
        "capo_storage_gateway.types.bandwidth_upload_rate_limit.BandwidthUploadRateLimit"
    ]
    """<p>The average upload bandwidth rate limit in bits per second.</p>"""
    average_download_rate_limit_in_bits_per_sec: NotRequired[
        "capo_storage_gateway.types.bandwidth_download_rate_limit.BandwidthDownloadRateLimit"
    ]
    """<p>The average download bandwidth rate limit in bits per second.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBandwidthRateLimitInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    if "average_upload_rate_limit_in_bits_per_sec" in value:
        out["AverageUploadRateLimitInBitsPerSec"] = value[
            "average_upload_rate_limit_in_bits_per_sec"
        ]
    if "average_download_rate_limit_in_bits_per_sec" in value:
        out["AverageDownloadRateLimitInBitsPerSec"] = value[
            "average_download_rate_limit_in_bits_per_sec"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBandwidthRateLimitInput:
    out: UpdateBandwidthRateLimitInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("AverageUploadRateLimitInBitsPerSec") is not None:
        out["average_upload_rate_limit_in_bits_per_sec"] = data[
            "AverageUploadRateLimitInBitsPerSec"
        ]
    if data.get("AverageDownloadRateLimitInBitsPerSec") is not None:
        out["average_download_rate_limit_in_bits_per_sec"] = data[
            "AverageDownloadRateLimitInBitsPerSec"
        ]
    return out
