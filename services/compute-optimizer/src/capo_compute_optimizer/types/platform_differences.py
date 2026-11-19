"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PlatformDifferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.platform_difference

PlatformDifferences: TypeAlias = list[
    "capo_compute_optimizer.types.platform_difference.PlatformDifference"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PlatformDifferences) -> list:
    import capo_compute_optimizer.types.platform_difference

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.platform_difference.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PlatformDifferences:
    import capo_compute_optimizer.types.platform_difference

    out: PlatformDifferences = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.platform_difference.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlatformDifferences) -> list:
    import capo_compute_optimizer.types.platform_difference

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.platform_difference.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PlatformDifferences:
    import capo_compute_optimizer.types.platform_difference

    out: PlatformDifferences = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.platform_difference.deserialize_cbor(item)
        )
    return out
