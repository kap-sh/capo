"""Generated from Smithy shape ``com.amazonaws.inspector2#SendCisSessionHealthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.uuid


class SendCisSessionHealthRequest(TypedDict, closed=True):
    scan_job_id: "capo_inspector2.types.uuid.UUID"
    """<p>A unique identifier for the scan job.</p>"""
    session_token: "capo_inspector2.types.uuid.UUID"
    """<p>The unique token that identifies the CIS session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendCisSessionHealthRequest) -> dict:
    out: dict = {}
    out["scanJobId"] = value["scan_job_id"]
    out["sessionToken"] = value["session_token"]
    return out


def deserialize_json(data: dict) -> SendCisSessionHealthRequest:
    out: SendCisSessionHealthRequest = {}  # type: ignore[typeddict-item]
    if data.get("scanJobId") is not None:
        out["scan_job_id"] = data["scanJobId"]
    else:
        out["scan_job_id"] = ""
    if data.get("sessionToken") is not None:
        out["session_token"] = data["sessionToken"]
    else:
        out["session_token"] = ""
    return out
