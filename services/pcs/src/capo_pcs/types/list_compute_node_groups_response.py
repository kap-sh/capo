"""Generated from Smithy shape ``com.amazonaws.pcs#ListComputeNodeGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.compute_node_group_list


class ListComputeNodeGroupsResponse(TypedDict, closed=True):
    compute_node_groups: "capo_pcs.types.compute_node_group_list.ComputeNodeGroupList"
    """<p>The list of compute node groups for the cluster.</p>"""
    next_token: NotRequired["str"]
    """<p>The value of <code>nextToken</code> is a unique pagination token for each page of results returned. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token returns an <code>HTTP 400 InvalidToken</code> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListComputeNodeGroupsResponse) -> dict:
    out: dict = {}
    import capo_pcs.types.compute_node_group_list

    out["computeNodeGroups"] = (
        capo_pcs.types.compute_node_group_list.serialize_aws_json_1_0(
            value["compute_node_groups"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListComputeNodeGroupsResponse:
    out: ListComputeNodeGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("computeNodeGroups") is not None:
        import capo_pcs.types.compute_node_group_list

        out["compute_node_groups"] = (
            capo_pcs.types.compute_node_group_list.deserialize_aws_json_1_0(
                data["computeNodeGroups"]
            )
        )
    else:
        out["compute_node_groups"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
