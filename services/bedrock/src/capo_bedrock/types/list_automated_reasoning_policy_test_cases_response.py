"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAutomatedReasoningPolicyTestCasesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_test_case_list
    import capo_bedrock.types.pagination_token


class ListAutomatedReasoningPolicyTestCasesResponse(TypedDict, closed=True):
    test_cases: "capo_bedrock.types.automated_reasoning_policy_test_case_list.AutomatedReasoningPolicyTestCaseList"
    """<p>A list of tests for the specified policy.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>The pagination token to use in a subsequent request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedReasoningPolicyTestCasesResponse) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_test_case_list

    out["testCases"] = (
        capo_bedrock.types.automated_reasoning_policy_test_case_list.serialize_json(
            value["test_cases"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAutomatedReasoningPolicyTestCasesResponse:
    out: ListAutomatedReasoningPolicyTestCasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("testCases") is not None:
        import capo_bedrock.types.automated_reasoning_policy_test_case_list

        out["test_cases"] = (
            capo_bedrock.types.automated_reasoning_policy_test_case_list.deserialize_json(
                data["testCases"]
            )
        )
    else:
        out["test_cases"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(
    value: ListAutomatedReasoningPolicyTestCasesResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "test_cases" in value:
        import capo_bedrock.types.automated_reasoning_policy_test_case_list

        out["test_cases"] = (
            capo_bedrock.types.automated_reasoning_policy_test_case_list.redact_sensitive(
                value["test_cases"]
            )
        )
    return out
