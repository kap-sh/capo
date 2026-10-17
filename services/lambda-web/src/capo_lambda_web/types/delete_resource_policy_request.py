"""Generated from Smithy shape ``com.amazonaws.lambdaweb#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_web.types.policy_revision_id
    import capo_lambda_web.types.resource_arn


class DeleteResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_lambda_web.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web function.</p>"""
    revision_id: NotRequired[
        "capo_lambda_web.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>The revision ID of the policy. Use this to prevent deleting a policy that has been updated since you last retrieved it. If you don't specify a value, the policy is deleted regardless of its current revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
