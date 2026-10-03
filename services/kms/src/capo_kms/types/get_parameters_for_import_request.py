"""Generated from Smithy shape ``com.amazonaws.kms#GetParametersForImportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.algorithm_spec
    import capo_kms.types.key_id_type
    import capo_kms.types.wrapping_key_spec


class GetParametersForImportRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>The identifier of the KMS key that will be associated with the imported key material. The <code>Origin</code> of the KMS key must be <code>EXTERNAL</code>.</p> <p>All KMS key types are supported, including multi-Region keys. However, you cannot import key material into a KMS key in a custom key store.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    wrapping_algorithm: "capo_kms.types.algorithm_spec.AlgorithmSpec"
    """<p>The algorithm you will use with the RSA public key (<code>PublicKey</code>) in the response to protect your key material during import. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-get-public-key-and-token.html#select-wrapping-algorithm">Select a wrapping algorithm</a> in the <i>Key Management Service Developer Guide</i>.</p> <p>For RSA_AES wrapping algorithms, you encrypt your key material with an AES key that you generate, then encrypt your AES key with the RSA public key from KMS. For RSAES wrapping algorithms, you encrypt your key material directly with the RSA public key from KMS.</p> <p>The wrapping algorithms that you can use depend on the type of key material that you are importing. To import an RSA private key, you must use an RSA_AES wrapping algorithm.</p> <ul> <li> <p> <b>RSA_AES_KEY_WRAP_SHA_256</b> — Supported for wrapping RSA and ECC key material.</p> </li> <li> <p> <b>RSA_AES_KEY_WRAP_SHA_1</b> — Supported for wrapping RSA and ECC key material.</p> </li> <li> <p> <b>RSAES_OAEP_SHA_256</b> — Supported for all types of key material, except RSA key material (private key).</p> <p>You cannot use the RSAES_OAEP_SHA_256 wrapping algorithm with the RSA_2048 wrapping key spec to wrap ECC_NIST_P521 key material.</p> </li> <li> <p> <b>RSAES_OAEP_SHA_1</b> — Supported for all types of key material, except RSA key material (private key).</p> <p>You cannot use the RSAES_OAEP_SHA_1 wrapping algorithm with the RSA_2048 wrapping key spec to wrap ECC_NIST_P521 key material.</p> </li> <li> <p> <b>RSAES_PKCS1_V1_5</b> (Deprecated) — As of October 10, 2023, KMS does not support the RSAES_PKCS1_V1_5 wrapping algorithm.</p> </li> </ul>"""
    wrapping_key_spec: "capo_kms.types.wrapping_key_spec.WrappingKeySpec"
    """<p>The type of RSA public key to return in the response. You will use this wrapping key with the specified wrapping algorithm to protect your key material during import. </p> <p>Use the longest RSA wrapping key that is practical. </p> <p>You cannot use an RSA_2048 public key to directly wrap an ECC_NIST_P521 private key. Instead, use an RSA_AES wrapping algorithm or choose a longer RSA public key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetParametersForImportRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    import capo_kms.types.algorithm_spec

    out["WrappingAlgorithm"] = capo_kms.types.algorithm_spec.serialize_aws_json_1_1(
        value["wrapping_algorithm"]
    )
    import capo_kms.types.wrapping_key_spec

    out["WrappingKeySpec"] = capo_kms.types.wrapping_key_spec.serialize_aws_json_1_1(
        value["wrapping_key_spec"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetParametersForImportRequest:
    out: GetParametersForImportRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("GetParametersForImportRequest.key_id required")
    if data.get("WrappingAlgorithm") is not None:
        import capo_kms.types.algorithm_spec

        out["wrapping_algorithm"] = (
            capo_kms.types.algorithm_spec.deserialize_aws_json_1_1(
                data["WrappingAlgorithm"]
            )
        )
    else:
        raise DeserializationError(
            "GetParametersForImportRequest.wrapping_algorithm required"
        )
    if data.get("WrappingKeySpec") is not None:
        import capo_kms.types.wrapping_key_spec

        out["wrapping_key_spec"] = (
            capo_kms.types.wrapping_key_spec.deserialize_aws_json_1_1(
                data["WrappingKeySpec"]
            )
        )
    else:
        raise DeserializationError(
            "GetParametersForImportRequest.wrapping_key_spec required"
        )
    return out
