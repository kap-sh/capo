"""Generated from Smithy shape ``com.amazonaws.rekognition#ListProjectPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.extended_pagination_token
    import capo_rekognition.types.list_project_policies_page_size
    import capo_rekognition.types.project_arn


class ListProjectPoliciesRequest(TypedDict, closed=True):
    project_arn: "capo_rekognition.types.project_arn.ProjectArn"
    """<p>The ARN of the project for which you want to list the project policies.</p>"""
    next_token: NotRequired[
        "capo_rekognition.types.extended_pagination_token.ExtendedPaginationToken"
    ]
    """<p>If the previous response was incomplete (because there is more results to retrieve), Amazon Rekognition Custom Labels returns a pagination token in the response. You can use this pagination token to retrieve the next set of results. </p>"""
    max_results: NotRequired[
        "capo_rekognition.types.list_project_policies_page_size.ListProjectPoliciesPageSize"
    ]
    """<p>The maximum number of results to return per paginated call. The largest value you can specify is 5. If you specify a value greater than 5, a ValidationException error occurs. The default value is 5. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProjectPoliciesRequest) -> dict:
    out: dict = {}
    out["ProjectArn"] = value["project_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProjectPoliciesRequest:
    out: ListProjectPoliciesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProjectArn") is not None:
        out["project_arn"] = data["ProjectArn"]
    else:
        out["project_arn"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
