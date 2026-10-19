"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppCallPermissionLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_socialmessaging.types.iso8601_duration


class WhatsAppCallPermissionLimit(TypedDict, closed=True):
    time_period: "capo_socialmessaging.types.iso8601_duration.Iso8601Duration"
    """<p>The time period over which the limit applies, as an ISO 8601 duration.</p>"""
    max_allowed: "int"
    """<p>The maximum number of times the action is allowed within the time period.</p>"""
    current_usage: "int"
    """<p>The number of times the action has been used within the current time period.</p>"""
    limit_expiration_time: NotRequired["datetime.datetime"]
    """<p>The time when the limit resets. This value is present only when the current usage has reached the maximum allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppCallPermissionLimit) -> dict:
    out: dict = {}
    out["timePeriod"] = value["time_period"]
    out["maxAllowed"] = value["max_allowed"]
    out["currentUsage"] = value["current_usage"]
    if "limit_expiration_time" in value:
        import capo_socialmessaging.types._prelude.timestamp

        out["limitExpirationTime"] = (
            capo_socialmessaging.types._prelude.timestamp.serialize_json(
                value["limit_expiration_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> WhatsAppCallPermissionLimit:
    out: WhatsAppCallPermissionLimit = {}  # type: ignore[typeddict-item]
    if data.get("timePeriod") is not None:
        out["time_period"] = data["timePeriod"]
    else:
        out["time_period"] = ""
    if data.get("maxAllowed") is not None:
        out["max_allowed"] = data["maxAllowed"]
    else:
        out["max_allowed"] = 0
    if data.get("currentUsage") is not None:
        out["current_usage"] = data["currentUsage"]
    else:
        out["current_usage"] = 0
    if data.get("limitExpirationTime") is not None:
        import capo_socialmessaging.types._prelude.timestamp

        out["limit_expiration_time"] = (
            capo_socialmessaging.types._prelude.timestamp.deserialize_json(
                data["limitExpirationTime"]
            )
        )
    return out
