"""Generated from Smithy shape ``com.amazonaws.frauddetector#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.whole_number_version_string


class Rule(TypedDict, closed=True):
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The detector for which the rule is associated.</p>"""
    rule_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The rule ID.</p>"""
    rule_version: (
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    )
    """<p>The rule version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rule) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    out["ruleId"] = value["rule_id"]
    out["ruleVersion"] = value["rule_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    else:
        out["detector_id"] = ""
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    else:
        out["rule_id"] = ""
    if data.get("ruleVersion") is not None:
        out["rule_version"] = data["ruleVersion"]
    else:
        out["rule_version"] = ""
    return out
