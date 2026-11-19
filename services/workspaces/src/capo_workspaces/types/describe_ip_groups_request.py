"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeIpGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.ip_group_id_list
    import capo_workspaces.types.limit
    import capo_workspaces.types.pagination_token


class DescribeIpGroupsRequest(TypedDict, closed=True):
    group_ids: NotRequired["capo_workspaces.types.ip_group_id_list.IpGroupIdList"]
    """<p>The identifiers of one or more IP access control groups.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""
    max_results: NotRequired["capo_workspaces.types.limit.Limit"]
    """<p>The maximum number of items to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIpGroupsRequest) -> dict:
    out: dict = {}
    if "group_ids" in value:
        import capo_workspaces.types.ip_group_id_list

        out["GroupIds"] = capo_workspaces.types.ip_group_id_list.serialize_aws_json_1_1(
            value["group_ids"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIpGroupsRequest:
    out: DescribeIpGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupIds") is not None:
        import capo_workspaces.types.ip_group_id_list

        out["group_ids"] = (
            capo_workspaces.types.ip_group_id_list.deserialize_aws_json_1_1(
                data["GroupIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeIpGroupsRequest) -> dict:
    out: dict = {}
    if "group_ids" in value:
        import capo_workspaces.types.ip_group_id_list

        out["GroupIds"] = capo_workspaces.types.ip_group_id_list.serialize_cbor(
            value["group_ids"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> DescribeIpGroupsRequest:
    out: DescribeIpGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupIds") is not None:
        import capo_workspaces.types.ip_group_id_list

        out["group_ids"] = capo_workspaces.types.ip_group_id_list.deserialize_cbor(
            data["GroupIds"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
