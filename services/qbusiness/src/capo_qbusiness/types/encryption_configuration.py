"""Generated from Smithy shape ``com.amazonaws.qbusiness#EncryptionConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.kms_key_id


class EncryptionConfiguration(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_qbusiness.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the KMS key. Amazon Q Business doesn't support asymmetric keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out


def redact_sensitive(value: EncryptionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "kms_key_id" in value:
        out["kms_key_id"] = "*** Sensitive Data Redacted ***"
    return out
