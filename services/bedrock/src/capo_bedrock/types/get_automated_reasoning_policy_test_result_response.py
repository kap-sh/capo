"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyTestResultResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_test_result


class GetAutomatedReasoningPolicyTestResultResponse(TypedDict, closed=True):
    test_result: "capo_bedrock.types.automated_reasoning_policy_test_result.AutomatedReasoningPolicyTestResult"
    """<p>The test result containing validation findings, execution status, and detailed analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyTestResultResponse) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_test_result

    out["testResult"] = (
        capo_bedrock.types.automated_reasoning_policy_test_result.serialize_json(
            value["test_result"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyTestResultResponse:
    out: GetAutomatedReasoningPolicyTestResultResponse = {}  # type: ignore[typeddict-item]
    if data.get("testResult") is not None:
        import capo_bedrock.types.automated_reasoning_policy_test_result

        out["test_result"] = (
            capo_bedrock.types.automated_reasoning_policy_test_result.deserialize_json(
                data["testResult"]
            )
        )
    else:
        raise DeserializationError(
            "GetAutomatedReasoningPolicyTestResultResponse.test_result required"
        )
    return out


def redact_sensitive(
    value: GetAutomatedReasoningPolicyTestResultResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "test_result" in value:
        import capo_bedrock.types.automated_reasoning_policy_test_result

        out["test_result"] = (
            capo_bedrock.types.automated_reasoning_policy_test_result.redact_sensitive(
                value["test_result"]
            )
        )
    return out
