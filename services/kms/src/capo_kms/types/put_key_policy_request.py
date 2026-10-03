"""Generated from Smithy shape ``com.amazonaws.kms#PutKeyPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.boolean_type
    import capo_kms.types.key_id_type
    import capo_kms.types.policy_name_type
    import capo_kms.types.policy_type


class PutKeyPolicyRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Sets the key policy on the specified KMS key.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    policy_name: NotRequired["capo_kms.types.policy_name_type.PolicyNameType"]
    """<p>The name of the key policy. If no policy name is specified, the default value is <code>default</code>. The only valid value is <code>default</code>.</p>"""
    policy: "capo_kms.types.policy_type.PolicyType"
    r"""<p>The key policy to attach to the KMS key.</p> <p>The key policy must meet the following criteria:</p> <ul> <li> <p>The key policy must allow the calling principal to make a subsequent <code>PutKeyPolicy</code> request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key">Default key policy</a> in the <i>Key Management Service Developer Guide</i>. (To omit this condition, set <code>BypassPolicyLockoutSafetyCheck</code> to true.)</p> </li> <li> <p>Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to KMS. When you create a new Amazon Web Services principal, you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to KMS. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency">Changes that I make are not always immediately visible</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p> </li> </ul> <note> <p>If either of the required <code>Resource</code> or <code>Action</code> elements are missing from a key policy statement, the policy statement has no effect. When a key policy statement is missing one of these elements, the KMS console correctly reports an error, but the <code>PutKeyPolicy</code> API request succeeds, even though the policy statement is ineffective.</p> <p>For more information on required key policy elements, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-overview.html#key-policy-elements">Elements in a key policy</a> in the <i>Key Management Service Developer Guide</i>.</p> </note> <p>A key policy document can include only the following characters:</p> <ul> <li> <p>Printable ASCII characters from the space character (<code>\u0020</code>) through the end of the ASCII character range.</p> </li> <li> <p>Printable characters in the Basic Latin and Latin-1 Supplement character set (through <code>\u00FF</code>).</p> </li> <li> <p>The tab (<code>\u0009</code>), line feed (<code>\u000A</code>), and carriage return (<code>\u000D</code>) special characters</p> </li> </ul> <note> <p>If the key policy exceeds the length constraint, KMS returns a <code>LimitExceededException</code>.</p> </note> <p>For information about key policies, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html">Key policies in KMS</a> in the <i>Key Management Service Developer Guide</i>.For help writing and formatting a JSON policy document, see the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html">IAM JSON Policy Reference</a> in the <i> <i>Identity and Access Management User Guide</i> </i>.</p>"""
    bypass_policy_lockout_safety_check: "capo_kms.types.boolean_type.BooleanType"
    """<p>Skips ("bypasses") the key policy lockout safety check. The default value is false.</p> <important> <p>Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key">Default key policy</a> in the <i>Key Management Service Developer Guide</i>.</p> </important> <p>Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html">PutKeyPolicy</a> request on the KMS key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutKeyPolicyRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    out["Policy"] = value["policy"]
    out["BypassPolicyLockoutSafetyCheck"] = value.get(
        "bypass_policy_lockout_safety_check", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutKeyPolicyRequest:
    out: PutKeyPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("PutKeyPolicyRequest.key_id required")
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutKeyPolicyRequest.policy required")
    if data.get("BypassPolicyLockoutSafetyCheck") is not None:
        out["bypass_policy_lockout_safety_check"] = data[
            "BypassPolicyLockoutSafetyCheck"
        ]
    else:
        out["bypass_policy_lockout_safety_check"] = False
    return out
