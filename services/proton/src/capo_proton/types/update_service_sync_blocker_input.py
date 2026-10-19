"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceSyncBlockerInput``."""

from typing_extensions import TypedDict


class UpdateServiceSyncBlockerInput(TypedDict, closed=True):
    id: "str"
    """<p>The ID of the service sync blocker.</p>"""
    resolved_reason: "str"
    """<p>The reason the service sync blocker was resolved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceSyncBlockerInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["resolvedReason"] = value["resolved_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceSyncBlockerInput:
    out: UpdateServiceSyncBlockerInput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("resolvedReason") is not None:
        out["resolved_reason"] = data["resolvedReason"]
    else:
        out["resolved_reason"] = ""
    return out
