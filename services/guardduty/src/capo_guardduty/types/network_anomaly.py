"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkAnomaly``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count
    import capo_guardduty.types.integer
    import capo_guardduty.types.string


class NetworkAnomaly(TypedDict, closed=True):
    baseline_bytes: NotRequired["capo_guardduty.types.string.String"]
    """<p>The amount of data that is typical for the normal behavior.</p>"""
    deviation: NotRequired["capo_guardduty.types.string.String"]
    """<p>How much the activity deviates from normal behavior.</p>"""
    profile_age_days: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The number of days of activity that the normal behavior is based on.</p>"""
    remote_service: NotRequired["capo_guardduty.types.string.String"]
    """<p>The remote service that the activity involved.</p>"""
    remote_region: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Region of the remote endpoint.</p>"""
    duration: NotRequired["capo_guardduty.types.string.String"]
    """<p>The duration of the activity.</p>"""
    reset_ratio: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ratio of connection attempts that were reset.</p>"""
    target_host_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of target hosts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkAnomaly) -> dict:
    out: dict = {}
    if "baseline_bytes" in value:
        out["baselineBytes"] = value["baseline_bytes"]
    if "deviation" in value:
        out["deviation"] = value["deviation"]
    if "profile_age_days" in value:
        out["profileAgeDays"] = value["profile_age_days"]
    if "remote_service" in value:
        out["remoteService"] = value["remote_service"]
    if "remote_region" in value:
        out["remoteRegion"] = value["remote_region"]
    if "duration" in value:
        out["duration"] = value["duration"]
    if "reset_ratio" in value:
        out["resetRatio"] = value["reset_ratio"]
    if "target_host_count" in value:
        out["targetHostCount"] = value["target_host_count"]
    return out


def deserialize_json(data: dict) -> NetworkAnomaly:
    out: NetworkAnomaly = {}  # type: ignore[typeddict-item]
    if data.get("baselineBytes") is not None:
        out["baseline_bytes"] = data["baselineBytes"]
    if data.get("deviation") is not None:
        out["deviation"] = data["deviation"]
    if data.get("profileAgeDays") is not None:
        out["profile_age_days"] = data["profileAgeDays"]
    if data.get("remoteService") is not None:
        out["remote_service"] = data["remoteService"]
    if data.get("remoteRegion") is not None:
        out["remote_region"] = data["remoteRegion"]
    if data.get("duration") is not None:
        out["duration"] = data["duration"]
    if data.get("resetRatio") is not None:
        out["reset_ratio"] = data["resetRatio"]
    if data.get("targetHostCount") is not None:
        out["target_host_count"] = data["targetHostCount"]
    return out
