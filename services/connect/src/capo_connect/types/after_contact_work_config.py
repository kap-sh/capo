"""Generated from Smithy shape ``com.amazonaws.connect#AfterContactWorkConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.after_contact_work_time_limit


class AfterContactWorkConfig(TypedDict, closed=True):
    after_contact_work_time_limit: (
        "capo_connect.types.after_contact_work_time_limit.AfterContactWorkTimeLimit"
    )
    """<p>The after contact work (ACW) timeout duration in seconds. Minimum: 1 second. Maximum: 2,000,000 seconds (24 days). For the CHAT channel, the maximum for a specific duration is 5,400 seconds (90 minutes); higher values end ACW after 90 minutes. For all channels, including chat, you can enter 0 for an indefinite amount of time, meaning agents must manually choose to end ACW.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AfterContactWorkConfig) -> dict:
    out: dict = {}
    out["AfterContactWorkTimeLimit"] = value.get("after_contact_work_time_limit", 0)
    return out


def deserialize_json(data: dict) -> AfterContactWorkConfig:
    out: AfterContactWorkConfig = {}  # type: ignore[typeddict-item]
    if data.get("AfterContactWorkTimeLimit") is not None:
        out["after_contact_work_time_limit"] = data["AfterContactWorkTimeLimit"]
    else:
        out["after_contact_work_time_limit"] = 0
    return out
