"""Generated from Smithy shape ``com.amazonaws.ecr#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.encryption_type
    import capo_ecr.types.kms_key


class EncryptionConfiguration(TypedDict, closed=True):
    encryption_type: "capo_ecr.types.encryption_type.EncryptionType"
    """<p>The encryption type to use.</p> <p>If you use the <code>KMS</code> encryption type, the contents of the repository will be encrypted using server-side encryption with Key Management Service key stored in KMS. When you use KMS to encrypt your data, you can either use the default Amazon Web Services managed KMS key for Amazon ECR, or specify your own KMS key, which you already created.</p> <p>If you use the <code>KMS_DSSE</code> encryption type, the contents of the repository will be encrypted with two layers of encryption using server-side encryption with the KMS Management Service key stored in KMS. Similar to the <code>KMS</code> encryption type, you can either use the default Amazon Web Services managed KMS key for Amazon ECR, or specify your own KMS key, which you've already created. </p> <p>If you use the <code>AES256</code> encryption type, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts the images in the repository using an AES256 encryption algorithm.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html">Amazon ECR encryption at rest</a> in the <i>Amazon Elastic Container Registry User Guide</i>.</p>"""
    kms_key: NotRequired["capo_ecr.types.kms_key.KmsKey"]
    """<p>If you use the <code>KMS</code> encryption type, specify the KMS key to use for encryption. The alias, key ID, or full ARN of the KMS key can be specified. The key must exist in the same Region as the repository. If no key is specified, the default Amazon Web Services managed KMS key for Amazon ECR will be used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_ecr.types.encryption_type

    out["encryptionType"] = capo_ecr.types.encryption_type.serialize_aws_json_1_1(
        value["encryption_type"]
    )
    if "kms_key" in value:
        out["kmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("encryptionType") is not None:
        import capo_ecr.types.encryption_type

        out["encryption_type"] = (
            capo_ecr.types.encryption_type.deserialize_aws_json_1_1(
                data["encryptionType"]
            )
        )
    else:
        raise DeserializationError("EncryptionConfiguration.encryption_type required")
    if data.get("kmsKey") is not None:
        out["kms_key"] = data["kmsKey"]
    return out
