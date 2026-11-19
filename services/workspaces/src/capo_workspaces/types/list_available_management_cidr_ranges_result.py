"""Generated from Smithy shape ``com.amazonaws.workspaces#ListAvailableManagementCidrRangesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.dedicated_tenancy_cidr_range_list
    import capo_workspaces.types.pagination_token


class ListAvailableManagementCidrRangesResult(TypedDict, closed=True):
    management_cidr_ranges: NotRequired[
        "capo_workspaces.types.dedicated_tenancy_cidr_range_list.DedicatedTenancyCidrRangeList"
    ]
    """<p>The list of available IP address ranges, specified as IPv4 CIDR blocks.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailableManagementCidrRangesResult) -> dict:
    out: dict = {}
    if "management_cidr_ranges" in value:
        import capo_workspaces.types.dedicated_tenancy_cidr_range_list

        out["ManagementCidrRanges"] = (
            capo_workspaces.types.dedicated_tenancy_cidr_range_list.serialize_aws_json_1_1(
                value["management_cidr_ranges"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailableManagementCidrRangesResult:
    out: ListAvailableManagementCidrRangesResult = {}  # type: ignore[typeddict-item]
    if data.get("ManagementCidrRanges") is not None:
        import capo_workspaces.types.dedicated_tenancy_cidr_range_list

        out["management_cidr_ranges"] = (
            capo_workspaces.types.dedicated_tenancy_cidr_range_list.deserialize_aws_json_1_1(
                data["ManagementCidrRanges"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAvailableManagementCidrRangesResult) -> dict:
    out: dict = {}
    if "management_cidr_ranges" in value:
        import capo_workspaces.types.dedicated_tenancy_cidr_range_list

        out["ManagementCidrRanges"] = (
            capo_workspaces.types.dedicated_tenancy_cidr_range_list.serialize_cbor(
                value["management_cidr_ranges"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAvailableManagementCidrRangesResult:
    out: ListAvailableManagementCidrRangesResult = {}  # type: ignore[typeddict-item]
    if data.get("ManagementCidrRanges") is not None:
        import capo_workspaces.types.dedicated_tenancy_cidr_range_list

        out["management_cidr_ranges"] = (
            capo_workspaces.types.dedicated_tenancy_cidr_range_list.deserialize_cbor(
                data["ManagementCidrRanges"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
