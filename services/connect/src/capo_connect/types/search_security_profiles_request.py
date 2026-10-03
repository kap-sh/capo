"""Generated from Smithy shape ``com.amazonaws.connect#SearchSecurityProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.next_token2500
    import capo_connect.types.security_profile_search_criteria
    import capo_connect.types.security_profiles_search_filter


class SearchSecurityProfilesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""
    search_criteria: NotRequired[
        "capo_connect.types.security_profile_search_criteria.SecurityProfileSearchCriteria"
    ]
    """<p>The search criteria to be used to return security profiles. </p> <note> <p>The <code>name</code> field support "contains" queries with a minimum of 2 characters and maximum of 25 characters. Any queries with character lengths outside of this range will throw invalid results.</p> </note> <note> <p>The currently supported value for <code>FieldName</code>: <code>name</code> </p> </note>"""
    search_filter: NotRequired[
        "capo_connect.types.security_profiles_search_filter.SecurityProfilesSearchFilter"
    ]
    """<p>Filters to be applied to search results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSecurityProfilesRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "search_criteria" in value:
        import capo_connect.types.security_profile_search_criteria

        out["SearchCriteria"] = (
            capo_connect.types.security_profile_search_criteria.serialize_json(
                value["search_criteria"]
            )
        )
    if "search_filter" in value:
        import capo_connect.types.security_profiles_search_filter

        out["SearchFilter"] = (
            capo_connect.types.security_profiles_search_filter.serialize_json(
                value["search_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchSecurityProfilesRequest:
    out: SearchSecurityProfilesRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("SearchSecurityProfilesRequest.instance_id required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("SearchCriteria") is not None:
        import capo_connect.types.security_profile_search_criteria

        out["search_criteria"] = (
            capo_connect.types.security_profile_search_criteria.deserialize_json(
                data["SearchCriteria"]
            )
        )
    if data.get("SearchFilter") is not None:
        import capo_connect.types.security_profiles_search_filter

        out["search_filter"] = (
            capo_connect.types.security_profiles_search_filter.deserialize_json(
                data["SearchFilter"]
            )
        )
    return out
