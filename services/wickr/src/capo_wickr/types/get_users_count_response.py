"""Generated from Smithy shape ``com.amazonaws.wickr#GetUsersCountResponse``."""

from typing_extensions import TypedDict


class GetUsersCountResponse(TypedDict, closed=True):
    pending: "int"
    """<p>The number of users with pending status (invited but not yet accepted).</p>"""
    active: "int"
    """<p>The number of users with active status in the network.</p>"""
    rejected: "int"
    """<p>The number of users who have rejected network invitations.</p>"""
    remaining: "int"
    """<p>The number of additional users that can be added to the network while maintaining premium free trial eligibility.</p>"""
    total: "int"
    """<p>The total number of users in the network (active and pending combined).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUsersCountResponse) -> dict:
    out: dict = {}
    out["pending"] = value["pending"]
    out["active"] = value["active"]
    out["rejected"] = value["rejected"]
    out["remaining"] = value["remaining"]
    out["total"] = value["total"]
    return out


def deserialize_json(data: dict) -> GetUsersCountResponse:
    out: GetUsersCountResponse = {}  # type: ignore[typeddict-item]
    if data.get("pending") is not None:
        out["pending"] = data["pending"]
    else:
        out["pending"] = 0
    if data.get("active") is not None:
        out["active"] = data["active"]
    else:
        out["active"] = 0
    if data.get("rejected") is not None:
        out["rejected"] = data["rejected"]
    else:
        out["rejected"] = 0
    if data.get("remaining") is not None:
        out["remaining"] = data["remaining"]
    else:
        out["remaining"] = 0
    if data.get("total") is not None:
        out["total"] = data["total"]
    else:
        out["total"] = 0
    return out
