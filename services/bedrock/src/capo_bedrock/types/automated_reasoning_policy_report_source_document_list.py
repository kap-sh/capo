"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyReportSourceDocumentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_report_source_document

AutomatedReasoningPolicyReportSourceDocumentList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_report_source_document.AutomatedReasoningPolicyReportSourceDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyReportSourceDocumentList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_report_source_document

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_report_source_document.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyReportSourceDocumentList:
    import capo_bedrock.types.automated_reasoning_policy_report_source_document

    out: AutomatedReasoningPolicyReportSourceDocumentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_report_source_document.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyReportSourceDocumentList,
) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_report_source_document

    return [
        capo_bedrock.types.automated_reasoning_policy_report_source_document.redact_sensitive(
            item
        )
        for item in value
    ]
