"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageEncryptionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.kms_key_id


class PackageEncryptionOptions(TypedDict, closed=True):
    kms_key_identifier: NotRequired["capo_opensearch.types.kms_key_id.KmsKeyId"]
    """<p>KMS key ID for encrypting the package.</p>"""
    encryption_enabled: "capo_opensearch.types.boolean.Boolean"
    """<p>Whether encryption is enabled for the package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageEncryptionOptions) -> dict:
    out: dict = {}
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    out["EncryptionEnabled"] = value["encryption_enabled"]
    return out


def deserialize_json(data: dict) -> PackageEncryptionOptions:
    out: PackageEncryptionOptions = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    if data.get("EncryptionEnabled") is not None:
        out["encryption_enabled"] = data["EncryptionEnabled"]
    else:
        out["encryption_enabled"] = False
    return out
