"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTestCaseList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_test_case

AutomatedReasoningPolicyTestCaseList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_test_case.AutomatedReasoningPolicyTestCase"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyTestCaseList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_test_case

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_test_case.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyTestCaseList:
    import capo_bedrock.types.automated_reasoning_policy_test_case

    out: AutomatedReasoningPolicyTestCaseList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_test_case.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyTestCaseList) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_test_case

    return [
        capo_bedrock.types.automated_reasoning_policy_test_case.redact_sensitive(item)
        for item in value
    ]
