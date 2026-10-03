"""Generated from Smithy shape ``com.amazonaws.kms#DeriveSharedSecretRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.grant_token_list
    import capo_kms.types.key_agreement_algorithm_spec
    import capo_kms.types.key_id_type
    import capo_kms.types.nullable_boolean_type
    import capo_kms.types.public_key_type
    import capo_kms.types.recipient_info


class DeriveSharedSecretRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Identifies an asymmetric NIST-standard ECC or SM2 (China Regions only) KMS key. KMS uses the private key in the specified key pair to derive the shared secret. The key usage of the KMS key must be <code>KEY_AGREEMENT</code>. To find the <code>KeyUsage</code> of a KMS key, use the <a>DescribeKey</a> operation.</p> <p>To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with <code>"alias/"</code>. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias ARN: <code>arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>. To get the alias name and alias ARN, use <a>ListAliases</a>.</p>"""
    key_agreement_algorithm: (
        "capo_kms.types.key_agreement_algorithm_spec.KeyAgreementAlgorithmSpec"
    )
    """<p>Specifies the key agreement algorithm used to derive the shared secret. The only valid value is <code>ECDH</code>.</p>"""
    public_key: "capo_kms.types.public_key_type.PublicKeyType"
    """<p>Specifies the public key in your peer's NIST-standard elliptic curve (ECC) or SM2 (China Regions only) key pair.</p> <p>The public key must be a DER-encoded X.509 public key, also known as <code>SubjectPublicKeyInfo</code> (SPKI), as defined in <a href="https://tools.ietf.org/html/rfc5280">RFC 5280</a>.</p> <p> <a>GetPublicKey</a> returns the public key of an asymmetric KMS key pair in the required DER-encoded format.</p> <note> <p>If you use <a href="https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-welcome.html">Amazon Web Services CLI version 1</a>, you must provide the DER-encoded X.509 public key in a file. Otherwise, the Amazon Web Services CLI Base64-encodes the public key a second time, resulting in a <code>ValidationException</code>.</p> </note> <p>You can specify the public key as binary data in a file using fileb (<code>fileb://<path-to-file></code>) or in-line using a Base64 encoded string.</p>"""
    grant_tokens: NotRequired["capo_kms.types.grant_token_list.GrantTokenList"]
    """<p>A list of grant tokens.</p> <p>Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved <i>eventual consistency</i>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token">Grant token</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html">Using a grant token</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    dry_run: NotRequired["capo_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    recipient: NotRequired["capo_kms.types.recipient_info.RecipientInfo"]
    """<p>A signed <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitro-enclave-how.html#term-attestdoc">attestation document</a> from an Amazon Web Services Nitro enclave or NitroTPM, and the encryption algorithm to use with the public key in the attestation document. The only valid encryption algorithm is <code>RSAES_OAEP_SHA_256</code>. </p> <p>This parameter only supports attestation documents for Amazon Web Services Nitro Enclaves or Amazon Web Services NitroTPM. To call DeriveSharedSecret generate an attestation document use either <a href="https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk">Amazon Web Services Nitro Enclaves SDK</a> for an Amazon Web Services Nitro Enclaves or <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attestation-get-doc.html">Amazon Web Services NitroTPM tools</a> for Amazon Web Services NitroTPM. Then use the Recipient parameter from any Amazon Web Services SDK to provide the attestation document for the attested environment.</p> <p>When you use this parameter, instead of returning a plaintext copy of the shared secret, KMS encrypts the plaintext shared secret under the public key in the attestation document, and returns the resulting ciphertext in the <code>CiphertextForRecipient</code> field in the response. This ciphertext can be decrypted only with the private key in the attested environment. The <code>CiphertextBlob</code> field in the response contains the encrypted shared secret derived from the KMS key specified by the <code>KeyId</code> parameter and public key specified by the <code>PublicKey</code> parameter. The <code>SharedSecret</code> field in the response is null or empty.</p> <p>For information about the interaction between KMS and Amazon Web Services Nitro Enclaves or Amazon Web Services NitroTPM, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html">Cryptographic attestation support in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeriveSharedSecretRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    import capo_kms.types.key_agreement_algorithm_spec

    out["KeyAgreementAlgorithm"] = (
        capo_kms.types.key_agreement_algorithm_spec.serialize_aws_json_1_1(
            value["key_agreement_algorithm"]
        )
    )
    import capo_kms.types.public_key_type

    out["PublicKey"] = capo_kms.types.public_key_type.serialize_aws_json_1_1(
        value["public_key"]
    )
    if "grant_tokens" in value:
        import capo_kms.types.grant_token_list

        out["GrantTokens"] = capo_kms.types.grant_token_list.serialize_aws_json_1_1(
            value["grant_tokens"]
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "recipient" in value:
        import capo_kms.types.recipient_info

        out["Recipient"] = capo_kms.types.recipient_info.serialize_aws_json_1_1(
            value["recipient"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeriveSharedSecretRequest:
    out: DeriveSharedSecretRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("DeriveSharedSecretRequest.key_id required")
    if data.get("KeyAgreementAlgorithm") is not None:
        import capo_kms.types.key_agreement_algorithm_spec

        out["key_agreement_algorithm"] = (
            capo_kms.types.key_agreement_algorithm_spec.deserialize_aws_json_1_1(
                data["KeyAgreementAlgorithm"]
            )
        )
    else:
        raise DeserializationError(
            "DeriveSharedSecretRequest.key_agreement_algorithm required"
        )
    if data.get("PublicKey") is not None:
        import capo_kms.types.public_key_type

        out["public_key"] = capo_kms.types.public_key_type.deserialize_aws_json_1_1(
            data["PublicKey"]
        )
    else:
        raise DeserializationError("DeriveSharedSecretRequest.public_key required")
    if data.get("GrantTokens") is not None:
        import capo_kms.types.grant_token_list

        out["grant_tokens"] = capo_kms.types.grant_token_list.deserialize_aws_json_1_1(
            data["GrantTokens"]
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    if data.get("Recipient") is not None:
        import capo_kms.types.recipient_info

        out["recipient"] = capo_kms.types.recipient_info.deserialize_aws_json_1_1(
            data["Recipient"]
        )
    return out
