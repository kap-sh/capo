"""Generated from Smithy shape ``com.amazonaws.backupgateway#BandwidthRateLimitIntervals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup_gateway.types.bandwidth_rate_limit_interval

BandwidthRateLimitIntervals: TypeAlias = list[
    "capo_backup_gateway.types.bandwidth_rate_limit_interval.BandwidthRateLimitInterval"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BandwidthRateLimitIntervals) -> list:
    import capo_backup_gateway.types.bandwidth_rate_limit_interval

    out: list = []
    for item in value:
        out.append(
            capo_backup_gateway.types.bandwidth_rate_limit_interval.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BandwidthRateLimitIntervals:
    import capo_backup_gateway.types.bandwidth_rate_limit_interval

    out: BandwidthRateLimitIntervals = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_backup_gateway.types.bandwidth_rate_limit_interval.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BandwidthRateLimitIntervals) -> list:
    import capo_backup_gateway.types.bandwidth_rate_limit_interval

    out: list = []
    for item in value:
        out.append(
            capo_backup_gateway.types.bandwidth_rate_limit_interval.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> BandwidthRateLimitIntervals:
    import capo_backup_gateway.types.bandwidth_rate_limit_interval

    out: BandwidthRateLimitIntervals = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_backup_gateway.types.bandwidth_rate_limit_interval.deserialize_cbor(
                item
            )
        )
    return out
