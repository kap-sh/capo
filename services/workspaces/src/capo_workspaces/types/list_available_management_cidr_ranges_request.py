"""Generated from Smithy shape ``com.amazonaws.workspaces#ListAvailableManagementCidrRangesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.management_cidr_range_constraint
    import capo_workspaces.types.management_cidr_range_max_results
    import capo_workspaces.types.pagination_token


class ListAvailableManagementCidrRangesRequest(TypedDict, closed=True):
    management_cidr_range_constraint: "capo_workspaces.types.management_cidr_range_constraint.ManagementCidrRangeConstraint"
    """<p>The IP address range to search. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block).</p>"""
    max_results: NotRequired[
        "capo_workspaces.types.management_cidr_range_max_results.ManagementCidrRangeMaxResults"
    ]
    """<p>The maximum number of items to return.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailableManagementCidrRangesRequest) -> dict:
    out: dict = {}
    out["ManagementCidrRangeConstraint"] = value["management_cidr_range_constraint"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailableManagementCidrRangesRequest:
    out: ListAvailableManagementCidrRangesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ManagementCidrRangeConstraint") is not None:
        out["management_cidr_range_constraint"] = data["ManagementCidrRangeConstraint"]
    else:
        out["management_cidr_range_constraint"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
