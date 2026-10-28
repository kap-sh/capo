"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyGenerateFidelityReportContent``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list


class AutomatedReasoningPolicyGenerateFidelityReportContentDocumentsMember(
    TypedDict, closed=True
):
    documents: "capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list.AutomatedReasoningPolicyGenerateFidelityReportDocumentList"


AutomatedReasoningPolicyGenerateFidelityReportContent: TypeAlias = (
    AutomatedReasoningPolicyGenerateFidelityReportContentDocumentsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(
    value: AutomatedReasoningPolicyGenerateFidelityReportContent,
) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AutomatedReasoningPolicyGenerateFidelityReportContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "documents" in value:
        import capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list

        return {
            "documents": capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list.serialize_json(
                value["documents"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyGenerateFidelityReportContent: no variant present"
        )


def deserialize_json(
    data: dict,
) -> AutomatedReasoningPolicyGenerateFidelityReportContent:
    if data.get("documents") is not None:
        import capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list

        return {
            "documents": capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list.deserialize_json(
                data["documents"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AutomatedReasoningPolicyGenerateFidelityReportContent: no recognized variant key"
        )


def redact_sensitive(
    value: AutomatedReasoningPolicyGenerateFidelityReportContent,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "documents" in value:
        import capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list

        out["documents"] = (
            capo_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list.redact_sensitive(
                value["documents"]
            )
        )
    return out
