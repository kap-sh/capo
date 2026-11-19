"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.describe_workspaces_pools_filter

DescribeWorkspacesPoolsFilters: TypeAlias = list[
    "capo_workspaces.types.describe_workspaces_pools_filter.DescribeWorkspacesPoolsFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsFilters) -> list:
    import capo_workspaces.types.describe_workspaces_pools_filter

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.describe_workspaces_pools_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DescribeWorkspacesPoolsFilters:
    import capo_workspaces.types.describe_workspaces_pools_filter

    out: DescribeWorkspacesPoolsFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.describe_workspaces_pools_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspacesPoolsFilters) -> list:
    import capo_workspaces.types.describe_workspaces_pools_filter

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.describe_workspaces_pools_filter.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> DescribeWorkspacesPoolsFilters:
    import capo_workspaces.types.describe_workspaces_pools_filter

    out: DescribeWorkspacesPoolsFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces.types.describe_workspaces_pools_filter.deserialize_cbor(
                item
            )
        )
    return out
