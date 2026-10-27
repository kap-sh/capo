"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.max_results
    import capo_sso_admin.types.region_scope
    import capo_sso_admin.types.token


class ListInstancesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_sso_admin.types.max_results.MaxResults"]
    """<p>The maximum number of results to display for the instance.</p>"""
    next_token: NotRequired["capo_sso_admin.types.token.Token"]
    """<p>The pagination token for the list API. Initially the value is null. Use the output of previous API calls to make subsequent calls.</p>"""
    region_scope: NotRequired["capo_sso_admin.types.region_scope.RegionScope"]
    """<p>Specifies which Amazon Web Services Regions to list IAM Identity Center instances from. Valid values:</p> <ul> <li> <p> <code>CURRENT_REGION</code> - Lists only the instances in the Region that you call this API from.</p> </li> <li> <p> <code>ALL_REGIONS</code> - Lists the instances that the caller owns or that are shared with the caller across all Regions.</p> </li> </ul> <p>If you don't specify a value, the default is <code>CURRENT_REGION</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInstancesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "region_scope" in value:
        import capo_sso_admin.types.region_scope

        out["RegionScope"] = capo_sso_admin.types.region_scope.serialize_aws_json_1_1(
            value["region_scope"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInstancesRequest:
    out: ListInstancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RegionScope") is not None:
        import capo_sso_admin.types.region_scope

        out["region_scope"] = (
            capo_sso_admin.types.region_scope.deserialize_aws_json_1_1(
                data["RegionScope"]
            )
        )
    return out
