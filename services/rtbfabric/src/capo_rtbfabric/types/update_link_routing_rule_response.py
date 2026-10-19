"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateLinkRoutingRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_rtbfabric.types.rule_id
    import capo_rtbfabric.types.rule_status


class UpdateLinkRoutingRuleResponse(TypedDict, closed=True):
    rule_id: "capo_rtbfabric.types.rule_id.RuleId"
    """<p>The unique identifier of the routing rule.</p>"""
    status: "capo_rtbfabric.types.rule_status.RuleStatus"
    """<p>The status of the routing rule.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp of when the routing rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkRoutingRuleResponse) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    import capo_rtbfabric.types.rule_status

    out["status"] = capo_rtbfabric.types.rule_status.serialize_json(value["status"])
    import capo_rtbfabric.types._prelude.timestamp

    out["updatedAt"] = capo_rtbfabric.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> UpdateLinkRoutingRuleResponse:
    out: UpdateLinkRoutingRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    else:
        out["rule_id"] = ""
    if data.get("status") is not None:
        import capo_rtbfabric.types.rule_status

        out["status"] = capo_rtbfabric.types.rule_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_rtbfabric.types.rule_status.RuleStatus", "")
    if data.get("updatedAt") is not None:
        import capo_rtbfabric.types._prelude.timestamp

        out["updated_at"] = capo_rtbfabric.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
