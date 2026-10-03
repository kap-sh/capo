"""Generated from Smithy shape ``com.amazonaws.personalize#ListCampaignsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.max_results
    import capo_personalize.types.next_token


class ListCampaignsRequest(TypedDict, closed=True):
    solution_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the solution to list the campaigns for. When a solution is not specified, all the campaigns associated with the account are listed.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token returned from the previous call to <a href="https://docs.aws.amazon.com/personalize/latest/dg/API_ListCampaigns.html">ListCampaigns</a> for getting the next set of campaigns (if they exist).</p>"""
    max_results: NotRequired["capo_personalize.types.max_results.MaxResults"]
    """<p>The maximum number of campaigns to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCampaignsRequest) -> dict:
    out: dict = {}
    if "solution_arn" in value:
        out["solutionArn"] = value["solution_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCampaignsRequest:
    out: ListCampaignsRequest = {}  # type: ignore[typeddict-item]
    if data.get("solutionArn") is not None:
        out["solution_arn"] = data["solutionArn"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
