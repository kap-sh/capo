"""Generated from Smithy shape ``com.amazonaws.inspector2#ResetEncryptionKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.resource_type
    import capo_inspector2.types.scan_type


class ResetEncryptionKeyRequest(TypedDict, closed=True):
    scan_type: "capo_inspector2.types.scan_type.ScanType"
    """<p>The scan type the key encrypts.</p>"""
    resource_type: "capo_inspector2.types.resource_type.ResourceType"
    """<p>The resource type the key encrypts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetEncryptionKeyRequest) -> dict:
    out: dict = {}
    out["scanType"] = value["scan_type"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResetEncryptionKeyRequest:
    out: ResetEncryptionKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("scanType") is not None:
        out["scan_type"] = data["scanType"]
    else:
        out["scan_type"] = ""
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    return out
