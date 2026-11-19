"""Generated from Smithy shape ``com.amazonaws.guardduty#ActivityWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.timestamp


class ActivityWindow(TypedDict, closed=True):
    first_seen_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the activity was first observed.</p>"""
    last_seen_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the activity was last observed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivityWindow) -> dict:
    out: dict = {}
    if "first_seen_at" in value:
        import capo_guardduty.types.timestamp

        out["firstSeenAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["first_seen_at"]
        )
    if "last_seen_at" in value:
        import capo_guardduty.types.timestamp

        out["lastSeenAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["last_seen_at"]
        )
    return out


def deserialize_json(data: dict) -> ActivityWindow:
    out: ActivityWindow = {}  # type: ignore[typeddict-item]
    if data.get("firstSeenAt") is not None:
        import capo_guardduty.types.timestamp

        out["first_seen_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["firstSeenAt"]
        )
    if data.get("lastSeenAt") is not None:
        import capo_guardduty.types.timestamp

        out["last_seen_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["lastSeenAt"]
        )
    return out
