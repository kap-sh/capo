"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListLogPatternsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.log_pattern_set_name
    import capo_application_insights.types.max_entities
    import capo_application_insights.types.pagination_token
    import capo_application_insights.types.resource_group_name


class ListLogPatternsRequest(TypedDict, closed=True):
    resource_group_name: (
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    pattern_set_name: NotRequired[
        "capo_application_insights.types.log_pattern_set_name.LogPatternSetName"
    ]
    """<p>The name of the log pattern set.</p>"""
    max_results: NotRequired["capo_application_insights.types.max_entities.MaxEntities"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>"""
    next_token: NotRequired[
        "capo_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The token to request the next page of results.</p>"""
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLogPatternsRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    if "pattern_set_name" in value:
        out["PatternSetName"] = value["pattern_set_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLogPatternsRequest:
    out: ListLogPatternsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        out["resource_group_name"] = ""
    if data.get("PatternSetName") is not None:
        out["pattern_set_name"] = data["PatternSetName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
