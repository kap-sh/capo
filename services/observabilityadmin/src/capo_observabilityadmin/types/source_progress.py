"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#SourceProgress``."""

from typing_extensions import NotRequired, TypedDict


class SourceProgress(TypedDict, closed=True):
    active: NotRequired["int"]
    """<p>The number of discovered sources that are active and sending telemetry to the pipeline.</p>"""
    total: NotRequired["int"]
    """<p>The total number of sources discovered for the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceProgress) -> dict:
    out: dict = {}
    if "active" in value:
        out["Active"] = value["active"]
    if "total" in value:
        out["Total"] = value["total"]
    return out


def deserialize_json(data: dict) -> SourceProgress:
    out: SourceProgress = {}  # type: ignore[typeddict-item]
    if data.get("Active") is not None:
        out["active"] = data["Active"]
    if data.get("Total") is not None:
        out["total"] = data["Total"]
    return out
