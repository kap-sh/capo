"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteAutomatedReasoningPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn


class DeleteAutomatedReasoningPolicyRequest(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to delete.</p>"""
    force: NotRequired["bool"]
    """<p>Specifies whether to force delete the automated reasoning policy even if it has active resources. When <code>false</code>, Amazon Bedrock validates if all artifacts have been deleted (e.g. policy version, test case, test result) for a policy before deletion. When <code>true</code>, Amazon Bedrock will delete the policy and all its artifacts without validation. Default is <code>false</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAutomatedReasoningPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAutomatedReasoningPolicyRequest:
    out: DeleteAutomatedReasoningPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
