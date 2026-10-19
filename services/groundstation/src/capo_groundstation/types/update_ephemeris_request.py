"""Generated from Smithy shape ``com.amazonaws.groundstation#UpdateEphemerisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.ephemeris_priority
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.uuid


class UpdateEphemerisRequest(TypedDict, closed=True):
    ephemeris_id: "capo_groundstation.types.uuid.Uuid"
    """<p>The AWS Ground Station ephemeris ID.</p>"""
    enabled: "bool"
    """<p>Enable or disable the ephemeris. Changing this value doesn't require re-validation.</p>"""
    name: NotRequired["capo_groundstation.types.safe_name.SafeName"]
    """<p>A name that you can use to identify the ephemeris.</p>"""
    priority: NotRequired[
        "capo_groundstation.types.ephemeris_priority.EphemerisPriority"
    ]
    """<p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEphemerisRequest) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    if "name" in value:
        out["name"] = value["name"]
    if "priority" in value:
        out["priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> UpdateEphemerisRequest:
    out: UpdateEphemerisRequest = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    return out
