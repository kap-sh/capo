"""Generated from Smithy shape ``com.amazonaws.devopsagent#ReferenceOutput``."""

from typing_extensions import NotRequired, TypedDict


class ReferenceOutput(TypedDict, closed=True):
    system: "str"
    """<p>The name of the external system</p>"""
    title: NotRequired["str"]
    """<p>Optional title for the reference</p>"""
    reference_id: "str"
    """<p>The unique identifier in the external system</p>"""
    reference_url: "str"
    """<p>URL to access the reference in the external system</p>"""
    association_id: "str"
    """<p>Association identifier of the external system</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceOutput) -> dict:
    out: dict = {}
    out["system"] = value["system"]
    if "title" in value:
        out["title"] = value["title"]
    out["referenceId"] = value["reference_id"]
    out["referenceUrl"] = value["reference_url"]
    out["associationId"] = value["association_id"]
    return out


def deserialize_json(data: dict) -> ReferenceOutput:
    out: ReferenceOutput = {}  # type: ignore[typeddict-item]
    if data.get("system") is not None:
        out["system"] = data["system"]
    else:
        out["system"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("referenceId") is not None:
        out["reference_id"] = data["referenceId"]
    else:
        out["reference_id"] = ""
    if data.get("referenceUrl") is not None:
        out["reference_url"] = data["referenceUrl"]
    else:
        out["reference_url"] = ""
    if data.get("associationId") is not None:
        out["association_id"] = data["associationId"]
    else:
        out["association_id"] = ""
    return out
