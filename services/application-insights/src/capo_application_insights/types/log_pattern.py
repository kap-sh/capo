"""Generated from Smithy shape ``com.amazonaws.applicationinsights#LogPattern``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.log_pattern_name
    import capo_application_insights.types.log_pattern_rank
    import capo_application_insights.types.log_pattern_regex
    import capo_application_insights.types.log_pattern_set_name


class LogPattern(TypedDict, closed=True):
    pattern_set_name: NotRequired[
        "capo_application_insights.types.log_pattern_set_name.LogPatternSetName"
    ]
    """<p>The name of the log pattern. A log pattern name can contain as many as 30 characters, and it cannot be empty. The characters can be Unicode letters, digits, or one of the following symbols: period, dash, underscore.</p>"""
    pattern_name: NotRequired[
        "capo_application_insights.types.log_pattern_name.LogPatternName"
    ]
    """<p>The name of the log pattern. A log pattern name can contain as many as 50 characters, and it cannot be empty. The characters can be Unicode letters, digits, or one of the following symbols: period, dash, underscore.</p>"""
    pattern: NotRequired[
        "capo_application_insights.types.log_pattern_regex.LogPatternRegex"
    ]
    """<p>A regular expression that defines the log pattern. A log pattern can contain as many as 50 characters, and it cannot be empty. The pattern must be DFA compatible. Patterns that utilize forward lookahead or backreference constructions are not supported.</p>"""
    rank: "capo_application_insights.types.log_pattern_rank.LogPatternRank"
    """<p>Rank of the log pattern. Must be a value between <code>1</code> and <code>1,000,000</code>. The patterns are sorted by rank, so we recommend that you set your highest priority patterns with the lowest rank. A pattern of rank <code>1</code> will be the first to get matched to a log line. A pattern of rank <code>1,000,000</code> will be last to get matched. When you configure custom log patterns from the console, a <code>Low</code> severity pattern translates to a <code>750,000</code> rank. A <code>Medium</code> severity pattern translates to a <code>500,000</code> rank. And a <code>High</code> severity pattern translates to a <code>250,000</code> rank. Rank values less than <code>1</code> or greater than <code>1,000,000</code> are reserved for Amazon Web Services provided patterns. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogPattern) -> dict:
    out: dict = {}
    if "pattern_set_name" in value:
        out["PatternSetName"] = value["pattern_set_name"]
    if "pattern_name" in value:
        out["PatternName"] = value["pattern_name"]
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    out["Rank"] = value.get("rank", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> LogPattern:
    out: LogPattern = {}  # type: ignore[typeddict-item]
    if data.get("PatternSetName") is not None:
        out["pattern_set_name"] = data["PatternSetName"]
    if data.get("PatternName") is not None:
        out["pattern_name"] = data["PatternName"]
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    if data.get("Rank") is not None:
        out["rank"] = data["Rank"]
    else:
        out["rank"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LogPattern) -> dict:
    out: dict = {}
    if "pattern_set_name" in value:
        out["PatternSetName"] = value["pattern_set_name"]
    if "pattern_name" in value:
        out["PatternName"] = value["pattern_name"]
    if "pattern" in value:
        out["Pattern"] = value["pattern"]
    out["Rank"] = value.get("rank", 0)
    return out


def deserialize_cbor(data: dict) -> LogPattern:
    out: LogPattern = {}  # type: ignore[typeddict-item]
    if data.get("PatternSetName") is not None:
        out["pattern_set_name"] = data["PatternSetName"]
    if data.get("PatternName") is not None:
        out["pattern_name"] = data["PatternName"]
    if data.get("Pattern") is not None:
        out["pattern"] = data["Pattern"]
    if data.get("Rank") is not None:
        out["rank"] = data["Rank"]
    else:
        out["rank"] = 0
    return out
