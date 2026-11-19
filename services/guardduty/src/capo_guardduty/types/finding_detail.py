"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.activity_window
    import capo_guardduty.types.finding_id
    import capo_guardduty.types.finding_type
    import capo_guardduty.types.string


class FindingDetail(TypedDict, closed=True):
    finding_id: NotRequired["capo_guardduty.types.finding_id.FindingId"]
    """<p>The ID of the finding.</p>"""
    finding_type: NotRequired["capo_guardduty.types.finding_type.FindingType"]
    """<p>The type of the finding.</p>"""
    severity: NotRequired["capo_guardduty.types.string.String"]
    """<p>The severity of the finding.</p>"""
    account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the Amazon Web Services account in which the finding was generated.</p>"""
    region: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services Region in which the finding was generated.</p>"""
    activity_window: NotRequired["capo_guardduty.types.activity_window.ActivityWindow"]
    """<p>The time range of the activity that the finding describes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingDetail) -> dict:
    out: dict = {}
    if "finding_id" in value:
        out["findingId"] = value["finding_id"]
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "severity" in value:
        out["severity"] = value["severity"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "activity_window" in value:
        import capo_guardduty.types.activity_window

        out["activityWindow"] = capo_guardduty.types.activity_window.serialize_json(
            value["activity_window"]
        )
    return out


def deserialize_json(data: dict) -> FindingDetail:
    out: FindingDetail = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    if data.get("severity") is not None:
        out["severity"] = data["severity"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("activityWindow") is not None:
        import capo_guardduty.types.activity_window

        out["activity_window"] = capo_guardduty.types.activity_window.deserialize_json(
            data["activityWindow"]
        )
    return out
