"""Generated from Smithy shape ``com.amazonaws.wickr#GetBotsCountResponse``."""

from typing_extensions import TypedDict


class GetBotsCountResponse(TypedDict, closed=True):
    pending: "int"
    """<p>The number of bots with pending status (invited but not yet activated).</p>"""
    active: "int"
    """<p>The number of bots with active status.</p>"""
    total: "int"
    """<p>The total number of bots in the network (active and pending).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotsCountResponse) -> dict:
    out: dict = {}
    out["pending"] = value["pending"]
    out["active"] = value["active"]
    out["total"] = value["total"]
    return out


def deserialize_json(data: dict) -> GetBotsCountResponse:
    out: GetBotsCountResponse = {}  # type: ignore[typeddict-item]
    if data.get("pending") is not None:
        out["pending"] = data["pending"]
    else:
        out["pending"] = 0
    if data.get("active") is not None:
        out["active"] = data["active"]
    else:
        out["active"] = 0
    if data.get("total") is not None:
        out["total"] = data["total"]
    else:
        out["total"] = 0
    return out
