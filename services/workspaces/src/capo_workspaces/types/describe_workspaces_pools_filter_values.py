"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.describe_workspaces_pools_filter_value

DescribeWorkspacesPoolsFilterValues: TypeAlias = list[
    "capo_workspaces.types.describe_workspaces_pools_filter_value.DescribeWorkspacesPoolsFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DescribeWorkspacesPoolsFilterValues:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspacesPoolsFilterValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DescribeWorkspacesPoolsFilterValues:
    return [item for item in data if item is not None]
