"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateAutomatedReasoningPolicyTestCaseRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_result
    import capo_bedrock.types.automated_reasoning_check_translation_confidence
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_test_guard_content
    import capo_bedrock.types.automated_reasoning_policy_test_query_content
    import capo_bedrock.types.idempotency_token


class CreateAutomatedReasoningPolicyTestCaseRequest(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create the test.</p>"""
    guard_content: "capo_bedrock.types.automated_reasoning_policy_test_guard_content.AutomatedReasoningPolicyTestGuardContent"
    """<p>The output content that's validated by the Automated Reasoning policy. This represents the foundation model response that will be checked for accuracy.</p>"""
    query_content: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_test_query_content.AutomatedReasoningPolicyTestQueryContent"
    ]
    """<p>The input query or prompt that generated the content. This provides context for the validation.</p>"""
    expected_aggregated_findings_result: "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult"
    """<p>The expected result of the Automated Reasoning check. Valid values include: , TOO_COMPLEX, and NO_TRANSLATIONS.</p> <ul> <li> <p> <code>VALID</code> - The claims are true. The claims are implied by the premises and the Automated Reasoning policy. Given the Automated Reasoning policy and premises, it is not possible for these claims to be false. In other words, there are no alternative answers that are true that contradict the claims.</p> </li> <li> <p> <code>INVALID</code> - The claims are false. The claims are not implied by the premises and Automated Reasoning policy. Furthermore, there exists different claims that are consistent with the premises and Automated Reasoning policy.</p> </li> <li> <p> <code>SATISFIABLE</code> - The claims can be true or false. It depends on what assumptions are made for the claim to be implied from the premises and Automated Reasoning policy rules. In this situation, different assumptions can make input claims false and alternative claims true.</p> </li> <li> <p> <code>IMPOSSIBLE</code> - Automated Reasoning can’t make a statement about the claims. This can happen if the premises are logically incorrect, or if there is a conflict within the Automated Reasoning policy itself.</p> </li> <li> <p> <code>TRANSLATION_AMBIGUOUS</code> - Detected an ambiguity in the translation meant it would be unsound to continue with validity checking. Additional context or follow-up questions might be needed to get translation to succeed.</p> </li> <li> <p> <code>TOO_COMPLEX</code> - The input contains too much information for Automated Reasoning to process within its latency limits.</p> </li> <li> <p> <code>NO_TRANSLATIONS</code> - Identifies that some or all of the input prompt wasn't translated into logic. This can happen if the input isn't relevant to the Automated Reasoning policy, or if the policy doesn't have variables to model relevant input. If Automated Reasoning can't translate anything, you get a single <code>NO_TRANSLATIONS</code> finding. You might also see a <code>NO_TRANSLATIONS</code> (along with other findings) if some part of the validation isn't translated.</p> </li> </ul>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>"""
    confidence_threshold: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
    ]
    """<p>The minimum confidence level for logic validation. Content that meets the threshold is considered a high-confidence finding that can be validated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomatedReasoningPolicyTestCaseRequest) -> dict:
    out: dict = {}
    out["guardContent"] = value["guard_content"]
    if "query_content" in value:
        out["queryContent"] = value["query_content"]
    import capo_bedrock.types.automated_reasoning_check_result

    out["expectedAggregatedFindingsResult"] = (
        capo_bedrock.types.automated_reasoning_check_result.serialize_json(
            value["expected_aggregated_findings_result"]
        )
    )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "confidence_threshold" in value:
        out["confidenceThreshold"] = (
            "NaN"
            if value["confidence_threshold"] != value["confidence_threshold"]
            else "Infinity"
            if value["confidence_threshold"] == float("inf")
            else "-Infinity"
            if value["confidence_threshold"] == float("-inf")
            else value["confidence_threshold"]
        )
    return out


def deserialize_json(data: dict) -> CreateAutomatedReasoningPolicyTestCaseRequest:
    out: CreateAutomatedReasoningPolicyTestCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("guardContent") is not None:
        out["guard_content"] = data["guardContent"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyTestCaseRequest.guard_content required"
        )
    if data.get("queryContent") is not None:
        out["query_content"] = data["queryContent"]
    if data.get("expectedAggregatedFindingsResult") is not None:
        import capo_bedrock.types.automated_reasoning_check_result

        out["expected_aggregated_findings_result"] = (
            capo_bedrock.types.automated_reasoning_check_result.deserialize_json(
                data["expectedAggregatedFindingsResult"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyTestCaseRequest.expected_aggregated_findings_result required"
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("confidenceThreshold") is not None:
        out["confidence_threshold"] = float(data["confidenceThreshold"])
    return out


def redact_sensitive(
    value: CreateAutomatedReasoningPolicyTestCaseRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "guard_content" in value:
        out["guard_content"] = "*** Sensitive Data Redacted ***"
    if "query_content" in value:
        out["query_content"] = "*** Sensitive Data Redacted ***"
    return out
