"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardSecurityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id


class ModelCardSecurityConfig(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>A Key Management Service <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id">key ID</a> to use for encrypting a model card.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardSecurityConfig) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelCardSecurityConfig:
    out: ModelCardSecurityConfig = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
