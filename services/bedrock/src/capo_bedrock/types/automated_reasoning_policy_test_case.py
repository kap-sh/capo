"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTestCase``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_result
    import capo_bedrock.types.automated_reasoning_check_translation_confidence
    import capo_bedrock.types.automated_reasoning_policy_test_case_id
    import capo_bedrock.types.automated_reasoning_policy_test_guard_content
    import capo_bedrock.types.automated_reasoning_policy_test_query_content
    import capo_bedrock.types.timestamp


class AutomatedReasoningPolicyTestCase(TypedDict, closed=True):
    test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId"
    """<p>The unique identifier of the test.</p>"""
    guard_content: "capo_bedrock.types.automated_reasoning_policy_test_guard_content.AutomatedReasoningPolicyTestGuardContent"
    """<p>The output content to be validated by the policy, typically representing a foundation model response.</p>"""
    query_content: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_test_query_content.AutomatedReasoningPolicyTestQueryContent"
    ]
    """<p>The input query or prompt that generated the content. This provides context for the validation.</p>"""
    expected_aggregated_findings_result: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult"
    ]
    """<p>The expected result of the Automated Reasoning check for this test.</p>"""
    created_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the test was created.</p>"""
    updated_at: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the test was last updated.</p>"""
    confidence_threshold: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
    ]
    """<p>The minimum confidence level for logic validation. Content meeting this threshold is considered high-confidence and can be validated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyTestCase) -> dict:
    out: dict = {}
    out["testCaseId"] = value["test_case_id"]
    out["guardContent"] = value["guard_content"]
    if "query_content" in value:
        out["queryContent"] = value["query_content"]
    if "expected_aggregated_findings_result" in value:
        import capo_bedrock.types.automated_reasoning_check_result

        out["expectedAggregatedFindingsResult"] = (
            capo_bedrock.types.automated_reasoning_check_result.serialize_json(
                value["expected_aggregated_findings_result"]
            )
        )
    import capo_bedrock.types.timestamp

    out["createdAt"] = capo_bedrock.types.timestamp.serialize_json(value["created_at"])
    import capo_bedrock.types.timestamp

    out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(value["updated_at"])
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


def deserialize_json(data: dict) -> AutomatedReasoningPolicyTestCase:
    out: AutomatedReasoningPolicyTestCase = {}  # type: ignore[typeddict-item]
    if data.get("testCaseId") is not None:
        out["test_case_id"] = data["testCaseId"]
    else:
        out["test_case_id"] = ""
    if data.get("guardContent") is not None:
        out["guard_content"] = data["guardContent"]
    else:
        out["guard_content"] = ""
    if data.get("queryContent") is not None:
        out["query_content"] = data["queryContent"]
    if data.get("expectedAggregatedFindingsResult") is not None:
        import capo_bedrock.types.automated_reasoning_check_result

        out["expected_aggregated_findings_result"] = (
            capo_bedrock.types.automated_reasoning_check_result.deserialize_json(
                data["expectedAggregatedFindingsResult"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_bedrock.types.timestamp

        out["created_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("confidenceThreshold") is not None:
        out["confidence_threshold"] = float(data["confidenceThreshold"])
    return out


def redact_sensitive(value: AutomatedReasoningPolicyTestCase) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "guard_content" in value:
        out["guard_content"] = "*** Sensitive Data Redacted ***"
    if "query_content" in value:
        out["query_content"] = "*** Sensitive Data Redacted ***"
    return out
