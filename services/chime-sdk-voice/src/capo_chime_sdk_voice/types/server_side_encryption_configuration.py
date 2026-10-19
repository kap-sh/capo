"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ServerSideEncryptionConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.arn


class ServerSideEncryptionConfiguration(TypedDict, closed=True):
    kms_key_arn: "capo_chime_sdk_voice.types.arn.Arn"
    """<p>The ARN of the KMS key used to encrypt the enrollment data in a voice profile domain. Asymmetric customer managed keys are not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerSideEncryptionConfiguration) -> dict:
    out: dict = {}
    out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> ServerSideEncryptionConfiguration:
    out: ServerSideEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    else:
        out["kms_key_arn"] = ""
    return out


def redact_sensitive(value: ServerSideEncryptionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "kms_key_arn" in value:
        out["kms_key_arn"] = "*** Sensitive Data Redacted ***"
    return out
