"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateLinkRoutingRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.link_id
    import capo_rtbfabric.types.rule_condition
    import capo_rtbfabric.types.rule_id
    import capo_rtbfabric.types.rule_priority


class UpdateLinkRoutingRuleRequest(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    rule_id: "capo_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""
    priority: "capo_rtbfabric.types.rule_priority.RulePriority"
    """<p>The updated priority of the routing rule. Lower numbers are evaluated first. Valid values are 1 to 1000. Priority must be unique among non-deleted rules within a link.</p>"""
    conditions: "capo_rtbfabric.types.rule_condition.RuleCondition"
    """<p>The updated conditions for the routing rule. All specified fields must match for the rule to apply. At least one condition field must be set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkRoutingRuleRequest) -> dict:
    out: dict = {}
    out["priority"] = value["priority"]
    import capo_rtbfabric.types.rule_condition

    out["conditions"] = capo_rtbfabric.types.rule_condition.serialize_json(
        value["conditions"]
    )
    return out


def deserialize_json(data: dict) -> UpdateLinkRoutingRuleRequest:
    out: UpdateLinkRoutingRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        out["priority"] = 0
    if data.get("conditions") is not None:
        import capo_rtbfabric.types.rule_condition

        out["conditions"] = capo_rtbfabric.types.rule_condition.deserialize_json(
            data["conditions"]
        )
    else:
        raise DeserializationError("UpdateLinkRoutingRuleRequest.conditions required")
    return out
