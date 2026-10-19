"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#EntryLimitsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.iso8601_duration


class EntryLimitsConfig(TypedDict, closed=True):
    max_entry_count: "int"
    """Maximum number of times a participant can enter the campaign. A value of 0 indicates unlimited entries. Values of 1 or greater specify the exact number of entries allowed."""
    min_entry_interval: "capo_connectcampaignsv2.types.iso8601_duration.Iso8601Duration"
    """Minimum time interval that must pass before a participant can enter the campaign again."""


# --- restJson1 ser/de ---
def serialize_json(value: EntryLimitsConfig) -> dict:
    out: dict = {}
    out["maxEntryCount"] = value["max_entry_count"]
    out["minEntryInterval"] = value["min_entry_interval"]
    return out


def deserialize_json(data: dict) -> EntryLimitsConfig:
    out: EntryLimitsConfig = {}  # type: ignore[typeddict-item]
    if data.get("maxEntryCount") is not None:
        out["max_entry_count"] = data["maxEntryCount"]
    else:
        out["max_entry_count"] = 0
    if data.get("minEntryInterval") is not None:
        out["min_entry_interval"] = data["minEntryInterval"]
    else:
        out["min_entry_interval"] = ""
    return out
