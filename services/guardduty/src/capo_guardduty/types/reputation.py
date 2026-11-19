"""Generated from Smithy shape ``com.amazonaws.guardduty#Reputation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class Reputation(TypedDict, closed=True):
    finding_time_disposition: NotRequired["capo_guardduty.types.string.String"]
    """<p>The reputation of the indicator at the time of the finding.</p>"""
    current_disposition: NotRequired["capo_guardduty.types.string.String"]
    """<p>The current reputation of the indicator.</p>"""
    reputation_comparison: NotRequired["capo_guardduty.types.string.String"]
    """<p>A comparison of the reputation at the time of the finding with the current reputation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Reputation) -> dict:
    out: dict = {}
    if "finding_time_disposition" in value:
        out["findingTimeDisposition"] = value["finding_time_disposition"]
    if "current_disposition" in value:
        out["currentDisposition"] = value["current_disposition"]
    if "reputation_comparison" in value:
        out["reputationComparison"] = value["reputation_comparison"]
    return out


def deserialize_json(data: dict) -> Reputation:
    out: Reputation = {}  # type: ignore[typeddict-item]
    if data.get("findingTimeDisposition") is not None:
        out["finding_time_disposition"] = data["findingTimeDisposition"]
    if data.get("currentDisposition") is not None:
        out["current_disposition"] = data["currentDisposition"]
    if data.get("reputationComparison") is not None:
        out["reputation_comparison"] = data["reputationComparison"]
    return out
