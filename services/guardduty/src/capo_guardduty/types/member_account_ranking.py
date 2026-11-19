"""Generated from Smithy shape ``com.amazonaws.guardduty#MemberAccountRanking``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.integer
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.risk_level
    import capo_guardduty.types.string


class MemberAccountRanking(TypedDict, closed=True):
    rank: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The position of the account in the ranking.</p>"""
    account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID of the member account.</p>"""
    finding_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of findings in the account.</p>"""
    risk_level: NotRequired["capo_guardduty.types.risk_level.RiskLevel"]
    """<p>The assessed risk level of the account. Possible values are <code>Info</code>, <code>Low</code>, <code>Medium</code>, <code>High</code>, and <code>Critical</code>.</p>"""
    risk_rationale: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>The reason for the assessed risk level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberAccountRanking) -> dict:
    out: dict = {}
    if "rank" in value:
        out["rank"] = value["rank"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "finding_count" in value:
        out["findingCount"] = value["finding_count"]
    if "risk_level" in value:
        import capo_guardduty.types.risk_level

        out["riskLevel"] = capo_guardduty.types.risk_level.serialize_json(
            value["risk_level"]
        )
    if "risk_rationale" in value:
        out["riskRationale"] = value["risk_rationale"]
    return out


def deserialize_json(data: dict) -> MemberAccountRanking:
    out: MemberAccountRanking = {}  # type: ignore[typeddict-item]
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("findingCount") is not None:
        out["finding_count"] = data["findingCount"]
    if data.get("riskLevel") is not None:
        import capo_guardduty.types.risk_level

        out["risk_level"] = capo_guardduty.types.risk_level.deserialize_json(
            data["riskLevel"]
        )
    if data.get("riskRationale") is not None:
        out["risk_rationale"] = data["riskRationale"]
    return out
