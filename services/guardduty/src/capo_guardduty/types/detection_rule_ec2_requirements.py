"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectionRuleEc2Requirements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detection_rule_agent_version


class DetectionRuleEc2Requirements(TypedDict, closed=True):
    min_agent_version: NotRequired[
        "capo_guardduty.types.detection_rule_agent_version.DetectionRuleAgentVersion"
    ]
    """<p>The minimum GuardDuty agent version required to run the rule on Amazon EC2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectionRuleEc2Requirements) -> dict:
    out: dict = {}
    if "min_agent_version" in value:
        out["minAgentVersion"] = value["min_agent_version"]
    return out


def deserialize_json(data: dict) -> DetectionRuleEc2Requirements:
    out: DetectionRuleEc2Requirements = {}  # type: ignore[typeddict-item]
    if data.get("minAgentVersion") is not None:
        out["min_agent_version"] = data["minAgentVersion"]
    return out
