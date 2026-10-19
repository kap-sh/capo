"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#FindingIdentifier``."""

from typing_extensions import TypedDict


class FindingIdentifier(TypedDict, closed=True):
    scan_name: "str"
    """<p>The name of the scan that generated the finding. </p>"""
    finding_id: "str"
    """<p>The identifier for a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingIdentifier) -> dict:
    out: dict = {}
    out["scanName"] = value["scan_name"]
    out["findingId"] = value["finding_id"]
    return out


def deserialize_json(data: dict) -> FindingIdentifier:
    out: FindingIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("scanName") is not None:
        out["scan_name"] = data["scanName"]
    else:
        out["scan_name"] = ""
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        out["finding_id"] = ""
    return out
