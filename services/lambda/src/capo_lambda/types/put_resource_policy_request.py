"""Generated from Smithy shape ``com.amazonaws.lambda#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.policy_resource_arn
    import capo_lambda.types.resource_policy
    import capo_lambda.types.revision_id


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_lambda.types.policy_resource_arn.PolicyResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda resource you want to add the policy to. You can use a qualified or an unqualified ARN. The value must be a complete ARN, and the operation does not accept wildcard characters.</p>"""
    policy: "capo_lambda.types.resource_policy.ResourcePolicy"
    """<p>The policy document you want to add to your Lambda resource. This is formatted as a JSON string.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html">Working with resource-based policies in Lambda</a> in the <i>Lambda Developer Guide</i>.</p>"""
    revision_id: NotRequired["capo_lambda.types.revision_id.RevisionId"]
    """<p>The revision ID that the existing policy must match for the replacement to proceed. If the revision ID doesn't match, the operation fails with a <code>PreconditionFailedException</code> error. To retrieve the current revision ID, use the <a>GetResourcePolicy</a> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.policy required")
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    return out
