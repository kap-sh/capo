"""Generated from Smithy shape ``com.amazonaws.healthlake#ListDataTransformationProfileVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_next_token
    import capo_healthlake.types.max_results
    import capo_healthlake.types.profile_id_string


class ListDataTransformationProfileVersionsRequest(TypedDict, closed=True):
    profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString"
    """<p>The unique identifier of the profile whose versions to list.</p>"""
    max_results: NotRequired["capo_healthlake.types.max_results.MaxResults"]
    """<p>The maximum number of profile versions to return per page. If you don't specify a value, the service returns up to 100 results.</p>"""
    next_token: NotRequired[
        "capo_healthlake.types.data_transformation_next_token.DataTransformationNextToken"
    ]
    """<p>The pagination token from a previous response. Pass this value to retrieve the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDataTransformationProfileVersionsRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListDataTransformationProfileVersionsRequest:
    out: ListDataTransformationProfileVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
