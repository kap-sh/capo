"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeIpGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.workspaces_ip_groups_list


class DescribeIpGroupsResult(TypedDict, closed=True):
    result: NotRequired[
        "capo_workspaces.types.workspaces_ip_groups_list.WorkspacesIpGroupsList"
    ]
    """<p>Information about the IP access control groups.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIpGroupsResult) -> dict:
    out: dict = {}
    if "result" in value:
        import capo_workspaces.types.workspaces_ip_groups_list

        out["Result"] = (
            capo_workspaces.types.workspaces_ip_groups_list.serialize_aws_json_1_1(
                value["result"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIpGroupsResult:
    out: DescribeIpGroupsResult = {}  # type: ignore[typeddict-item]
    if data.get("Result") is not None:
        import capo_workspaces.types.workspaces_ip_groups_list

        out["result"] = (
            capo_workspaces.types.workspaces_ip_groups_list.deserialize_aws_json_1_1(
                data["Result"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeIpGroupsResult) -> dict:
    out: dict = {}
    if "result" in value:
        import capo_workspaces.types.workspaces_ip_groups_list

        out["Result"] = capo_workspaces.types.workspaces_ip_groups_list.serialize_cbor(
            value["result"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeIpGroupsResult:
    out: DescribeIpGroupsResult = {}  # type: ignore[typeddict-item]
    if data.get("Result") is not None:
        import capo_workspaces.types.workspaces_ip_groups_list

        out["result"] = (
            capo_workspaces.types.workspaces_ip_groups_list.deserialize_cbor(
                data["Result"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
