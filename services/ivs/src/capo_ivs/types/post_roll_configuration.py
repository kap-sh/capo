"""Generated from Smithy shape ``com.amazonaws.ivs#PostRollConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.ad_duration_seconds
    import capo_ivs.types.boolean


class PostRollConfiguration(TypedDict, closed=True):
    duration_seconds: "capo_ivs.types.ad_duration_seconds.AdDurationSeconds"
    """<p>Duration of the post-roll ad break, in seconds.</p>"""
    enabled: "capo_ivs.types.boolean.Boolean"
    """<p>Whether the post-roll ad configuration is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostRollConfiguration) -> dict:
    out: dict = {}
    out["durationSeconds"] = value["duration_seconds"]
    out["enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> PostRollConfiguration:
    out: PostRollConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("durationSeconds") is not None:
        out["duration_seconds"] = data["durationSeconds"]
    else:
        out["duration_seconds"] = 0
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out
