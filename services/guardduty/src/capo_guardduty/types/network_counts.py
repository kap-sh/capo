"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkCounts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count


class NetworkCounts(TypedDict, closed=True):
    request_count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of requests.</p>"""
    total_attempts: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The total number of connection attempts.</p>"""
    suspicious_attempts: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of connection attempts that were suspicious.</p>"""
    reset_attempts: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of connection attempts that were reset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkCounts) -> dict:
    out: dict = {}
    if "request_count" in value:
        out["requestCount"] = value["request_count"]
    if "total_attempts" in value:
        out["totalAttempts"] = value["total_attempts"]
    if "suspicious_attempts" in value:
        out["suspiciousAttempts"] = value["suspicious_attempts"]
    if "reset_attempts" in value:
        out["resetAttempts"] = value["reset_attempts"]
    return out


def deserialize_json(data: dict) -> NetworkCounts:
    out: NetworkCounts = {}  # type: ignore[typeddict-item]
    if data.get("requestCount") is not None:
        out["request_count"] = data["requestCount"]
    if data.get("totalAttempts") is not None:
        out["total_attempts"] = data["totalAttempts"]
    if data.get("suspiciousAttempts") is not None:
        out["suspicious_attempts"] = data["suspiciousAttempts"]
    if data.get("resetAttempts") is not None:
        out["reset_attempts"] = data["resetAttempts"]
    return out
