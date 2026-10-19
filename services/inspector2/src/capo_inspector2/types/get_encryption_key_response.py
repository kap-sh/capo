"""Generated from Smithy shape ``com.amazonaws.inspector2#GetEncryptionKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.kms_key_arn


class GetEncryptionKeyResponse(TypedDict, closed=True):
    kms_key_id: "capo_inspector2.types.kms_key_arn.KmsKeyArn"
    """<p>A kms key ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEncryptionKeyResponse) -> dict:
    out: dict = {}
    out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> GetEncryptionKeyResponse:
    out: GetEncryptionKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        out["kms_key_id"] = ""
    return out
