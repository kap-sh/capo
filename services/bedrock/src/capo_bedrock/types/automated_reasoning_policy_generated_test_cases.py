"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyGeneratedTestCases``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_generated_test_case_list


class AutomatedReasoningPolicyGeneratedTestCases(TypedDict, closed=True):
    generated_test_cases: "capo_bedrock.types.automated_reasoning_policy_generated_test_case_list.AutomatedReasoningPolicyGeneratedTestCaseList"
    """<p>Represents a collection of generated test cases.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyGeneratedTestCases) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_generated_test_case_list

    out["generatedTestCases"] = (
        capo_bedrock.types.automated_reasoning_policy_generated_test_case_list.serialize_json(
            value["generated_test_cases"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyGeneratedTestCases:
    out: AutomatedReasoningPolicyGeneratedTestCases = {}  # type: ignore[typeddict-item]
    if data.get("generatedTestCases") is not None:
        import capo_bedrock.types.automated_reasoning_policy_generated_test_case_list

        out["generated_test_cases"] = (
            capo_bedrock.types.automated_reasoning_policy_generated_test_case_list.deserialize_json(
                data["generatedTestCases"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyGeneratedTestCases.generated_test_cases required"
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyGeneratedTestCases,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "generated_test_cases" in value:
        import capo_bedrock.types.automated_reasoning_policy_generated_test_case_list

        out["generated_test_cases"] = (
            capo_bedrock.types.automated_reasoning_policy_generated_test_case_list.redact_sensitive(
                value["generated_test_cases"]
            )
        )
    return out
