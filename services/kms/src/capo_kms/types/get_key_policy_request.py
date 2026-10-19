"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.key_id_type
    import capo_kms.types.policy_name_type


class GetKeyPolicyRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Gets the key policy for the specified KMS key.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    policy_name: NotRequired["capo_kms.types.policy_name_type.PolicyNameType"]
    """<p>Specifies the name of the key policy. If no policy name is specified, the default value is <code>default</code>. The only valid name is <code>default</code>. To get the names of key policies, use <a>ListKeyPolicies</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKeyPolicyRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKeyPolicyRequest:
    out: GetKeyPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        out["key_id"] = ""
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    return out
