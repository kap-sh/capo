"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.describe_workspaces_pools_filters
    import capo_workspaces.types.limit
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.workspaces_pool_ids


class DescribeWorkspacesPoolsRequest(TypedDict, closed=True):
    pool_ids: NotRequired["capo_workspaces.types.workspaces_pool_ids.WorkspacesPoolIds"]
    """<p>The identifier of the WorkSpaces Pools.</p>"""
    filters: NotRequired[
        "capo_workspaces.types.describe_workspaces_pools_filters.DescribeWorkspacesPoolsFilters"
    ]
    """<p>The filter conditions for the WorkSpaces Pool to return.</p>"""
    limit: NotRequired["capo_workspaces.types.limit.Limit"]
    """<p>The maximum number of items to return.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsRequest) -> dict:
    out: dict = {}
    if "pool_ids" in value:
        import capo_workspaces.types.workspaces_pool_ids

        out["PoolIds"] = (
            capo_workspaces.types.workspaces_pool_ids.serialize_aws_json_1_1(
                value["pool_ids"]
            )
        )
    if "filters" in value:
        import capo_workspaces.types.describe_workspaces_pools_filters

        out["Filters"] = (
            capo_workspaces.types.describe_workspaces_pools_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesPoolsRequest:
    out: DescribeWorkspacesPoolsRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolIds") is not None:
        import capo_workspaces.types.workspaces_pool_ids

        out["pool_ids"] = (
            capo_workspaces.types.workspaces_pool_ids.deserialize_aws_json_1_1(
                data["PoolIds"]
            )
        )
    if data.get("Filters") is not None:
        import capo_workspaces.types.describe_workspaces_pools_filters

        out["filters"] = (
            capo_workspaces.types.describe_workspaces_pools_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspacesPoolsRequest) -> dict:
    out: dict = {}
    if "pool_ids" in value:
        import capo_workspaces.types.workspaces_pool_ids

        out["PoolIds"] = capo_workspaces.types.workspaces_pool_ids.serialize_cbor(
            value["pool_ids"]
        )
    if "filters" in value:
        import capo_workspaces.types.describe_workspaces_pools_filters

        out["Filters"] = (
            capo_workspaces.types.describe_workspaces_pools_filters.serialize_cbor(
                value["filters"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspacesPoolsRequest:
    out: DescribeWorkspacesPoolsRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolIds") is not None:
        import capo_workspaces.types.workspaces_pool_ids

        out["pool_ids"] = capo_workspaces.types.workspaces_pool_ids.deserialize_cbor(
            data["PoolIds"]
        )
    if data.get("Filters") is not None:
        import capo_workspaces.types.describe_workspaces_pools_filters

        out["filters"] = (
            capo_workspaces.types.describe_workspaces_pools_filters.deserialize_cbor(
                data["Filters"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
