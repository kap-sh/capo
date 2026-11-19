"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchTimeWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.fetch_duration_in_minutes
    import capo_guardduty.types.timestamp


class FetchTimeWindow(TypedDict, closed=True):
    started_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the time range starts.</p>"""
    duration_in_minutes: NotRequired[
        "capo_guardduty.types.fetch_duration_in_minutes.FetchDurationInMinutes"
    ]
    """<p>The length of the time range, in minutes. Valid values are 1 to 120.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FetchTimeWindow) -> dict:
    out: dict = {}
    if "started_at" in value:
        import capo_guardduty.types.timestamp

        out["startedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["started_at"]
        )
    if "duration_in_minutes" in value:
        out["durationInMinutes"] = value["duration_in_minutes"]
    return out


def deserialize_json(data: dict) -> FetchTimeWindow:
    out: FetchTimeWindow = {}  # type: ignore[typeddict-item]
    if data.get("startedAt") is not None:
        import capo_guardduty.types.timestamp

        out["started_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["startedAt"]
        )
    if data.get("durationInMinutes") is not None:
        out["duration_in_minutes"] = data["durationInMinutes"]
    return out
