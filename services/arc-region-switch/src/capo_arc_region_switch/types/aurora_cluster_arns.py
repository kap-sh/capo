"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AuroraClusterArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.aurora_cluster_arn

AuroraClusterArns: TypeAlias = list[
    "capo_arc_region_switch.types.aurora_cluster_arn.AuroraClusterArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AuroraClusterArns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AuroraClusterArns:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AuroraClusterArns) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AuroraClusterArns:
    return [item for item in data if item is not None]
