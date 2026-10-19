"""Generated from Smithy shape ``com.amazonaws.voiceid#ServerSideEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.kms_key_id


class ServerSideEncryptionConfiguration(TypedDict, closed=True):
    kms_key_id: "capo_voice_id.types.kms_key_id.KmsKeyId"
    """<p>The identifier of the KMS key to use to encrypt data stored by Voice ID. Voice ID doesn't support asymmetric customer managed keys. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServerSideEncryptionConfiguration) -> dict:
    out: dict = {}
    out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ServerSideEncryptionConfiguration:
    out: ServerSideEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    else:
        out["kms_key_id"] = ""
    return out
