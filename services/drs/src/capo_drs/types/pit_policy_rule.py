"""Generated from Smithy shape ``com.amazonaws.drs#PITPolicyRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.pit_policy_rule_units
    import capo_drs.types.positive_integer
    import capo_drs.types.strictly_positive_integer


class PITPolicyRule(TypedDict, closed=True):
    rule_id: "capo_drs.types.positive_integer.PositiveInteger"
    """<p>The ID of the rule.</p>"""
    units: "capo_drs.types.pit_policy_rule_units.PITPolicyRuleUnits"
    """<p>The units used to measure the interval and retentionDuration.</p>"""
    interval: "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
    """<p>How often, in the chosen units, a snapshot should be taken.</p>"""
    retention_duration: (
        "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
    )
    """<p>The duration to retain a snapshot for, in the chosen units.</p>"""
    enabled: NotRequired["bool"]
    """<p>Whether this rule is enabled or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PITPolicyRule) -> dict:
    out: dict = {}
    out["ruleID"] = value.get("rule_id", 0)
    out["units"] = value["units"]
    out["interval"] = value["interval"]
    out["retentionDuration"] = value["retention_duration"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> PITPolicyRule:
    out: PITPolicyRule = {}  # type: ignore[typeddict-item]
    if data.get("ruleID") is not None:
        out["rule_id"] = data["ruleID"]
    else:
        out["rule_id"] = 0
    if data.get("units") is not None:
        out["units"] = data["units"]
    else:
        out["units"] = ""
    if data.get("interval") is not None:
        out["interval"] = data["interval"]
    else:
        out["interval"] = 0
    if data.get("retentionDuration") is not None:
        out["retention_duration"] = data["retentionDuration"]
    else:
        out["retention_duration"] = 0
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    return out
