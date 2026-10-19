"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSessionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_rule_details
    import capo_inspector2.types.cis_rule_status
    import capo_inspector2.types.rule_id


class CisSessionMessage(TypedDict, closed=True):
    rule_id: "capo_inspector2.types.rule_id.RuleId"
    """<p>The rule ID for the CIS session message.</p>"""
    status: "capo_inspector2.types.cis_rule_status.CisRuleStatus"
    """<p>The status of the CIS session message.</p>"""
    cis_rule_details: "capo_inspector2.types.cis_rule_details.CisRuleDetails"
    """<p>The CIS rule details for the CIS session message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CisSessionMessage) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    import capo_inspector2.types.cis_rule_status

    out["status"] = capo_inspector2.types.cis_rule_status.serialize_json(
        value["status"]
    )
    import capo_inspector2.types.cis_rule_details

    out["cisRuleDetails"] = capo_inspector2.types.cis_rule_details.serialize_json(
        value["cis_rule_details"]
    )
    return out


def deserialize_json(data: dict) -> CisSessionMessage:
    out: CisSessionMessage = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    else:
        out["rule_id"] = ""
    if data.get("status") is not None:
        import capo_inspector2.types.cis_rule_status

        out["status"] = capo_inspector2.types.cis_rule_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_inspector2.types.cis_rule_status.CisRuleStatus", ""
        )
    if data.get("cisRuleDetails") is not None:
        import capo_inspector2.types.cis_rule_details

        out["cis_rule_details"] = (
            capo_inspector2.types.cis_rule_details.deserialize_json(
                data["cisRuleDetails"]
            )
        )
    else:
        out["cis_rule_details"] = b""
    return out
