"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#TemplateRevision``."""

from typing_extensions import TypedDict


class TemplateRevision(TypedDict, closed=True):
    major_revision: "int"
    """<p>The revision version of the template. Re-enrolling all certificate holders will increment the major revision.</p>"""
    minor_revision: "int"
    """<p>The revision version of the template. Re-enrolling all certificate holders will increment the major revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateRevision) -> dict:
    out: dict = {}
    out["MajorRevision"] = value["major_revision"]
    out["MinorRevision"] = value["minor_revision"]
    return out


def deserialize_json(data: dict) -> TemplateRevision:
    out: TemplateRevision = {}  # type: ignore[typeddict-item]
    if data.get("MajorRevision") is not None:
        out["major_revision"] = data["MajorRevision"]
    else:
        out["major_revision"] = 0
    if data.get("MinorRevision") is not None:
        out["minor_revision"] = data["MinorRevision"]
    else:
        out["minor_revision"] = 0
    return out
