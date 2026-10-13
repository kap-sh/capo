"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyGeneratedTestCaseList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_generated_test_case

AutomatedReasoningPolicyGeneratedTestCaseList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_generated_test_case.AutomatedReasoningPolicyGeneratedTestCase"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyGeneratedTestCaseList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_generated_test_case

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_generated_test_case.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyGeneratedTestCaseList:
    import capo_bedrock.types.automated_reasoning_policy_generated_test_case

    out: AutomatedReasoningPolicyGeneratedTestCaseList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_generated_test_case.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyGeneratedTestCaseList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_generated_test_case

    return [
        capo_bedrock.types.automated_reasoning_policy_generated_test_case.redact_sensitive(
            item
        )
        for item in value
    ]
