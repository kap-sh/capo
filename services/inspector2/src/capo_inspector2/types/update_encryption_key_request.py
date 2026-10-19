"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateEncryptionKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.kms_key_arn
    import capo_inspector2.types.resource_type
    import capo_inspector2.types.scan_type


class UpdateEncryptionKeyRequest(TypedDict, closed=True):
    kms_key_id: "capo_inspector2.types.kms_key_arn.KmsKeyArn"
    """<p>A KMS key ID for the encryption key.</p>"""
    scan_type: "capo_inspector2.types.scan_type.ScanType"
    """<p>The scan type for the encryption key.</p>"""
    resource_type: "capo_inspector2.types.resource_type.ResourceType"
    """<p>The resource type for the encryption key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEncryptionKeyRequest) -> dict:
    out: dict = {}
    out["kmsKeyId"] = value["kms_key_id"]
    out["scanType"] = value["scan_type"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> UpdateEncryptionKeyRequest:
    out: UpdateEncryptionKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        out["kms_key_id"] = ""
    if data.get("scanType") is not None:
        out["scan_type"] = data["scanType"]
    else:
        out["scan_type"] = ""
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    return out
