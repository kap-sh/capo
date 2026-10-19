"""Generated from Smithy shape ``com.amazonaws.applicationinsights#UpdateLogPatternRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_insights.types.log_pattern_name
    import capo_application_insights.types.log_pattern_rank
    import capo_application_insights.types.log_pattern_regex
    import capo_application_insights.types.log_pattern_set_name
    import capo_application_insights.types.resource_group_name


class UpdateLogPatternRequest(TypedDict, closed=True):
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
    pattern: NotRequired[
        "capo_application_insights.types.log_pattern_regex.LogPatternRegex"
    ]
    """<p>The log pattern. The pattern must be DFA compatible. Patterns that utilize forward lookahead or backreference constructions are not supported.</p>"""
    rank: NotRequired["capo_application_insights.types.log_pattern_rank.LogPatternRank"]
    """<p>Rank of the log pattern. Must be a value between <code>1</code> and <code>1,000,000</code>. The patterns are sorted by rank, so we recommend that you set your highest priority patterns with the lowest rank. A pattern of rank <code>1</code> will be the first to get matched to a log line. A pattern of rank <code>1,000,000</code> will be last to get matched. When you configure custom log patterns from the console, a <code>Low</code> severity pattern translates to a <code>750,000</code> rank. A <code>Medium</code> severity pattern translates to a <code>500,000</code> rank. And a <code>High</code> severity pattern translates to a <code>250,000</code> rank. Rank values less than <code>1</code> or greater than <code>1,000,000</code> are reserved for Amazon Web Services provided patterns. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLogPatternRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["PatternSetName"] = value["pattern_set_name"]
    out["PatternName"] = value["pattern_name"]
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    if "rank" in value:
        out["Rank"] = value["rank"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLogPatternRequest:
    out: UpdateLogPatternRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        raise DeserializationError(
            "UpdateLogPatternRequest.resource_group_name required"
        )
    if data.get("PatternSetName") is not None:
        out["pattern_set_name"] = data["PatternSetName"]
    else:
        raise DeserializationError("UpdateLogPatternRequest.pattern_set_name required")
    if data.get("PatternName") is not None:
        out["pattern_name"] = data["PatternName"]
    else:
        raise DeserializationError("UpdateLogPatternRequest.pattern_name required")
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    if data.get("Rank") is not None:
        out["rank"] = data["Rank"]
    return out
