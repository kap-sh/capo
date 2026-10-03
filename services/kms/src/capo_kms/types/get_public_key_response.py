"""Generated from Smithy shape ``com.amazonaws.kms#GetPublicKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.customer_master_key_spec
    import capo_kms.types.encryption_algorithm_spec_list
    import capo_kms.types.key_agreement_algorithm_spec_list
    import capo_kms.types.key_id_type
    import capo_kms.types.key_spec
    import capo_kms.types.key_usage_type
    import capo_kms.types.public_key_type
    import capo_kms.types.signing_algorithm_spec_list


class GetPublicKeyResponse(TypedDict, closed=True):
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">key ARN</a>) of the asymmetric KMS key from which the public key was downloaded.</p>"""
    public_key: NotRequired["capo_kms.types.public_key_type.PublicKeyType"]
    """<p>The exported public key. </p> <p>The value is a DER-encoded X.509 public key, also known as <code>SubjectPublicKeyInfo</code> (SPKI), as defined in <a href="https://tools.ietf.org/html/rfc5280">RFC 5280</a>. When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.</p> <p></p>"""
    customer_master_key_spec: NotRequired[
        "capo_kms.types.customer_master_key_spec.CustomerMasterKeySpec"
    ]
    """<p>Instead, use the <code>KeySpec</code> field in the <code>GetPublicKey</code> response.</p> <p>The <code>KeySpec</code> and <code>CustomerMasterKeySpec</code> fields have the same value. We recommend that you use the <code>KeySpec</code> field in your code. However, to avoid breaking changes, KMS supports both fields.</p>"""
    key_spec: NotRequired["capo_kms.types.key_spec.KeySpec"]
    """<p>The type of the of the public key that was downloaded.</p>"""
    key_usage: NotRequired["capo_kms.types.key_usage_type.KeyUsageType"]
    """<p>The permitted use of the public key. Valid values for asymmetric key pairs are <code>ENCRYPT_DECRYPT</code>, <code>SIGN_VERIFY</code>, and <code>KEY_AGREEMENT</code>. </p> <p>This information is critical. For example, if a public key with <code>SIGN_VERIFY</code> key usage encrypts data outside of KMS, the ciphertext cannot be decrypted. </p>"""
    encryption_algorithms: NotRequired[
        "capo_kms.types.encryption_algorithm_spec_list.EncryptionAlgorithmSpecList"
    ]
    """<p>The encryption algorithms that KMS supports for this key. </p> <p>This information is critical. If a public key encrypts data outside of KMS by using an unsupported encryption algorithm, the ciphertext cannot be decrypted. </p> <p>This field appears in the response only when the <code>KeyUsage</code> of the public key is <code>ENCRYPT_DECRYPT</code>.</p>"""
    signing_algorithms: NotRequired[
        "capo_kms.types.signing_algorithm_spec_list.SigningAlgorithmSpecList"
    ]
    """<p>The signing algorithms that KMS supports for this key.</p> <p>This field appears in the response only when the <code>KeyUsage</code> of the public key is <code>SIGN_VERIFY</code>.</p>"""
    key_agreement_algorithms: NotRequired[
        "capo_kms.types.key_agreement_algorithm_spec_list.KeyAgreementAlgorithmSpecList"
    ]
    """<p>The key agreement algorithm used to derive a shared secret. This field is present only when the KMS key has a <code>KeyUsage</code> value of <code>KEY_AGREEMENT</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPublicKeyResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "public_key" in value:
        import capo_kms.types.public_key_type

        out["PublicKey"] = capo_kms.types.public_key_type.serialize_aws_json_1_1(
            value["public_key"]
        )
    if "customer_master_key_spec" in value:
        import capo_kms.types.customer_master_key_spec

        out["CustomerMasterKeySpec"] = (
            capo_kms.types.customer_master_key_spec.serialize_aws_json_1_1(
                value["customer_master_key_spec"]
            )
        )
    if "key_spec" in value:
        import capo_kms.types.key_spec

        out["KeySpec"] = capo_kms.types.key_spec.serialize_aws_json_1_1(
            value["key_spec"]
        )
    if "key_usage" in value:
        import capo_kms.types.key_usage_type

        out["KeyUsage"] = capo_kms.types.key_usage_type.serialize_aws_json_1_1(
            value["key_usage"]
        )
    if "encryption_algorithms" in value:
        import capo_kms.types.encryption_algorithm_spec_list

        out["EncryptionAlgorithms"] = (
            capo_kms.types.encryption_algorithm_spec_list.serialize_aws_json_1_1(
                value["encryption_algorithms"]
            )
        )
    if "signing_algorithms" in value:
        import capo_kms.types.signing_algorithm_spec_list

        out["SigningAlgorithms"] = (
            capo_kms.types.signing_algorithm_spec_list.serialize_aws_json_1_1(
                value["signing_algorithms"]
            )
        )
    if "key_agreement_algorithms" in value:
        import capo_kms.types.key_agreement_algorithm_spec_list

        out["KeyAgreementAlgorithms"] = (
            capo_kms.types.key_agreement_algorithm_spec_list.serialize_aws_json_1_1(
                value["key_agreement_algorithms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPublicKeyResponse:
    out: GetPublicKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("PublicKey") is not None:
        import capo_kms.types.public_key_type

        out["public_key"] = capo_kms.types.public_key_type.deserialize_aws_json_1_1(
            data["PublicKey"]
        )
    if data.get("CustomerMasterKeySpec") is not None:
        import capo_kms.types.customer_master_key_spec

        out["customer_master_key_spec"] = (
            capo_kms.types.customer_master_key_spec.deserialize_aws_json_1_1(
                data["CustomerMasterKeySpec"]
            )
        )
    if data.get("KeySpec") is not None:
        import capo_kms.types.key_spec

        out["key_spec"] = capo_kms.types.key_spec.deserialize_aws_json_1_1(
            data["KeySpec"]
        )
    if data.get("KeyUsage") is not None:
        import capo_kms.types.key_usage_type

        out["key_usage"] = capo_kms.types.key_usage_type.deserialize_aws_json_1_1(
            data["KeyUsage"]
        )
    if data.get("EncryptionAlgorithms") is not None:
        import capo_kms.types.encryption_algorithm_spec_list

        out["encryption_algorithms"] = (
            capo_kms.types.encryption_algorithm_spec_list.deserialize_aws_json_1_1(
                data["EncryptionAlgorithms"]
            )
        )
    if data.get("SigningAlgorithms") is not None:
        import capo_kms.types.signing_algorithm_spec_list

        out["signing_algorithms"] = (
            capo_kms.types.signing_algorithm_spec_list.deserialize_aws_json_1_1(
                data["SigningAlgorithms"]
            )
        )
    if data.get("KeyAgreementAlgorithms") is not None:
        import capo_kms.types.key_agreement_algorithm_spec_list

        out["key_agreement_algorithms"] = (
            capo_kms.types.key_agreement_algorithm_spec_list.deserialize_aws_json_1_1(
                data["KeyAgreementAlgorithms"]
            )
        )
    return out
