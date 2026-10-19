"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateAutomatedReasoningPolicyTestCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_test_case_id


class CreateAutomatedReasoningPolicyTestCaseResponse(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the policy for which the test was created.</p>"""
    test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId"
    """<p>The unique identifier of the created test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomatedReasoningPolicyTestCaseResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["testCaseId"] = value["test_case_id"]
    return out


def deserialize_json(data: dict) -> CreateAutomatedReasoningPolicyTestCaseResponse:
    out: CreateAutomatedReasoningPolicyTestCaseResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        out["policy_arn"] = ""
    if data.get("testCaseId") is not None:
        out["test_case_id"] = data["testCaseId"]
    else:
        out["test_case_id"] = ""
    return out
