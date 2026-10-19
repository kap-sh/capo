"""Generated from Smithy shape ``com.amazonaws.bedrock#StartAutomatedReasoningPolicyTestWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn


class StartAutomatedReasoningPolicyTestWorkflowResponse(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the policy for which the test workflow was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAutomatedReasoningPolicyTestWorkflowResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    return out


def deserialize_json(data: dict) -> StartAutomatedReasoningPolicyTestWorkflowResponse:
    out: StartAutomatedReasoningPolicyTestWorkflowResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        out["policy_arn"] = ""
    return out
