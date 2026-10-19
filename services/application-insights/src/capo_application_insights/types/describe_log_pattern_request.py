"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeLogPatternRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.log_pattern_name
    import capo_application_insights.types.log_pattern_set_name
    import capo_application_insights.types.resource_group_name


class DescribeLogPatternRequest(TypedDict, closed=True):
    resource_group_name: (
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    pattern_set_name: (
        "capo_application_insights.types.log_pattern_set_name.LogPatternSetName"
    )
    """<p>The name of the log pattern set.</p>"""
    pattern_name: "capo_application_insights.types.log_pattern_name.LogPatternName"
    """<p>The name of the log pattern.</p>"""
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLogPatternRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["PatternSetName"] = value["pattern_set_name"]
    out["PatternName"] = value["pattern_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLogPatternRequest:
    out: DescribeLogPatternRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        out["resource_group_name"] = ""
    if data.get("PatternSetName") is not None:
        out["pattern_set_name"] = data["PatternSetName"]
    else:
        out["pattern_set_name"] = ""
    if data.get("PatternName") is not None:
        out["pattern_name"] = data["PatternName"]
    else:
        out["pattern_name"] = ""
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
