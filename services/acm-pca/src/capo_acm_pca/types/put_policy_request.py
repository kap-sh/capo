"""Generated from Smithy shape ``com.amazonaws.acmpca#PutPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.arn
    import capo_acm_pca.types.aws_policy


class PutPolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_acm_pca.types.arn.Arn"
    """<p>The Amazon Resource Number (ARN) of the private CA to associate with the policy. The ARN of the CA can be found by calling the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html">ListCertificateAuthorities</a> action.</p> <p/>"""
    policy: "capo_acm_pca.types.aws_policy.AWSPolicy"
    """<p>The path and file name of a JSON-formatted IAM policy to attach to the specified private CA resource. If this policy does not contain all required statements or if it includes any statement that is not allowed, the <code>PutPolicy</code> action returns an <code>InvalidPolicyException</code>. For information about IAM policy and statement structure, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json">Overview of JSON Policies</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPolicyRequest:
    out: PutPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutPolicyRequest.resource_arn required")
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutPolicyRequest.policy required")
    return out
