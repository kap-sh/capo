"""Generated from Smithy shape ``com.amazonaws.inspector#ListExclusionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.list_max_results
    import capo_inspector.types.pagination_token


class ListExclusionsRequest(TypedDict, closed=True):
    assessment_run_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment run that generated the exclusions that you want to list.</p>"""
    next_token: NotRequired["capo_inspector.types.pagination_token.PaginationToken"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListExclusionsRequest action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.</p>"""
    max_results: NotRequired["capo_inspector.types.list_max_results.ListMaxResults"]
    """<p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 100. The maximum value is 500.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExclusionsRequest) -> dict:
    out: dict = {}
    out["assessmentRunArn"] = value["assessment_run_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExclusionsRequest:
    out: ListExclusionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentRunArn") is not None:
        out["assessment_run_arn"] = data["assessmentRunArn"]
    else:
        out["assessment_run_arn"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
