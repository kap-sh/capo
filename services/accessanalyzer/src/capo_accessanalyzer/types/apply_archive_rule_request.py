"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ApplyArchiveRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.name


class ApplyArchiveRuleRequest(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The Amazon resource name (ARN) of the analyzer.</p>"""
    rule_name: "capo_accessanalyzer.types.name.Name"
    """<p>The name of the rule to apply.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplyArchiveRuleRequest) -> dict:
    out: dict = {}
    out["analyzerArn"] = value["analyzer_arn"]
    out["ruleName"] = value["rule_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ApplyArchiveRuleRequest:
    out: ApplyArchiveRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("analyzerArn") is not None:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        out["analyzer_arn"] = ""
    if data.get("ruleName") is not None:
        out["rule_name"] = data["ruleName"]
    else:
        out["rule_name"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
