"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TimeoutConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.timeout_duration


class TimeoutConfig(TypedDict, closed=True):
    duration_in_seconds: (
        "capo_connectcampaignsv2.types.timeout_duration.TimeoutDuration"
    )


# --- restJson1 ser/de ---
def serialize_json(value: TimeoutConfig) -> dict:
    out: dict = {}
    out["durationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_json(data: dict) -> TimeoutConfig:
    out: TimeoutConfig = {}  # type: ignore[typeddict-item]
    if data.get("durationInSeconds") is not None:
        out["duration_in_seconds"] = data["durationInSeconds"]
    else:
        out["duration_in_seconds"] = 0
    return out
