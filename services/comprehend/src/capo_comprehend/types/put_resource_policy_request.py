"""Generated from Smithy shape ``com.amazonaws.comprehend#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.policy
    import capo_comprehend.types.policy_revision_id


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    """<p>The Amazon Resource Name (ARN) of the custom model to attach the policy to.</p>"""
    resource_policy: "capo_comprehend.types.policy.Policy"
    r"""<p>The JSON resource-based policy to attach to your custom model. Provide your JSON as a UTF-8 encoded string without line breaks. To provide valid JSON for your policy, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:</p> <p> <code>"{\"attribute\": \"value\", \"attribute\": [\"value\"]}"</code> </p> <p>To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:</p> <p> <code>'{"attribute": "value", "attribute": ["value"]}'</code> </p>"""
    policy_revision_id: NotRequired[
        "capo_comprehend.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>The revision ID that Amazon Comprehend assigned to the policy that you are updating. If you are creating a new policy that has no prior version, don't use this parameter. Amazon Comprehend creates the revision ID for you.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["ResourcePolicy"] = value["resource_policy"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_arn required")
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_policy required")
    if data.get("PolicyRevisionId") is not None:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    return out
