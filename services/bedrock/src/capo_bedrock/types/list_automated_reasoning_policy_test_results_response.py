"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAutomatedReasoningPolicyTestResultsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_test_list
    import capo_bedrock.types.pagination_token


class ListAutomatedReasoningPolicyTestResultsResponse(TypedDict, closed=True):
    test_results: "capo_bedrock.types.automated_reasoning_policy_test_list.AutomatedReasoningPolicyTestList"
    """<p>A list of test results, each containing information about how the policy performed on specific test scenarios.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>A pagination token to use in subsequent requests to retrieve additional test results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedReasoningPolicyTestResultsResponse) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_test_list

    out["testResults"] = (
        capo_bedrock.types.automated_reasoning_policy_test_list.serialize_json(
            value["test_results"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAutomatedReasoningPolicyTestResultsResponse:
    out: ListAutomatedReasoningPolicyTestResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("testResults") is not None:
        import capo_bedrock.types.automated_reasoning_policy_test_list

        out["test_results"] = (
            capo_bedrock.types.automated_reasoning_policy_test_list.deserialize_json(
                data["testResults"]
            )
        )
    else:
        raise DeserializationError(
            "ListAutomatedReasoningPolicyTestResultsResponse.test_results required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(
    value: ListAutomatedReasoningPolicyTestResultsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "test_results" in value:
        import capo_bedrock.types.automated_reasoning_policy_test_list

        out["test_results"] = (
            capo_bedrock.types.automated_reasoning_policy_test_list.redact_sensitive(
                value["test_results"]
            )
        )
    return out
