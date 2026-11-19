"""Generated from Smithy shape ``com.amazonaws.guardduty#RdsLoginActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.activity_window
    import capo_guardduty.types.count
    import capo_guardduty.types.enrichment
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.string


class RdsLoginActivity(TypedDict, closed=True):
    outcome: NotRequired["capo_guardduty.types.string.String"]
    """<p>The outcome of the login attempts.</p>"""
    rate: NotRequired["capo_guardduty.types.string.String"]
    """<p>The rate of the login attempts.</p>"""
    anomaly_context: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>An explanation of how the login activity deviates from normal behavior.</p>"""
    login_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of login attempts.</p>"""
    activity_window: NotRequired["capo_guardduty.types.activity_window.ActivityWindow"]
    """<p>The time range of the login activity.</p>"""
    enrichment: NotRequired["capo_guardduty.types.enrichment.Enrichment"]
    """<p>Additional context about the login activity, such as geolocation information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsLoginActivity) -> dict:
    out: dict = {}
    if "outcome" in value:
        out["outcome"] = value["outcome"]
    if "rate" in value:
        out["rate"] = value["rate"]
    if "anomaly_context" in value:
        out["anomalyContext"] = value["anomaly_context"]
    if "login_count" in value:
        out["loginCount"] = value["login_count"]
    if "activity_window" in value:
        import capo_guardduty.types.activity_window

        out["activityWindow"] = capo_guardduty.types.activity_window.serialize_json(
            value["activity_window"]
        )
    if "enrichment" in value:
        import capo_guardduty.types.enrichment

        out["enrichment"] = capo_guardduty.types.enrichment.serialize_json(
            value["enrichment"]
        )
    return out


def deserialize_json(data: dict) -> RdsLoginActivity:
    out: RdsLoginActivity = {}  # type: ignore[typeddict-item]
    if data.get("outcome") is not None:
        out["outcome"] = data["outcome"]
    if data.get("rate") is not None:
        out["rate"] = data["rate"]
    if data.get("anomalyContext") is not None:
        out["anomaly_context"] = data["anomalyContext"]
    if data.get("loginCount") is not None:
        out["login_count"] = data["loginCount"]
    if data.get("activityWindow") is not None:
        import capo_guardduty.types.activity_window

        out["activity_window"] = capo_guardduty.types.activity_window.deserialize_json(
            data["activityWindow"]
        )
    if data.get("enrichment") is not None:
        import capo_guardduty.types.enrichment

        out["enrichment"] = capo_guardduty.types.enrichment.deserialize_json(
            data["enrichment"]
        )
    return out
