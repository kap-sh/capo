"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.idempotence_token
    import capo_lookoutequipment.types.policy
    import capo_lookoutequipment.types.policy_revision_id
    import capo_lookoutequipment.types.resource_arn


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_lookoutequipment.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which the policy is being created.</p>"""
    resource_policy: "capo_lookoutequipment.types.policy.Policy"
    """<p>The JSON-formatted resource policy to create.</p>"""
    policy_revision_id: NotRequired[
        "capo_lookoutequipment.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>A unique identifier for a revision of the resource policy.</p>"""
    client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["ResourcePolicy"] = value["resource_policy"]
    if "policy_revision_id" in value:
        out["PolicyRevisionId"] = value["policy_revision_id"]
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    else:
        out["resource_policy"] = ""
    if data.get("PolicyRevisionId") is not None:
        out["policy_revision_id"] = data["PolicyRevisionId"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    return out
