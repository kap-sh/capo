"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyGeneratedTestCase``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_result
    import capo_bedrock.types.automated_reasoning_policy_test_guard_content
    import capo_bedrock.types.automated_reasoning_policy_test_query_content


class AutomatedReasoningPolicyGeneratedTestCase(TypedDict, closed=True):
    query_content: "capo_bedrock.types.automated_reasoning_policy_test_query_content.AutomatedReasoningPolicyTestQueryContent"
    """<p>The input query or prompt that generated the content. This provides context for the validation.</p>"""
    guard_content: "capo_bedrock.types.automated_reasoning_policy_test_guard_content.AutomatedReasoningPolicyTestGuardContent"
    """<p>The output content that's validated by the Automated Reasoning policy. This represents the foundation model response that will be checked for accuracy.</p>"""
    expected_aggregated_findings_result: "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult"
    """<p>The expected results of the generated test case. Possible values include:</p> <ul> <li> <p> <code>VALID</code> - The claims are true. The claims are implied by the premises and the Automated Reasoning policy. Given the Automated Reasoning policy and premises, it is not possible for these claims to be false. In other words, there are no alternative answers that are true that contradict the claims.</p> </li> <li> <p> <code>INVALID</code> - The claims are false. The claims are not implied by the premises and Automated Reasoning policy. Furthermore, there exists different claims that are consistent with the premises and Automated Reasoning policy.</p> </li> <li> <p> <code>SATISFIABLE</code> - The claims can be true or false. It depends on what assumptions are made for the claim to be implied from the premises and Automated Reasoning policy rules. In this situation, different assumptions can make input claims false and alternative claims true.</p> </li> <li> <p> <code>IMPOSSIBLE</code> - Automated Reasoning can’t make a statement about the claims. This can happen if the premises are logically incorrect, or if there is a conflict within the Automated Reasoning policy itself.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyGeneratedTestCase) -> dict:
    out: dict = {}
    out["queryContent"] = value["query_content"]
    out["guardContent"] = value["guard_content"]
    import capo_bedrock.types.automated_reasoning_check_result

    out["expectedAggregatedFindingsResult"] = (
        capo_bedrock.types.automated_reasoning_check_result.serialize_json(
            value["expected_aggregated_findings_result"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyGeneratedTestCase:
    out: AutomatedReasoningPolicyGeneratedTestCase = {}  # type: ignore[typeddict-item]
    if data.get("queryContent") is not None:
        out["query_content"] = data["queryContent"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyGeneratedTestCase.query_content required"
        )
    if data.get("guardContent") is not None:
        out["guard_content"] = data["guardContent"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyGeneratedTestCase.guard_content required"
        )
    if data.get("expectedAggregatedFindingsResult") is not None:
        import capo_bedrock.types.automated_reasoning_check_result

        out["expected_aggregated_findings_result"] = (
            capo_bedrock.types.automated_reasoning_check_result.deserialize_json(
                data["expectedAggregatedFindingsResult"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyGeneratedTestCase.expected_aggregated_findings_result required"
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyGeneratedTestCase,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_content" in value:
        out["query_content"] = "*** Sensitive Data Redacted ***"
    if "guard_content" in value:
        out["guard_content"] = "*** Sensitive Data Redacted ***"
    return out
