"""Generated from Smithy shape ``com.amazonaws.kms#GenerateMacRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.grant_token_list
    import capo_kms.types.key_id_type
    import capo_kms.types.mac_algorithm_spec
    import capo_kms.types.nullable_boolean_type
    import capo_kms.types.plaintext_type


class GenerateMacRequest(TypedDict, closed=True):
    message: "capo_kms.types.plaintext_type.PlaintextType"
    """<p>The message to be hashed. Specify a message of up to 4,096 bytes. </p> <p> <code>GenerateMac</code> and <a>VerifyMac</a> do not provide special handling for message digests. If you generate an HMAC for a hash digest of a message, you must verify the HMAC of the same hash digest.</p>"""
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>The HMAC KMS key to use in the operation. The MAC algorithm computes the HMAC for the message and the key as described in <a href="https://datatracker.ietf.org/doc/html/rfc2104">RFC 2104</a>.</p> <p>To identify an HMAC KMS key, use the <a>DescribeKey</a> operation and see the <code>KeySpec</code> field in the response.</p>"""
    mac_algorithm: "capo_kms.types.mac_algorithm_spec.MacAlgorithmSpec"
    """<p>The MAC algorithm used in the operation.</p> <p> The algorithm must be compatible with the HMAC KMS key that you specify. To find the MAC algorithms that your HMAC KMS key supports, use the <a>DescribeKey</a> operation and see the <code>MacAlgorithms</code> field in the <code>DescribeKey</code> response.</p>"""
    grant_tokens: NotRequired["capo_kms.types.grant_token_list.GrantTokenList"]
    """<p>A list of grant tokens.</p> <p>Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved <i>eventual consistency</i>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token">Grant token</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html">Using a grant token</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    dry_run: NotRequired["capo_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateMacRequest) -> dict:
    out: dict = {}
    import capo_kms.types.plaintext_type

    out["Message"] = capo_kms.types.plaintext_type.serialize_aws_json_1_1(
        value["message"]
    )
    out["KeyId"] = value["key_id"]
    import capo_kms.types.mac_algorithm_spec

    out["MacAlgorithm"] = capo_kms.types.mac_algorithm_spec.serialize_aws_json_1_1(
        value["mac_algorithm"]
    )
    if "grant_tokens" in value:
        import capo_kms.types.grant_token_list

        out["GrantTokens"] = capo_kms.types.grant_token_list.serialize_aws_json_1_1(
            value["grant_tokens"]
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateMacRequest:
    out: GenerateMacRequest = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        import capo_kms.types.plaintext_type

        out["message"] = capo_kms.types.plaintext_type.deserialize_aws_json_1_1(
            data["Message"]
        )
    else:
        raise DeserializationError("GenerateMacRequest.message required")
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("GenerateMacRequest.key_id required")
    if data.get("MacAlgorithm") is not None:
        import capo_kms.types.mac_algorithm_spec

        out["mac_algorithm"] = (
            capo_kms.types.mac_algorithm_spec.deserialize_aws_json_1_1(
                data["MacAlgorithm"]
            )
        )
    else:
        raise DeserializationError("GenerateMacRequest.mac_algorithm required")
    if data.get("GrantTokens") is not None:
        import capo_kms.types.grant_token_list

        out["grant_tokens"] = capo_kms.types.grant_token_list.deserialize_aws_json_1_1(
            data["GrantTokens"]
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
