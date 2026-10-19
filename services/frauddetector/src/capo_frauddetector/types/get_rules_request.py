"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.rules_max_results
    import capo_frauddetector.types.string
    import capo_frauddetector.types.whole_number_version_string


class GetRulesRequest(TypedDict, closed=True):
    rule_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The rule ID.</p>"""
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The detector ID.</p>"""
    rule_version: NotRequired[
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p>The rule version.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next page token.</p>"""
    max_results: NotRequired[
        "capo_frauddetector.types.rules_max_results.RulesMaxResults"
    ]
    """<p>The maximum number of rules to return for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRulesRequest) -> dict:
    out: dict = {}
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    out["detectorId"] = value["detector_id"]
    if "rule_version" in value:
        out["ruleVersion"] = value["rule_version"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRulesRequest:
    out: GetRulesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    else:
        out["detector_id"] = ""
    if data.get("ruleVersion") is not None:
        out["rule_version"] = data["ruleVersion"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
