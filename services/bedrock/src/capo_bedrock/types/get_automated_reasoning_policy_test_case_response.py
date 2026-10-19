"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyTestCaseResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_test_case


class GetAutomatedReasoningPolicyTestCaseResponse(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the policy that contains the test.</p>"""
    test_case: "capo_bedrock.types.automated_reasoning_policy_test_case.AutomatedReasoningPolicyTestCase"
    """<p>The test details including the content, query, expected result, and metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyTestCaseResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    import capo_bedrock.types.automated_reasoning_policy_test_case

    out["testCase"] = (
        capo_bedrock.types.automated_reasoning_policy_test_case.serialize_json(
            value["test_case"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyTestCaseResponse:
    out: GetAutomatedReasoningPolicyTestCaseResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        out["policy_arn"] = ""
    if data.get("testCase") is not None:
        import capo_bedrock.types.automated_reasoning_policy_test_case

        out["test_case"] = (
            capo_bedrock.types.automated_reasoning_policy_test_case.deserialize_json(
                data["testCase"]
            )
        )
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyTestCaseResponse.test_case required"
        )
    return out


def redact_sensitive(
    value: GetAutomatedReasoningPolicyTestCaseResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "test_case" in value:
        import capo_bedrock.types.automated_reasoning_policy_test_case

        out["test_case"] = (
            capo_bedrock.types.automated_reasoning_policy_test_case.redact_sensitive(
                value["test_case"]
            )
        )
    return out
