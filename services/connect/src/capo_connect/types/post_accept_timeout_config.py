"""Generated from Smithy shape ``com.amazonaws.connect#PostAcceptTimeoutConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.post_accept_preview_timeout_duration_in_seconds


class PostAcceptTimeoutConfig(TypedDict, closed=True):
    duration_in_seconds: "capo_connect.types.post_accept_preview_timeout_duration_in_seconds.PostAcceptPreviewTimeoutDurationInSeconds"
    """<p>Duration in seconds for the countdown timer after the agent accepted the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostAcceptTimeoutConfig) -> dict:
    out: dict = {}
    out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_json(data: dict) -> PostAcceptTimeoutConfig:
    out: PostAcceptTimeoutConfig = {}  # type: ignore[typeddict-item]
    if data.get("DurationInSeconds") is not None:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    else:
        out["duration_in_seconds"] = 0
    return out
