"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkRoutingRuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_rtbfabric.types.rule_condition
    import capo_rtbfabric.types.rule_id
    import capo_rtbfabric.types.rule_priority
    import capo_rtbfabric.types.rule_status


class LinkRoutingRuleSummary(TypedDict, closed=True):
    rule_id: "capo_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""
    priority: "capo_rtbfabric.types.rule_priority.RulePriority"
    """<p>The priority of the routing rule.</p>"""
    conditions: "capo_rtbfabric.types.rule_condition.RuleCondition"
    """<p>The conditions for the routing rule.</p>"""
    status: "capo_rtbfabric.types.rule_status.RuleStatus"
    """<p>The status of the routing rule.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp of when the routing rule was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the routing rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkRoutingRuleSummary) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    out["priority"] = value["priority"]
    import capo_rtbfabric.types.rule_condition

    out["conditions"] = capo_rtbfabric.types.rule_condition.serialize_json(
        value["conditions"]
    )
    import capo_rtbfabric.types.rule_status

    out["status"] = capo_rtbfabric.types.rule_status.serialize_json(value["status"])
    import capo_rtbfabric.types._prelude.timestamp

    out["createdAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_rtbfabric.types._prelude.timestamp

    out["updatedAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> LinkRoutingRuleSummary:
    out: LinkRoutingRuleSummary = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    else:
        out["rule_id"] = ""
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
        raise DeserializationError("LinkRoutingRuleSummary.conditions required")
    if data.get("status") is not None:
        import capo_rtbfabric.types.rule_status

        out["status"] = capo_rtbfabric.types.rule_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_rtbfabric.types.rule_status.RuleStatus", "")
    if data.get("createdAt") is not None:
        import capo_rtbfabric.types._prelude.timestamp

        out["created_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_rtbfabric.types._prelude.timestamp

        out["updated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
