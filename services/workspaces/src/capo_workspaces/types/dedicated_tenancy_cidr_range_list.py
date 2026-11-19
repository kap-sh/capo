"""Generated from Smithy shape ``com.amazonaws.workspaces#DedicatedTenancyCidrRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.dedicated_tenancy_management_cidr_range

DedicatedTenancyCidrRangeList: TypeAlias = list[
    "capo_workspaces.types.dedicated_tenancy_management_cidr_range.DedicatedTenancyManagementCidrRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DedicatedTenancyCidrRangeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DedicatedTenancyCidrRangeList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DedicatedTenancyCidrRangeList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DedicatedTenancyCidrRangeList:
    return [item for item in data if item is not None]
