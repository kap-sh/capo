"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateBandwidthRateLimitScheduleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.bandwidth_rate_limit_intervals
    import capo_storage_gateway.types.gateway_arn


class UpdateBandwidthRateLimitScheduleInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    bandwidth_rate_limit_intervals: "capo_storage_gateway.types.bandwidth_rate_limit_intervals.BandwidthRateLimitIntervals"
    """<p> An array containing bandwidth rate limit schedule intervals for a gateway. When no bandwidth rate limit intervals have been scheduled, the array is empty. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBandwidthRateLimitScheduleInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    import capo_storage_gateway.types.bandwidth_rate_limit_intervals

    out["BandwidthRateLimitIntervals"] = (
        capo_storage_gateway.types.bandwidth_rate_limit_intervals.serialize_aws_json_1_1(
            value["bandwidth_rate_limit_intervals"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBandwidthRateLimitScheduleInput:
    out: UpdateBandwidthRateLimitScheduleInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("BandwidthRateLimitIntervals") is not None:
        import capo_storage_gateway.types.bandwidth_rate_limit_intervals

        out["bandwidth_rate_limit_intervals"] = (
            capo_storage_gateway.types.bandwidth_rate_limit_intervals.deserialize_aws_json_1_1(
                data["BandwidthRateLimitIntervals"]
            )
        )
    else:
        out["bandwidth_rate_limit_intervals"] = []
    return out
