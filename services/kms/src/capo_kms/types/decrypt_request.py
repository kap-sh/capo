"""Generated from Smithy shape ``com.amazonaws.kms#DecryptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.ciphertext_type
    import capo_kms.types.dry_run_modifier_list
    import capo_kms.types.encryption_algorithm_spec
    import capo_kms.types.encryption_context_type
    import capo_kms.types.grant_token_list
    import capo_kms.types.key_id_type
    import capo_kms.types.nullable_boolean_type
    import capo_kms.types.recipient_info


class DecryptRequest(TypedDict, closed=True):
    ciphertext_blob: NotRequired["capo_kms.types.ciphertext_type.CiphertextType"]
    """<p>Ciphertext to be decrypted. The blob includes metadata.</p> <p>This parameter is required in all cases except when <code>DryRun</code> is <code>true</code> and <code>DryRunModifiers</code> is set to <code>IGNORE_CIPHERTEXT</code>.</p>"""
    encryption_context: NotRequired[
        "capo_kms.types.encryption_context_type.EncryptionContextType"
    ]
    """<p>Specifies the encryption context to use when decrypting the data. An encryption context is valid only for <a href="https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations">cryptographic operations</a> with a symmetric encryption KMS key. The standard asymmetric encryption algorithms and HMAC algorithms that KMS uses do not support an encryption context.</p> <p>An <i>encryption context</i> is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html">Encryption context</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    grant_tokens: NotRequired["capo_kms.types.grant_token_list.GrantTokenList"]
    """<p>A list of grant tokens. </p> <p>Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved <i>eventual consistency</i>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token">Grant token</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html">Using a grant token</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>Specifies the KMS key that KMS uses to decrypt the ciphertext.</p> <p>Enter a key ID of the KMS key that was used to encrypt the ciphertext. If you identify a different KMS key, the <code>Decrypt</code> operation throws an <code>IncorrectKeyException</code>.</p> <p>This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key or when <code>DryRun</code> is <code>true</code> and <code>DryRunModifiers</code> is set to <code>IGNORE_CIPHERTEXT</code>. If you used a symmetric encryption KMS key, KMS can get the KMS key from metadata that it adds to the symmetric ciphertext blob. However, it is always recommended as a best practice. This practice ensures that you use the KMS key that you intend.</p> <p>To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with <code>"alias/"</code>. To specify a KMS key in a different Amazon Web Services account, you should use the key ARN or alias ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias ARN: <code>arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>. To get the alias name and alias ARN, use <a>ListAliases</a>.</p>"""
    encryption_algorithm: NotRequired[
        "capo_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
    ]
    """<p>Specifies the encryption algorithm that will be used to decrypt the ciphertext. Specify the same algorithm that was used to encrypt the data. If you specify a different algorithm, the <code>Decrypt</code> operation fails.</p> <p>This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key. The default value, <code>SYMMETRIC_DEFAULT</code>, represents the only supported algorithm that is valid for symmetric encryption KMS keys.</p>"""
    recipient: NotRequired["capo_kms.types.recipient_info.RecipientInfo"]
    """<p>A signed <a href="https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-concepts.html#term-attestdoc">attestation document</a> from an Amazon Web Services Nitro enclave or NitroTPM, and the encryption algorithm to use with the public key in the attestation document. The only valid encryption algorithm is <code>RSAES_OAEP_SHA_256</code>. </p> <p>This parameter supports the <a href="https://docs.aws.amazon.com/enclaves/latest/user/developing-applications.html#sdk">Amazon Web Services Nitro Enclaves SDK</a> or any Amazon Web Services SDK for Amazon Web Services Nitro Enclaves. It supports any Amazon Web Services SDK for Amazon Web Services NitroTPM. </p> <p>When you use this parameter, instead of returning the plaintext data, KMS encrypts the plaintext data with the public key in the attestation document, and returns the resulting ciphertext in the <code>CiphertextForRecipient</code> field in the response. This ciphertext can be decrypted only with the private key in the attested environment. The <code>Plaintext</code> field in the response is null or empty.</p> <p>For information about the interaction between KMS and Amazon Web Services Nitro Enclaves or Amazon Web Services NitroTPM, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html">Cryptographic attestation support in KMS</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    dry_run: NotRequired["capo_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    dry_run_modifiers: NotRequired[
        "capo_kms.types.dry_run_modifier_list.DryRunModifierList"
    ]
    """<p>Specifies the modifiers to apply to the dry run operation. <code>DryRunModifiers</code> is an optional parameter that only applies when <code>DryRun</code> is set to <code>true</code>.</p> <p>When set to <code>IGNORE_CIPHERTEXT</code>, KMS performs only authorization validation without ciphertext validation. This allows you to test permissions without requiring a valid ciphertext blob.</p> <p>To learn more about how to use this parameter, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DecryptRequest) -> dict:
    out: dict = {}
    if "ciphertext_blob" in value:
        import capo_kms.types.ciphertext_type

        out["CiphertextBlob"] = capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
            value["ciphertext_blob"]
        )
    if "encryption_context" in value:
        import capo_kms.types.encryption_context_type

        out["EncryptionContext"] = (
            capo_kms.types.encryption_context_type.serialize_aws_json_1_1(
                value["encryption_context"]
            )
        )
    if "grant_tokens" in value:
        import capo_kms.types.grant_token_list

        out["GrantTokens"] = capo_kms.types.grant_token_list.serialize_aws_json_1_1(
            value["grant_tokens"]
        )
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "encryption_algorithm" in value:
        import capo_kms.types.encryption_algorithm_spec

        out["EncryptionAlgorithm"] = (
            capo_kms.types.encryption_algorithm_spec.serialize_aws_json_1_1(
                value["encryption_algorithm"]
            )
        )
    if "recipient" in value:
        import capo_kms.types.recipient_info

        out["Recipient"] = capo_kms.types.recipient_info.serialize_aws_json_1_1(
            value["recipient"]
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "dry_run_modifiers" in value:
        import capo_kms.types.dry_run_modifier_list

        out["DryRunModifiers"] = (
            capo_kms.types.dry_run_modifier_list.serialize_aws_json_1_1(
                value["dry_run_modifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DecryptRequest:
    out: DecryptRequest = {}  # type: ignore[typeddict-item]
    if data.get("CiphertextBlob") is not None:
        import capo_kms.types.ciphertext_type

        out["ciphertext_blob"] = (
            capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["CiphertextBlob"]
            )
        )
    if data.get("EncryptionContext") is not None:
        import capo_kms.types.encryption_context_type

        out["encryption_context"] = (
            capo_kms.types.encryption_context_type.deserialize_aws_json_1_1(
                data["EncryptionContext"]
            )
        )
    if data.get("GrantTokens") is not None:
        import capo_kms.types.grant_token_list

        out["grant_tokens"] = capo_kms.types.grant_token_list.deserialize_aws_json_1_1(
            data["GrantTokens"]
        )
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("EncryptionAlgorithm") is not None:
        import capo_kms.types.encryption_algorithm_spec

        out["encryption_algorithm"] = (
            capo_kms.types.encryption_algorithm_spec.deserialize_aws_json_1_1(
                data["EncryptionAlgorithm"]
            )
        )
    if data.get("Recipient") is not None:
        import capo_kms.types.recipient_info

        out["recipient"] = capo_kms.types.recipient_info.deserialize_aws_json_1_1(
            data["Recipient"]
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    if data.get("DryRunModifiers") is not None:
        import capo_kms.types.dry_run_modifier_list

        out["dry_run_modifiers"] = (
            capo_kms.types.dry_run_modifier_list.deserialize_aws_json_1_1(
                data["DryRunModifiers"]
            )
        )
    return out
