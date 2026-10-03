"""Generated from Smithy shape ``com.amazonaws.kms#SignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.grant_token_list
    import capo_kms.types.key_id_type
    import capo_kms.types.message_type
    import capo_kms.types.nullable_boolean_type
    import capo_kms.types.plaintext_type
    import capo_kms.types.signing_algorithm_spec


class SignRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Identifies an asymmetric KMS key. KMS uses the private key in the asymmetric KMS key to sign the message. The <code>KeyUsage</code> type of the KMS key must be <code>SIGN_VERIFY</code>. To find the <code>KeyUsage</code> of a KMS key, use the <a>DescribeKey</a> operation.</p> <p>To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with <code>"alias/"</code>. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias ARN: <code>arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>. To get the alias name and alias ARN, use <a>ListAliases</a>.</p>"""
    message: "capo_kms.types.plaintext_type.PlaintextType"
    """<p>Specifies the message or message digest to sign. Messages can be 0-4096 bytes. To sign a larger message, provide a message digest.</p> <p>If you provide a message digest, use the <code>DIGEST</code> value of <code>MessageType</code> to prevent the digest from being hashed again while signing.</p>"""
    message_type: NotRequired["capo_kms.types.message_type.MessageType"]
    """<p>Tells KMS whether the value of the <code>Message</code> parameter should be hashed as part of the signing algorithm. Use <code>RAW</code> for unhashed messages; use <code>DIGEST</code> for message digests, which are already hashed; use <code>EXTERNAL_MU</code> for 64-byte representative μ used in ML-DSA signing as defined in NIST FIPS 204 Section 6.2.</p> <p>When the value of <code>MessageType</code> is <code>RAW</code>, KMS uses the standard signing algorithm, which begins with a hash function. When the value is <code>DIGEST</code>, KMS skips the hashing step in the signing algorithm. When the value is <code>EXTERNAL_MU</code> KMS skips the concatenated hashing of the public key hash and the message done in the ML-DSA signing algorithm.</p> <important> <p>Use the <code>DIGEST</code> or <code>EXTERNAL_MU</code> value only when the value of the <code>Message</code> parameter is a message digest. If you use the <code>DIGEST</code> value with an unhashed message, the security of the signing operation can be compromised.</p> </important> <p>When using ECC_NIST_EDWARDS25519 KMS keys:</p> <ul> <li> <p>ED25519_SHA_512 signing algorithm requires KMS <code>MessageType:RAW</code> </p> </li> <li> <p>ED25519_PH_SHA_512 signing algorithm requires KMS <code>MessageType:DIGEST</code> </p> </li> </ul> <important> <p>When you specify the ED25519_PH_SHA_512 signing algorithm with <code>MessageType:DIGEST</code>, KMS still performs the SHA-512 prehash described in <a href="https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-5.pdf#page=39">Step 1 of Section 7.8.1 in FIPS 186-5</a>. This means the input is hashed twice: once by you and once by KMS. </p> </important> <p>When the value of <code>MessageType</code> is <code>DIGEST</code>, the length of the <code>Message</code> value must match the length of hashed messages for the specified signing algorithm.</p> <p>When the value of <code>MessageType</code> is <code>EXTERNAL_MU</code> the length of the <code>Message</code> value must be 64 bytes.</p> <p>You can submit a message digest and omit the <code>MessageType</code> or specify <code>RAW</code> so the digest is hashed again while signing. However, this can cause verification failures when verifying with a system that assumes a single hash.</p> <p>The hashing algorithm that <code>Sign</code> uses is based on the <code>SigningAlgorithm</code> value.</p> <ul> <li> <p>Signing algorithms that end in SHA_256 use the SHA_256 hashing algorithm.</p> </li> <li> <p>Signing algorithms that end in SHA_384 use the SHA_384 hashing algorithm.</p> </li> <li> <p>Signing algorithms that end in SHA_512 use the SHA_512 hashing algorithm.</p> </li> <li> <p>Signing algorithms that end in SHAKE_256 use the SHAKE_256 hashing algorithm.</p> </li> <li> <p>SM2DSA uses the SM3 hashing algorithm. For details, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/offline-operations.html#key-spec-sm-offline-verification">Offline verification with SM2 key pairs</a>.</p> </li> </ul>"""
    grant_tokens: NotRequired["capo_kms.types.grant_token_list.GrantTokenList"]
    """<p>A list of grant tokens.</p> <p>Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved <i>eventual consistency</i>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token">Grant token</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html">Using a grant token</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    signing_algorithm: "capo_kms.types.signing_algorithm_spec.SigningAlgorithmSpec"
    """<p>Specifies the signing algorithm to use when signing the message. </p> <p>Choose an algorithm that is compatible with the type and size of the specified asymmetric KMS key. When signing with RSA key pairs, RSASSA-PSS algorithms are preferred. We include RSASSA-PKCS1-v1_5 algorithms for compatibility with existing applications.</p>"""
    dry_run: NotRequired["capo_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    import capo_kms.types.plaintext_type

    out["Message"] = capo_kms.types.plaintext_type.serialize_aws_json_1_1(
        value["message"]
    )
    if "message_type" in value:
        import capo_kms.types.message_type

        out["MessageType"] = capo_kms.types.message_type.serialize_aws_json_1_1(
            value["message_type"]
        )
    if "grant_tokens" in value:
        import capo_kms.types.grant_token_list

        out["GrantTokens"] = capo_kms.types.grant_token_list.serialize_aws_json_1_1(
            value["grant_tokens"]
        )
    import capo_kms.types.signing_algorithm_spec

    out["SigningAlgorithm"] = (
        capo_kms.types.signing_algorithm_spec.serialize_aws_json_1_1(
            value["signing_algorithm"]
        )
    )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SignRequest:
    out: SignRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("SignRequest.key_id required")
    if data.get("Message") is not None:
        import capo_kms.types.plaintext_type

        out["message"] = capo_kms.types.plaintext_type.deserialize_aws_json_1_1(
            data["Message"]
        )
    else:
        raise DeserializationError("SignRequest.message required")
    if data.get("MessageType") is not None:
        import capo_kms.types.message_type

        out["message_type"] = capo_kms.types.message_type.deserialize_aws_json_1_1(
            data["MessageType"]
        )
    if data.get("GrantTokens") is not None:
        import capo_kms.types.grant_token_list

        out["grant_tokens"] = capo_kms.types.grant_token_list.deserialize_aws_json_1_1(
            data["GrantTokens"]
        )
    if data.get("SigningAlgorithm") is not None:
        import capo_kms.types.signing_algorithm_spec

        out["signing_algorithm"] = (
            capo_kms.types.signing_algorithm_spec.deserialize_aws_json_1_1(
                data["SigningAlgorithm"]
            )
        )
    else:
        raise DeserializationError("SignRequest.signing_algorithm required")
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
