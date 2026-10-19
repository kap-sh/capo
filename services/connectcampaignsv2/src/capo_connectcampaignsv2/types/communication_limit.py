"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CommunicationLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.communication_limit_time_unit


class CommunicationLimit(TypedDict, closed=True):
    max_count_per_recipient: "int"
    """Maximum number of contacts allowed for a given target within the given frequency."""
    frequency: "int"
    """The number of days to consider with regards to this limit."""
    unit: "capo_connectcampaignsv2.types.communication_limit_time_unit.CommunicationLimitTimeUnit"


# --- restJson1 ser/de ---
def serialize_json(value: CommunicationLimit) -> dict:
    out: dict = {}
    out["maxCountPerRecipient"] = value["max_count_per_recipient"]
    out["frequency"] = value["frequency"]
    out["unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> CommunicationLimit:
    out: CommunicationLimit = {}  # type: ignore[typeddict-item]
    if data.get("maxCountPerRecipient") is not None:
        out["max_count_per_recipient"] = data["maxCountPerRecipient"]
    else:
        out["max_count_per_recipient"] = 0
    if data.get("frequency") is not None:
        out["frequency"] = data["frequency"]
    else:
        out["frequency"] = 0
    if data.get("unit") is not None:
        out["unit"] = data["unit"]
    else:
        out["unit"] = ""
    return out
